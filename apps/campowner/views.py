from django.shortcuts import render, reverse, get_object_or_404
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.views.generic import CreateView
from campowner.forms import CampOwnerRegisterForm
from campowner.models import CampOwner, BlockedPosts
from blog.models import Post


from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator


class CampOwnerCreateView(CreateView):
    template_name = 'accounts/registration/register_campowner.html'
    form_class = CampOwnerRegisterForm

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.user = self.request.user
        messages.success(self.request, "Kamp istediğiniz adminler tarafından incelenip onaylanacak")
        return super(CampOwnerCreateView, self).form_valid(form)

    def get_success_url(self):
        return reverse('home')

def pending_owners(request):
    queryset = CampOwner.objects.filter(is_pending=True)
    context = {
        'object_list': queryset
    }
    return render(request, 'campowner/pending_owners.html', context)

def block_post(request):
    if request.method == 'POST':
        user = request.user
        camp_id = request.POST.get("camp_id")
        campowner = get_object_or_404(CampOwner, id=camp_id)
        BlockedPosts.objects.create(
            user=user,
            campowner=campowner,
        )
        return HttpResponseRedirect("/")

def accept_or_reject(request):
    if request.method == 'POST':
        if 'accept' in request.POST:
            id = request.POST.get("accept")
            campowner = get_object_or_404(CampOwner, id=id)
            campowner.is_active = True
            campowner.is_pending = False
            campowner.save()
        elif 'reject' in request.POST:
            id = request.POST.get("reject")
            campowner = get_object_or_404(CampOwner, id=id)
            campowner.delete()
    return HttpResponseRedirect("/campowner/pending_owners")

def campowner(request, pk=None):
    obj = get_object_or_404(CampOwner, pk=pk)
    blogs = Post.objects.filter(user=obj.user)
    context = {
        'campowner': obj,
        'object_list': blogs,
    }
    return render(request, "campowner/campdetail.html", context)


def camp_owners(request):
    search = request.GET.get("search")
    if search:
        campowners = CampOwner.objects.filter(is_active=True, name__contains=search)
    else:
        campowners = CampOwner.objects.filter(is_active=True)


    paginator = Paginator(campowners, 10) # Show 10 contacts per page
    page = request.GET.get('page')
    campowners_with_page = paginator.get_page(page)
    context = {
        'campowners': campowners_with_page,
        'search': search,
    }
    return render(request, 'campowner/camp_owners.html', context)
