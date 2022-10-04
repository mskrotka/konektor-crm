from django.contrib import admin
from django.utils.html import format_html

from .models import Campaign, Lead, LeadExtend, LandingPage
from clients.models import Customer


@admin.register(Campaign)
class CampaignAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "name",
        "system_ads",
        "customer",
        "default"
    ]
    list_filter = ("customer", "system_ads")

@admin.register(Lead)
class LeadAdmin(admin.ModelAdmin):

    def show_customer(self, obj):
        campaign = Campaign.objects.get(id=obj.campaign.id)
        campaign = campaign.customer.name
        return campaign

    def link_to_clickup(self, obj):
        return format_html("<a href='https://app.clickup.com/t/{url}' target='blank'>#{url}</a>", url=obj.task_clickup_id)

    list_display = [
        "name",
        "rate",
        "created_at",
        "show_customer"
    ]
    list_filter = ("rate",)
    readonly_fields = ["created_at", "link_to_clickup", "lead_extend", "landing_page", "sms_id"]
    exclude = ('task_clickup_id',)

@admin.register(LeadExtend)
class LeadExtendAdmin(admin.ModelAdmin):
    list_display = [
        "id",
    ]
    list_filter = ("id",)
    readonly_fields = ["key_word"]

@admin.register(LandingPage)
class LandingPageAdmin(admin.ModelAdmin):
    list_display = [
        "name",
    ]
    list_filter = ("name",)
    readonly_fields = ["id",]