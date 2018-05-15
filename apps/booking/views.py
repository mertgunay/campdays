from django.shortcuts import render
from booking.forms import ReservationForm
from django.http import HttpResponseRedirect
from camps.models import campLocation
from django.contrib import messages


def booking(request, pk=None):
    camp_location = campLocation.objects.get(pk=pk)

    if request.method == 'POST':
        form = ReservationForm(request.POST)
        print(form)
        if form.is_valid():
            reservation = form.save(commit=False)
            reservation.user = request.user
            reservation.place = camp_location
            reservation.save()
            messages.success(request, "Başarı ile reservasyon yapıldı.")
            return HttpResponseRedirect("/")
    else:
        form = ReservationForm

    context = {
        'form': form,
    }
    return render(request, 'booking/booking.html', context)
