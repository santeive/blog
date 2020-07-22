from django.urls import path
from .feeds import LastestPostsFeed
from . import views

app_name = 'blog'

urlpatterns = [
    # Post views
    # path('', views.PostListView.as_view(), name='post_list'),
    path('', views.post_list, name='post_list'),
    path('tag/<slug:tag_slug>/', views.post_list, name='post_list_by_tag'),
    path('hello/<str:name>', views.hello),
    path('<int:year>/<int:month>/<int:day>/<slug:post>/', views.post_detail, name='post_detail'),
    path('<int:post_id>/share/', views.post_share, name='post_share'),
    path('feed/', LastestPostsFeed(), name='post_feed'),
    path('search/', views.post_search, name='post_search'),
]