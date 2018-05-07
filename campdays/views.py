from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views.generic import View
from blog.models import Post
# Create your views here.
class HomeView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        user = request.user
        followers_ids = [g_p.owner.id for g_p in user.followers.all()]
        queryset = Post.objects.filter(user__id__in=followers_ids).order_by('-timestampt')
        context = {
            'blogs': queryset,
        }
        return render(request, 'home.html', context)
