from django.shortcuts import render
from .forms import EmailVerifierForm
import re
import requests

def verify(request):
    if request.method == 'POST':
        form = EmailVerifierForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            domain = form.cleaned_data['domain']

            # Email verification
            email_regex = r'^[\w\.-]+@[\w\.-]+\.\w+$'
            is_valid_email = bool(re.match(email_regex, email))

            # Domain verification
            dns_url = f"https://dns.google/resolve?name={domain}&type=A"
            response = requests.get(dns_url)

            if response.status_code == 200:
                data = response.json()
                if data.get('Status') == 0:
                    is_valid_domain = True
                else:
                    is_valid_domain = False
            else:
                is_valid_domain = False

            context = {
                'form': form,
                'is_valid_email': is_valid_email,
                'is_valid_domain': is_valid_domain,
            }
            return render(request, 'email_verifier/verify.html', context)
    else:
        form = EmailVerifierForm()

    return render(request, 'email_verifier/verify.html', {'form': form})


# email_verifier/views.py
from django.shortcuts import render

def home_view(request):
    """
    View function to handle the root URL (/)
    """
    context = {
        'title': 'Email and Domain Verifier',
    }
    return render(request, 'email_verifier/home.html', context)