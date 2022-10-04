from rest_framework import serializers

from .models import Lead, LandingPage, LeadExtend, LeadExtend

class LeadExtendSerializer(serializers.ModelSerializer):

    class Meta:
        model = LeadExtend
        fields = ["key_word",]


class LeadSerializer(serializers.ModelSerializer):
    key_word =LeadExtendSerializer(many=True, read_only=True)

    class Meta:
        model = Lead
        fields = ["name", "phone", "info", "rodo", "campaign", "key_word", "landing_page"]