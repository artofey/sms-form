from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from .forms import MessageForm
from .models import System

from .sms_client import send_sms_and_get_status


@login_required
def add_and_save(request):
    """
    обработчик формы для отправки СМС
    :param request:
    :return:
    """
    if request.method == 'POST':
        smsf = MessageForm(request.POST)
        if smsf.is_valid():
            new_sms_form = smsf.save(commit=False)
            current_systems = smsf.cleaned_data['systems']
            text = smsf.cleaned_data['text']
            phone_list = []
            for system in current_systems:
                current_system_id = system.pk
                current_sys = System.objects.get(pk=current_system_id)
                phone_list += [cont.phone for cont in current_sys.contact_set.all()]
            new_sms_form.status = send_sms_and_get_status(list(set(phone_list)), text)
            new_sms_form.save()
            smsf.save_m2m()
            context = {'status': new_sms_form.status}
            return render(request, 'smsapp/smsstatus.html', context)
        else:
            context = {}
            return render(request, 'smsapp/smsform.html', context)
    else:
        smsf = MessageForm()
        context = {'form': smsf}
        return render(request, 'smsapp/smsform.html', context)
