from django.urls import path

from . import views

urlpatterns = [
    path('hello', views.hello_world_view, name="Hello World"),
    path('hello/query/', views.hello_from_path, name="Hello from Path"),
    path('post/example/', views.post_example, name="post_example"),
    path('post/submit/', views.post_submit, name="Post Submit Example"),
]
