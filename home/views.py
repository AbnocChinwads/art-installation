from django.shortcuts import render

# Create your views here.
def index(request):
    """ A view to return the index page """
    return render(request, "index.html")

def gallery(request):
    return render(request, "gallery.html")

def contact(request):
    return render(request, "contact.html")
