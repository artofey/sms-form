from django.views.generic.edit import CreateView
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render

from .forms import MessageForm
from .models import Message, System, Contact

from .sms_client import send_sms_and_get_status


def add_and_save(request):
    if request.method == 'POST':
        smsf = MessageForm(request.POST)
        if smsf.is_valid():
            new_sms_form = smsf.save(commit=False)
            current_system_id = smsf.cleaned_data['system'].id
            current_text = smsf.cleaned_data['text']
            # получаю систему выбранную в форме
            sys = System.objects.get(pk=current_system_id)
            # получаю список телефонов по выбранной системе
            current_phone_list = [cont.phone for cont in sys.contact_set.all()]
            # если выбрана не тестовая группа, то список телефонов дополняется телефонами из группы Default
            if sys.name != 'TEST':
                sys_default = System.objects.get(name='Default')
                default_phone_list = [cont.phone for cont in sys_default.contact_set.all()]
                current_phone_list += default_phone_list
            new_sms_form.status = send_sms_and_get_status(current_phone_list, current_text)
            new_sms_form.save()
            context = {'status': new_sms_form.status}
            return render(request, 'smsapp/smsstatus.html', context)
        else:
            context = {}
            return render(request, 'smsapp/smsform.html', context)
    else:
        smsf = MessageForm()
        context = {'form': smsf}
        return render(request, 'smsapp/smsform.html', context)
