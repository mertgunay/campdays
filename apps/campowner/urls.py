from django.urls import path

from campowner.views import pending_owners, CampOwnerCreateView, accept_or_reject, campowner, camp_owners

app_name = 'campowner'

urlpatterns = [
    path('pending_owners', pending_owners, name='pending_owners'),
    path('campowner', CampOwnerCreateView.as_view(), name="create"),
    path('accept_or_reject', accept_or_reject, name="accept_or_reject"),
    path('camp_owners', camp_owners, name='camp_owners'),

    ## her zaman en aşağıda olmalı. aksi halde bozulur
    path('<pk>', campowner, name="detail"),
   

]
