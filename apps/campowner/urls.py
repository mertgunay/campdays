from django.urls import path

from campowner.views import pending_owners

app_name = 'campowner'

urlpatterns = [
    path('pending_owners', pending_owners, name='pending_owners'),
]
