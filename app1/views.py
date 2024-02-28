from django.shortcuts import render
from .models import AdventurePackage


# Create your views here.


def home(request):
    return render(request,'home/home.html')

def packages(request):
    all_packages = AdventurePackage.objects.all()

    return render(request, 'home/packages.html', {'packages': all_packages})



def detailed_view(request,p):
    a=AdventurePackage.objects.get(name=p)
    return render(request,'home/detailed_view.html', {'a':a})






