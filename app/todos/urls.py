from django.urls import path

from . import views

urlpatterns = [
    path('hello', views.hello_world_view, name="Hello World"),
    path('hello/query/', views.hello_from_path, name="Hello from Path"),
]
