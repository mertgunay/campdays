from django.urls import path

from campowner.views import pending_owners, CampOwnerCreateView, accept_or_reject

app_name = 'campowner'

urlpatterns = [
    path('pending_owners', pending_owners, name='pending_owners'),
    path('campowner/', CampOwnerCreateView.as_view(), name="create"),
    path('accept_or_reject', accept_or_reject, name="accept_or_reject"),
]
