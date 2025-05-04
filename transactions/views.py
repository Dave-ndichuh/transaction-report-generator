
from django.core.mail import EmailMessage
from django.http import HttpResponse
from django.template.loader import render_to_string
from django.views.decorators.csrf import csrf_exempt
import io
from xhtml2pdf import pisa
import secrets

@csrf_exempt
def send_transaction_report(request):
    password = secrets.token_urlsafe(8)

    html = render_to_string('transactions/email_template.html', {'password': password})
    pdf_file = io.BytesIO()
    pisa.CreatePDF(io.BytesIO(html.encode('utf-8')), dest=pdf_file)
    
    email = EmailMessage(
        'Your Transaction Report',
        'Your transaction report is attached. Password: {}'.format(password),
        'noreply@bankreports.com',
        ['user@example.com'],
    )
    email.attach('transaction_report.pdf', pdf_file.getvalue(), 'application/pdf')
    email.send()

    return HttpResponse("Email with PDF sent. Check console.")
