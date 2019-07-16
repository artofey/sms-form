from django.contrib import admin
from .models import Contact, System, Message


class MessageAdmin(admin.ModelAdmin):
    list_display = ('system', 'sended_time')
    list_display_links = ('system',)
    search_fields = ('system', 'text')


admin.site.register(Contact)
admin.site.register(System)
admin.site.register(Message, MessageAdmin)
