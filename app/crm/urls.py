from django.urls import path

from .views import LeadView

app_name = "crm"

urlpatterns = [
    path("lead/", LeadView.as_view(), name="lead"),
]