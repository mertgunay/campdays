from django.shortcuts import render
from booking.forms import ReservationForm
from django.http import HttpResponseRedirect
from camps.models import campLocation
from django.contrib import messages
from booking.models import Reservation

import datetime
def booking(request, pk=None):
    camp_location = campLocation.objects.get(pk=pk)

    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            reservation = form.save(commit=False)
            reservation.user = request.user
            reservation.place = camp_location
            if calculateAvailability(camp_location, reservation):
                reservation.save()
                messages.success(request, "Başarı ile reservasyon yapıldı.")
            else:
                messages.error(request, "Kapasite yetersiz.")
            return HttpResponseRedirect("/")
    else:
        form = ReservationForm

    context = {
        'form': form,
    }
    return render(request, 'booking/booking.html', context)

def daterange(d1, d2):
    return (d1 + datetime.timedelta(days=i) for i in range((d2 - d1).days + 1))

def calculateAvailability(camp_location, reservation):
    tents  = 0
    guests = 0
    queryset = Reservation.objects.filter(place=camp_location)
    for r in queryset:
        for date in daterange(r.check_in, r.check_out):
            for date2 in daterange(reservation.check_in, reservation.check_out):
                if (date == date2):
                    tents += r.tents
                    tents += reservation.tents
                    guests += r.guests
                    guests += reservation.guests
            print(date)
            print("bugün için toplam")
            print(tents, guests)


    print("Total tents=", tents, "Total guests=", guests)
    return True



def list_reservations(request):

    queryset = Reservation.objects.filter(user=User)
    if queryset.exists():

    else:
        data["error"] = ""
