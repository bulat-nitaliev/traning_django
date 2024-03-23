from django.contrib import admin
from .models import TeleSettings

@admin.register(TeleSettings)
class TeleSettingsModelAdmin(admin.ModelAdmin):
    list_display = (
        'tg_token',
        'tg_chat',
        'tg_message',
    )
    fields = (
        'tg_token',
        'tg_chat',
        'tg_message',
    )
