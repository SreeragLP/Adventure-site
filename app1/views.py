from django.shortcuts import render,redirect
from .models import AdventurePackage,Rating



# Create your views here.


def home(request):
    return render(request,'home/home.html')

def packages(request):
    all_packages = AdventurePackage.objects.all()

    return render(request, 'home/packages.html', {'packages': all_packages})



def detailed_view(request,p):
    a=AdventurePackage.objects.get(name=p)
    return render(request,'home/detailed_view.html', {'a':a})






def rating(request):
    if request.method == 'POST':
        rating = request.POST.get('starRating')
        feedback = request.POST.get('textbox')
        Rating.objects.create(rating=rating, feedback=feedback)
        return redirect('app1:thanks')  # Redirect to a thank you page after submission
    return render(request, 'home/rating.html')

def thanks(request):
    return render(request, 'home/thanks.html')





def review(request):
    ratings = Rating.objects.all()
    return render(request, 'home/review.html', {'ratings': ratings})





