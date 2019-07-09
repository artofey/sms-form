from django.views.generic.edit import CreateView

from .forms import MessageForm
from .models import Message


class SmsCreateView(CreateView):
    template_name = 'smsapp/smsform.html'
    form_class = MessageForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['messages'] = Message.objects.all()
        return context
