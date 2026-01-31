from django.http import HttpResponse
from django.shortcuts import render

def hello_world_view(request):
    return render(request, "todos/hello.html")

def hello_from_path(request):
    name = request.GET.get("q")

    return HttpResponse(f"Hello {name}!")
