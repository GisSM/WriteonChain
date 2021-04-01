from django.urls import path
from . import views

urlpatterns = [
       path('',views.post_lastfive,name='homepage'),
       path('post_all',views.post_all,name='post/all'),
       path('<int:id>/<slug:slug>/',views.post_detail, name='post_detail'),
       path('<int:id>/<slug:slug>/edit',views.post_edit, name='post_edit'),
       path('post_new/',views.post_new,name='post_new'),
       path('<user>/<id>',views.post_profilo, name='post_profilo'),
       path('api_post/',views.api_post,name='api_post'),
       path('post_api_all/',views.post_api_all, name='post_api_all'),
       path('post_api_1h/',views.post_api_1h, name='post_api_1h'),
       path('admin_conta_post',views.admin_count_post, name='admin_conta_post'),

]