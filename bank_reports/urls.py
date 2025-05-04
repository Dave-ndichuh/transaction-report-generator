
from django.contrib import admin
from django.urls import path
from transactions.views import send_transaction_report

urlpatterns = [
    path('admin/', admin.site.urls),
    path('send-report/', send_transaction_report, name='send_report'),
]
