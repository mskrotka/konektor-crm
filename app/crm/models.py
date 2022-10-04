import uuid
from django.db import models
from django.utils import timezone

from clients.models import Customer


class Campaign(models.Model):
    SYSTEM_ADS = [
        (1, "Google Ads"),
        (2, "Facebook Ads"),
        (3, "Internet"),
        (4, "Newsletter"),
    ]
    id = models.CharField(max_length=32, primary_key=True)
    name = models.CharField(max_length=256)
    description = models.TextField(blank=True, null=True)
    customer = models.ForeignKey(Customer, on_delete=models.DO_NOTHING, null=True, blank=True)
    system_ads = models.SmallIntegerField(choices=SYSTEM_ADS, null=True, blank=True)
    default = models.BooleanField(default=False)

    def __str__(self):
        if self.customer is None:
            text = f"{self.name}"
        else:
            text = f"{self.name} - {self.customer}"
        return text

    def get_name_system_ads(self):
        get_name = [item for item in self.SYSTEM_ADS if item[0] == self.system_ads]
        return f"{get_name[0][1]}"


class Lead(models.Model):
    RATE_STATUS = [
        (1, "Good"),
        (2, "Bad"),
        (3, "Duplicate"),
    ]

    rate = models.SmallIntegerField(choices=RATE_STATUS, default=1)
    name = models.CharField(max_length=128)
    phone = models.CharField(max_length=15)
    info = models.TextField(blank=True, null=True)
    rodo = models.BooleanField(default=False)
    campaign = models.ForeignKey("Campaign", on_delete=models.DO_NOTHING)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)
    task_clickup_id = models.CharField(max_length=12, blank=True, null=True)
    lead_extend = models.ForeignKey("LeadExtend", on_delete=models.DO_NOTHING, blank=True, null=True)
    landing_page = models.ForeignKey("LandingPage", on_delete=models.DO_NOTHING, null=True, blank=True)
    sms_id = models.CharField(max_length=128, blank=True, null=True)

    def __str__(self):
        return f"{self.phone}"


class LeadExtend(models.Model):
    key_word = models.CharField(max_length=256, blank=True, null=True)

    def __str__(self):
        return f"Słowo kluczowe: {self.key_word}"


class LandingPage(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    name = models.CharField(max_length=256, blank=True, null=True)
    link = models.CharField(max_length=256, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    customer = models.ForeignKey(Customer, on_delete=models.DO_NOTHING)

    def __str__(self):
        return f"{self.link}"