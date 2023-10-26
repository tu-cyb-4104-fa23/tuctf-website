from django.shortcuts import render

# Create your views here.

def index(request):
    """ The home page for tuctf. """
    return render(request, 'core_site/index.html')

