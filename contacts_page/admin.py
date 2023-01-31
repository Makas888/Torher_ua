from django.contrib import admin
from contacts_page.models import UserMessage, ContactList


@admin.register(UserMessage)
class UserMessageAdmin(admin.ModelAdmin):
    list_display = ['name', 'archived', 'email', 'phone', 'message', 'date_archiving', 'date_in']
    list_filter = ['date_archiving', 'date_in', 'archived']
    list_editable = ['archived']
    list_display_links = ['name', 'email', 'phone', 'message']


admin.site.register(ContactList)
