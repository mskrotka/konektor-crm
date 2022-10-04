from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import permission_classes
from django.core.exceptions import ObjectDoesNotExist

from .serializers import LeadSerializer
from .models import Campaign, Lead, LeadExtend, LandingPage

from core.tools.change_to_number import change_to_number
from core.tools.lead.lead_to_clickup import lead_to_clickup
from core.tools.smsapi.send_sms import send_sms


def update_key_word(lead, key_word):
    if len(key_word) > 0:
        lead_extend = LeadExtend.objects.create(key_word=key_word)
        new_lead = Lead.objects.filter(id=lead.id).update(lead_extend=lead_extend)
        new_lead = Lead.objects.get(id=lead.id)
    else:
        new_lead = Lead.objects.get(id=lead.id)
    return new_lead



@permission_classes([])
class LeadView(APIView):
    serializer_class = LeadSerializer

    def post(self, request):
        data = request.POST
        serializer = LeadSerializer(data=data)
        customer = LandingPage.objects.get(id=data["landing_page"]).customer

        try:
            Campaign.objects.get(id=data["campaign"])
        except ObjectDoesNotExist:
            data = data.copy()
            data["campaign"] = Campaign.objects.get(customer=customer, default=True).id
            post = Campaign.objects.get(id=data["campaign"])
            post.save()

        serializer = LeadSerializer(data=data)

        if serializer.is_valid():
            serializer.validated_data["phone"] = change_to_number(serializer.validated_data["phone"])
            new_lead = serializer.save()

            new_lead = update_key_word(new_lead, data["key_word"])

            new_lead = send_sms(new_lead)

            lead_to_clickup(new_lead)

            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)