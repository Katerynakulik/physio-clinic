from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import Booking
from accounts.utils import is_client


# Client creates booking

@login_required
def create_booking(request, physio_id):
    if not is_client(request.user):
        return redirect('login')

    if request.method == 'POST':
        Booking.objects.create(
            client=request.user.clientprofile,
            physiotherapist_id=physio_id,
            date=request.POST['date'],
            time=request.POST['time']
        )
        return redirect('client_dashboard')

    return render(request, 'bookings/create.html')


# Physiotherapist blocks slots

@login_required
def block_slot(request):
    if not hasattr(request.user, 'physiotherapist'):
        return redirect('login')

    if request.method == 'POST':
        BlockedSlot.objects.create(
            physiotherapist=request.user.physiotherapist,
            date=request.POST['date'],
            time=request.POST['time']
        )
        return redirect('physio_dashboard')
