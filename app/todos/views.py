from django.http import HttpResponse, HttpResponseNotAllowed
from django.shortcuts import render

def hello_world_view(request):
    return render(request, "todos/hello.html")

def hello_from_path(request):
    name = request.GET.get("q")

    return HttpResponse(f"Hello {name}!")

def post_example(request):
    if request.method == "POST":
        name = request.POST.get("name")
        age = request.POST.get("age")
        job = request.POST.get("job")

        return HttpResponse(f"You input data: {name}, {age}, {job}")
    else:
        return HttpResponseNotAllowed("POST")

def post_submit(request):
    return render(request, "todos/post_submit.html")
