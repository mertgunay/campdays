from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views.generic import View
from blog.models import Post
# Create your views here.
class HomeView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        user = request.user
        campowners_ids = [c_o.owner.id for c_o in user.followers.all()]
        queryset = Post.objects.filter(
                user__campowner__id__in=campowners_ids
            ).order_by('-timestampt')
        context = {
            'blogs': queryset,
        }
        return render(request, 'home.html', context)
