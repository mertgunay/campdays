from django.shortcuts import render, reverse
from django.views.generic import CreateView
from campowner.forms import CampOwnerRegisterForm

class CampOwnerCreateView(CreateView):
    template_name = 'accounts/registration/register_campowner.html'
    form_class = CampOwnerRegisterForm

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.user = self.request.user
        return super(CampOwnerCreateView, self).form_valid(form)

    def get_success_url(self):
        return reverse('home')

def pending_owners(request):
    return render(request, 'campowner/pending_owners.html', {})
