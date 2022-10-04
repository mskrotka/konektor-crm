from email.policy import default
import time

from crm.models import Lead

from ..clickup.create_task import create_task_clickup
from .description_tasks import description_lead
from ..clickup.get_custom_field import get_custom_fields, check_exist


def user_test(lead):
    if lead.name == "test":
        user = ""
    else:
        user = [lead.campaign.customer.clickup_user_id]
    return user

def update_clickup_task(lead, task_id):
    new_lead = Lead.objects.filter(id=lead.id).update(task_clickup_id=task_id)
    new_lead = Lead.objects.get(id=lead.id)
    return new_lead

def set_source(lead):
    source_name = lead.campaign.get_name_system_ads()
    list_clickup = lead.campaign.customer.primary_list_clickup
    token_clickup = lead.campaign.customer.token_clickup
    name_field = "Źródło"
    source_clickup_id = get_custom_fields(source_name, list_clickup, token_clickup, name_field)

    if source_clickup_id:
        source = {
            "id": lead.campaign.customer.clickup_source_id,
            "value": source_clickup_id
        }
    else:
        source = {}
    return source


def set_phone(lead):
    list_clickup = lead.campaign.customer.primary_list_clickup
    token_clickup = lead.campaign.customer.token_clickup
    name_field = "Numer kontaktowy"
    exist = check_exist(list_clickup, token_clickup, name_field)

    if exist:
        phone = {
            "id": lead.campaign.customer.clickup_phone_id,
            "value": lead.phone,
        }
    else:
        phone = {}
    return phone


def set_campaign(lead):
    campaign_name = lead.campaign.name
    list_clickup = lead.campaign.customer.primary_list_clickup
    token_clickup = lead.campaign.customer.token_clickup
    name_field = "Kampania"
    campaign_clickup_id = get_custom_fields(campaign_name, list_clickup, token_clickup, name_field)

    if campaign_clickup_id:
        campaign = {
            "id": lead.campaign.customer.clickup_campaign_id,
            "value": campaign_clickup_id
        }
    else:
        campaign = {}
    return campaign

def lead_to_clickup(lead):
    unix_time = int(round(time.time() * 1000))

    url = "https://api.clickup.com/api/v2/list/" + lead.campaign.customer.primary_list_clickup + "/task"

    data = {
        "name": lead.name + " " + "[" + lead.phone[-3:] + "]",
        "assignees": user_test(lead),
        "markdown_description": description_lead(lead),
        "due_date": unix_time + 432000000,
        "due_date_time": "false",
        "start_date": unix_time,
        "start_date_time": "false",
        "notify_all": "true",
        "custom_fields": [
            set_phone(lead),
            set_source(lead),
            set_campaign(lead),
        ]
    }

    task_id = create_task_clickup(url, data, lead.campaign.customer.token_clickup)
    update_clickup_task(lead, task_id)

    if lead.campaign.customer.secondary_list_lickup is not None:

        url = "https://api.clickup.com/api/v2/list/" + lead.campaign.customer.secondary_list_lickup + "/task"

        data = {
            "name": lead.campaign.customer.name_second_task + " " + "[" + lead.phone[-3:] + "]",
            "assignees": user_test(lead),
            "description": "",
            "links_to": task_id,
            "start_date": unix_time,
            "due_date": unix_time + 172800000,
        }

        create_task_clickup(url, data, lead.campaign.customer.token_clickup)
    return task_id