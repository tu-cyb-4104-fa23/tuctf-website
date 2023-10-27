from django.shortcuts import render

# Create your views here.

def index(request):
    """ The home page for TUCTF """
    return render(request, 'core_site/index.html')


def tuctf_2023(request):
    """ Page TUCTF 2023 """
    return render(request, 'core_site/tuctf_2023.html')


def rules_2023(request):
    """ Page Rules """
    return render(request, 'core_site/rules_2023.html')