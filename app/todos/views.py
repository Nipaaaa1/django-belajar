from django.http import HttpResponse, HttpResponseNotAllowed
from django.shortcuts import render

from .forms import PersonForm

def hello_world_view(request):
    return render(request, "todos/hello.html")

def hello_from_path(request):
    name = request.GET.get("q")

    return HttpResponse(f"Hello {name}!")

def post_example(request):
    if request.method == "POST":
        form = PersonForm(request.POST)

        if form.is_valid():
            name = form.cleaned_data["name"]
            age = form.cleaned_data["age"]
            job = form.cleaned_data["job"]

            return HttpResponse(f"You input data: {name}, {age}, {job}")
    else:
        return HttpResponseNotAllowed("POST")

def post_submit(request):
    form = PersonForm()
    return render(request, "todos/post_submit.html", { "form": form })

def templating_example(request):
    context = {
        "name": "Nipa",
        "age": 20,
        "skills": ["Typescript", "Python", "Django", "Docker"]
    }

    return render(request, "todos/templating.html", context)
