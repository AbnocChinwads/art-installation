from django.shortcuts import render

from .models import Image

# Create your views here.
def index(request):
    """ A view to return the index page """
    return render(request, "index.html")

def gallery(request):
    images = Image.objects.all()
    context = {
        "images": images,
    }
    return render(request, "gallery.html", context)

def contact(request):
    return render(request, "contact.html")
