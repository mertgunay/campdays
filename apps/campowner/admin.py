from django.contrib import admin

from campowner.models import CampOwner, CampProfile, BlockedPosts

admin.site.register(CampOwner)
admin.site.register(CampProfile)
admin.site.register(BlockedPosts)
