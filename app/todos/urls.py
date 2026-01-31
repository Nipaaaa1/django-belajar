from django.urls import path

from . import views

urlpatterns = [
    path('hello', views.hello_world_view, name="Hello World"),
    path('hello/query/', views.hello_from_path, name="Hello from Path"),
    path('post/example/', views.post_example, name="post_example"),
    path('post/submit/', views.post_submit, name="Post Submit Example"),
    path('templating/', views.templating_example, name="templating"),
    path('todos/', views.todos_view, name="todos_view"),
    path('person/<int:person_id>', views.person_details_view, name="person_detail"),

]
