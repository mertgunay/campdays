from django.urls import path
from blog.views import (
    blog_home,
    blog_detail,
    blog_list,
    blog_update,
    blog_delete,
)

app_name = 'blog'

urlpatterns = [
    path('home/', blog_home),
    path('(?P<id>\d+)/', blog_detail),
    path('list/', blog_list),
    path('update/', blog_update),
    path('delete/', blog_delete),

]
