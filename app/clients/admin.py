from django.contrib import admin

from .models import Customer


@admin.register(Customer)
class ClientsAdmin(admin.ModelAdmin):
    list_display = ["name"]