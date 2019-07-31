from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from .forms import MessageForm
from .models import System

from .sms_client import send_sms_and_get_status


@login_required
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
