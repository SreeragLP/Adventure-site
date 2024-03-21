from django.http import JsonResponse
from django.views.decorators.csrf import ensure_csrf_cookie
from .models import YourResponse
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from .models import AdventurePackage, Rating
from datetime import datetime, timedelta




@ensure_csrf_cookie
def home(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        your_response = YourResponse.objects.create(name=name, email=email, subject=subject, message=message)
        your_response.save()

        # Return JSON response indicating success
        return JsonResponse({'success': True})
    else:
        return render(request, 'home/home.html')



def about(request):
    return render(request, 'home/about.html')

def packages(request):
    all_packages = AdventurePackage.objects.all()
    return render(request, 'home/packages.html', {'packages': all_packages})



def detailed_view(request,p):
    a=AdventurePackage.objects.get(name=p)
    # Calculate the maximum date (90 days from today)
    max_date = (datetime.today() + timedelta(days=90)).strftime('%Y-%m-%d')
    return render(request,'home/detailed_view.html', {'a':a, 'max_date': max_date})


def rating(request, package_name):
    adventure_package = get_object_or_404(AdventurePackage, name=package_name)
    context = {'package_name': adventure_package.name}

    if request.method == 'POST':
        rating_value = request.POST.get('starRating')
        feedback = request.POST.get('textbox')

        if rating_value is not None:
            # Get the currently logged-in user
            user = request.user
            # Create the rating object associated with the user and package
            rating_obj = Rating.objects.create(user=user, package=adventure_package, rating=rating_value,
                                               feedback=feedback,has_rated = True)
            # Update the has_rated field of the Rating object
            # rating_obj.has_rated = True
            rating_obj.save()
            return redirect('app1:thanks')

    return render(request, 'home/rating.html', context)



def thanks(request):
    return render(request, 'home/thanks.html')



def review(request):
    ratings = Rating.objects.all()
    return render(request, 'home/review.html', {'ratings': ratings})







