from django.shortcuts import render,redirect
from .models import AdventurePackage,Cart
from .models import Cart
from django.contrib.auth.models import User



# Create your views here.

# def add_to_cart(request,p):
#
#     if request.user.is_authenticated:  #its for login required purpose
#
#         a = AdventurePackage.objects.get(name=p)
#         user = request.user
#         try:
#             cart = Cart.objects.get(user=user, items=a)
#             cart.total_persons += 1
#             cart.save()
#         except Cart.DoesNotExist:
#             cart = Cart.objects.create(items=a, user=user, total_persons=1)
#             cart.save()
#             return redirect('cart:cart_view')
#     else:
#         return redirect('UserAuthentication:user_login')
#
#
#
#
#
# def cart_view(request):
#     if request.user.is_authenticated:  # its for login required purpose
#
#
#         user = request.user
#         cart_items = Cart.objects.filter(user=user)
#
#         total = 0
#         for item in cart_items:
#             total += item.subtotal()
#
#         return render(request, 'cart/cart_view.html', {
#             'cart_items': cart_items,
#             'total': total,
#         })
#     else:
#         return redirect('UserAuthentication:user_login')

def add_to_cart(request,p ):
    package=AdventurePackage.objects.get(name=p)
    user=request.user
    try:
        cart=Cart.objects.get(user=user,items=package)

        cart.total_persons+=1
        cart.save()

    except Cart.DoesNotExist:

        cart=Cart.objects.create(items=package,user=user,total_persons=1)
        cart.save()

    return redirect('cart:cart_view')

def cart_view(request):
    user= request.user
    cart=Cart.objects.filter(user=user)
    return render(request,'cart/cart_view.html',{'cart':cart})



def cart_remove(request,p):
    package=AdventurePackage.objects.get(name=p)
    user=request.user
    try:
        cart=Cart.objects.get(user=user,items=package)
        if(cart.total_persons>1):
            cart.total_persons-=1
            cart.save()

        else:
            cart.delete()

    except:
        pass
    return redirect('cart:cart_view')


def full_remove(request,p):
    package = AdventurePackage.objects.get(name=p)
    user = request.user
    try:
        cart = Cart.objects.get(user=user, items=package)
        cart.delete()
    except:
        pass
    return redirect('cart:cart_view')
