from django.urls import path

from .views import SmsCreateView

urlpatterns = [
    path('', SmsCreateView.as_view(), name='smsform'),
]
