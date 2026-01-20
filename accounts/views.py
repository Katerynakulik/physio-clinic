from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from .forms import ClientRegistrationForm
from .models import ClientProfile

def register_client(request):
    if request.method == 'POST':
        form = ClientRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            ClientProfile.objects.create(user=user)
            login(request, user)
            return redirect('client_dashboard')
    else:
        form = ClientRegistrationForm()

    return render(request, 'accounts/register.html', {'form': form})

def client_dashboard(request):
    """
    Dashboard page for logged-in clients.
    Shows future appointments and booking options.
    """
    return render(request, 'accounts/client_dashboard.html')
