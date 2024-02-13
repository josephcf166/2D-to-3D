from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from .forms import UsersGLBForm
from .models import UsersGLB

def index(request):
    return render(request, "index.html", {})

def home(request):
    if request.method == "POST":
        glb = UsersGLBForm(request.POST, request.FILES)
        if glb.is_valid():
            uploaded_glb = glb.save()
            glb_url = uploaded_glb.glb_file.url
            return render(request, "rendered_glb.html", {"glb_url": glb_url})

    else:
        form = UsersGLBForm()
    return render(request, "home.html", {"form": form})
