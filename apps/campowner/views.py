from django.shortcuts import render


def pending_owners(request):
    return render(request, 'campowner/pending_owners.html', {})
