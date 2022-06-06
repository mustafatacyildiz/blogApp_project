from django.urls import path
from .views import post_list, post_create, blog_detail, blog_update, blog_delete

urlpatterns = [
    path('list/', post_list , name='list'),
    path('create/', post_create , name='create'),
    path('detail/<int:id>', blog_detail , name='detail'),
    path('update/<int:id>', blog_update , name='update'),
    path('delete/<int:id>', blog_delete , name='delete'),
]