from django.forms import ModelForm, CheckboxSelectMultiple

from .models import Message


class MessageForm(ModelForm):
    class Meta:
        model = Message
        fields = ('text', 'systems')
        widgets = {'systems': CheckboxSelectMultiple}
