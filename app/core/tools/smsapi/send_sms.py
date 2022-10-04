from smsapi.client import SmsApiPlClient

from crm.models import Lead

def send_sms(lead):
    if lead.campaign.customer.token_sms is not None:
        token = lead.campaign.customer.token_sms
        phone = lead.phone

        client = SmsApiPlClient(access_token=token)
        try:
            send_results = client.sms.send(to=phone, template='NowyLead')
            for result in send_results:
                if result.error == None:
                    to_class = result.id
                else:
                    to_class = result.error
        except:
            to_class = "Niepoprawny numer telefonu lub brak środków na SMS API"
    else:
        to_class = ""

    new_lead = Lead.objects.filter(id=lead.id).update(sms_id=to_class)
    new_lead = Lead.objects.get(id=lead.id)

    return new_lead
