from django.urls import path

from .views import add_and_save

urlpatterns = [
    path('', add_and_save, name='smsform'),
]
