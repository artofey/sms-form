from django.contrib import admin
from django.db import models
from django.forms import CheckboxSelectMultiple
from .models import Contact, System, Message


class MessageAdmin(admin.ModelAdmin):
    list_display = ('sended_time', 'status')
    list_display_links = ('sended_time',)
    search_fields = ('systems', 'text')
    formfield_overrides = {
        models.ManyToManyField: {'widget': CheckboxSelectMultiple},
    }


class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone')
    list_display_links = ('name',)
    search_fields = ('name', 'phone')
    formfield_overrides = {
        models.ManyToManyField: {'widget': CheckboxSelectMultiple},
    }


admin.site.register(Contact, ContactAdmin)
admin.site.register(System)
admin.site.register(Message, MessageAdmin)
