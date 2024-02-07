from django.shortcuts import render

def index(request):
    return render(request, "index.html", {})

def hello_world(request):
    return render(request, "hello_world.html", {})
