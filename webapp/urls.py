from django.urls import path

from webapp.views import *
from django.conf import settings
from django.conf.urls.static import static


app_name = 'webapp'

urlpatterns = [
    path('', index, name='home'),
    path('payment_success/', payment_success, name='payment_success'),
    path('payment_error/', payment_error, name='payment_error'),
    ]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
