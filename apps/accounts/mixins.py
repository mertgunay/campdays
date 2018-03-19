from django.contrib.auth.mixins import AccessMixin
from django.core.exceptions import PermissionDenied

class OwnerRequiredMixin(object):
    """Verify that the current user is owner."""
    def dispatch(self, request, *args, **kwargs):
        if not request.user == self.get_object():
            raise PermissionDenied
        return super(OwnerRequiredMixin, self).dispatch(request, *args, **kwargs)
