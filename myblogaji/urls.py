from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/tag/<int:pk>/', views.post_tag, name='post_tag'),
    path('post/search/', views.post_search, name='post_search'),
    path('post/like/<int:pk>/', views.post_like, name='post_like'),
    path('post/dislike/<int:pk>/', views.post_dislike, name='post_dislike'),
    path('post/new/', views.post_new, name='post_new'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
    path('post/<int:pk>/command/', views.post_command, name='post_command'),
]