from django.urls import path
from blog.views import (
    blog_create,
    blog_detail,
    blog_list,
    blog_update,
    blog_delete,
)

app_name = 'blog'

urlpatterns = [
    path('', blog_list, name='list'),
    path('create', blog_create),
    path('<id>', blog_detail, name='blog_detail'),
    path('<id>/update/', blog_update, name='blog_update'),
    path('<id>/delete/', blog_delete),

]
