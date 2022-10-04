import uuid
from django.db import models


class Customer(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    name = models.CharField(max_length=256)
    primary_list_clickup = models.CharField(max_length=256, null=True, blank=True)
    secondary_list_lickup = models.CharField(max_length=256, null=True, blank=True)
    tertiary_list_lickup = models.CharField(max_length=256, null=True, blank=True)
    name_second_task = models.CharField(max_length=256, null=True, blank=True)
    name_tertiary_task = models.CharField(max_length=256, null=True, blank=True)
    token_clickup = models.CharField(max_length=256, null=True, blank=True)
    clickup_user_id = models.CharField(max_length=24, null=True, blank=True)
    clickup_phone_id = models.CharField(max_length=128, null=True, blank=True)
    clickup_campaign_id = models.CharField(max_length=128, null=True, blank=True)
    clickup_source_id = models.CharField(max_length=128, null=True, blank=True)
    token_sms = models.CharField(max_length=256, null=True, blank=True)

    def __str__(self):
        return f"{self.name}"