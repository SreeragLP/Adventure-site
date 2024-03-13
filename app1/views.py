from django.shortcuts import render,redirect
from .models import AdventurePackage,Rating,YourResponse



# Create your views here.


# def home(request):
#
#     if request.method == "POST":
#         name = request.POST['name']
#         email = request.POST['email']
#         subject = request.POST['subject']
#         message = request.POST['message']
#
#         your_response = YourResponse.objects.create(name=name, email=email, subject=subject,
#                                            message=message)
#
#         your_response.save()
#     else:
#         pass
#
#
#
#     return render(request,'home/home.html')



from django.http import JsonResponse
from django.views.decorators.csrf import ensure_csrf_cookie
from .models import YourResponse

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




def packages(request):
    all_packages = AdventurePackage.objects.all()

    return render(request, 'home/packages.html', {'packages': all_packages})



def detailed_view(request,p):
    a=AdventurePackage.objects.get(name=p)
    return render(request,'home/detailed_view.html', {'a':a})





#og code
# def rating(request):
#     if request.method == 'POST':
#         rating = request.POST.get('starRating')
#         feedback = request.POST.get('textbox')
#         Rating.objects.create(rating=rating, feedback=feedback)
#         return redirect('app1:thanks')  # Redirect to a thank you page after submission
#     return render(request, 'home/rating.html')


from django.contrib.auth.decorators import login_required  # Import the login_required decorator

# from django.shortcuts import render, redirect, get_object_or_404
# from .models import AdventurePackage
#
# def rating(request, package_name):
#     adventure_package = get_object_or_404(AdventurePackage, name=package_name)
#     context = {'package_name': adventure_package.name}
#     if request.method == 'POST':
#         rating_value = request.POST.get('starRating')
#         feedback = request.POST.get('textbox')
#         if rating_value is not None:
#             # Get the currently logged-in user
#             user = request.user
#             # Create the rating object associated with the user and package
#             # Modify this part according to your Rating model
#             Rating.objects.create(user=user, package=adventure_package, rating=rating_value, feedback=feedback)
#             return redirect('app1:thanks')
#     return render(request, 'home/rating.html', context)


from django.shortcuts import render, redirect, get_object_or_404
from .models import AdventurePackage, Rating


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


# from django.contrib import messages
#
#
# def rating(request, package_name):
#     adventure_package = get_object_or_404(AdventurePackage, name=package_name)
#     context = {'package_name': adventure_package.name}
#
#     if request.method == 'POST':
#         rating_value = request.POST.get('starRating')
#         feedback = request.POST.get('textbox')
#
#         if rating_value is not None:
#             # Get the currently logged-in user
#             user = request.user
#
#             # Check if the user has already rated the package
#             if Rating.objects.filter(user=user, package=adventure_package).exists():
#                 # User has already rated the package
#                 # Display a message informing the user
#                 message = 'You have already rated this package.'
#                 context['message'] = message
#                 return redirect('app1:thanks')
#
#             # Create the rating object associated with the user and package
#             rating_obj = Rating.objects.create(user=user, package=adventure_package, rating=rating_value,
#                                                feedback=feedback)
#
#             # Update the has_rated field of the Rating object
#             rating_obj.has_rated = True
#             rating_obj.save()
#
#             return redirect('app1:thanks')
#
#     return render(request, 'home/rating.html', context)


#
# from django.shortcuts import render, get_object_or_404, redirect
# from django.contrib import messages
# from .models import AdventurePackage, Rating
# from django.contrib.auth.decorators import login_required

@login_required
# def rating(request, package_name):
#     adventure_package = get_object_or_404(AdventurePackage, name=package_name)
#     context = {'package_name': adventure_package.name}
#
#     if request.method == 'POST':
#         rating_value = request.POST.get('starRating')
#         feedback = request.POST.get('textbox')
#
#         if rating_value is not None:
#             # Get the currently logged-in user
#             user = request.user
#
#             # Check if the user has already rated the package
#             if Rating.objects.filter(user=user, package=adventure_package).exists():
#                 # User has already rated the package
#                 # Display a message informing the user
#                 message = 'You have already rated this package.'
#                 context['message'] = message
#                 return redirect('app1:thanks')
#
#             # Create the rating object associated with the user and package
#             rating_obj = Rating.objects.create(user=user, package=adventure_package, rating=rating_value,
#                                                feedback=feedback)
#
#             # Update the has_rated field of the Rating object
#             rating_obj.has_rated = True
#             rating_obj.save()
#
#             return redirect('app1:thanks')
#
#     return render(request, 'home/rating.html', context)







def thanks(request):
    return render(request, 'home/thanks.html')





def review(request):
    ratings = Rating.objects.all()
    return render(request, 'home/review.html', {'ratings': ratings})





