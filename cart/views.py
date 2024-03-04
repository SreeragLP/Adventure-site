from django.shortcuts import render,redirect
from .models import AdventurePackage,Cart
from .models import Cart
from django.contrib.auth.models import User
# #
# #
# #
# # # Create your views here.
# #
# # # def add_to_cart(request,p):
# # #
# # #     if request.user.is_authenticated:  #its for login required purpose
# # #
# # #         a = AdventurePackage.objects.get(name=p)
# # #         user = request.user
# # #         try:
# # #             cart = Cart.objects.get(user=user, items=a)
# # #             cart.total_persons += 1
# # #             cart.save()
# # #         except Cart.DoesNotExist:
# # #             cart = Cart.objects.create(items=a, user=user, total_persons=1)
# # #             cart.save()
# # #             return redirect('cart:cart_view')
# # #     else:
# # #         return redirect('UserAuthentication:user_login')
# # #
# # #
# # #
# # #
# # #
# # # def cart_view(request):
# # #     if request.user.is_authenticated:  # its for login required purpose
# # #
# # #
# # #         user = request.user
# # #         cart_items = Cart.objects.filter(user=user)
# # #
# # #         total = 0
# # #         for item in cart_items:
# # #             total += item.subtotal()
# # #
# # #         return render(request, 'cart/cart_view.html', {
# # #             'cart_items': cart_items,
# # #             'total': total,
# # #         })
# # #     else:
# # #         return redirect('UserAuthentication:user_login')
# #
# # # def add_to_cart(request,p ):
# # #     package=AdventurePackage.objects.get(name=p)
# # #     user=request.user
# # #     try:
# # #         cart=Cart.objects.get(user=user,items=package)
# # #
# # #         cart.total_persons+=1
# # #         cart.save()
# # #
# # #     except Cart.DoesNotExist:
# # #
# # #         cart=Cart.objects.create(items=package,user=user,total_persons=1)
# # #         cart.save()
# # #
# # #     return redirect('cart:cart_view')
# #
# #
# # from django.shortcuts import render, redirect
# # from .models import AdventurePackage, Cart
# #
# # def add_to_cart(request, p):
# #     if request.method == 'POST':
# #         package_name = p
# #         selected_date = request.POST.get('selected_date')
# #         package = AdventurePackage.objects.get(name=package_name)
# #         user = request.user
# #         try:
# #             cart = Cart.objects.get(user=user, items=package, selected_date=selected_date)
# #             cart.total_persons += 1
# #             cart.save()
# #         except Cart.DoesNotExist:
# #             if selected_date:
# #                 cart = Cart.objects.create(items=package, user=user, total_persons=1, selected_date=selected_date)
# #                 cart.save()
# #             else:
# #                 error_message = "Please select a date for the package."
# #                 return render(request, 'your_detailed_view_template.html', {'a': package, 'error_message': error_message})
# #         return redirect('cart:cart_view')
# #     else:
# #         package = AdventurePackage.objects.get(name=p)
# #         return render(request, 'home/detailed_view.html', {'a': package})
# #
# #
# # def cart_view(request):
# #     user= request.user
# #     cart=Cart.objects.filter(user=user)
# #     return render(request,'cart/cart_view.html',{'cart':cart})
# #
# #
# #
# # def cart_remove(request,p):
# #     package=AdventurePackage.objects.get(name=p)
# #     user=request.user
# #     try:
# #         cart=Cart.objects.get(user=user,items=package)
# #         if(cart.total_persons>1):
# #             cart.total_persons-=1
# #             cart.save()
# #
# #         else:
# #             cart.delete()
# #
# #     except:
# #         pass
# #     return redirect('cart:cart_view')
# #
# #
# # def full_remove(request,p):
# #     package = AdventurePackage.objects.get(name=p)
# #     user = request.user
# #     try:
# #         cart = Cart.objects.get(user=user, items=package)
# #         cart.delete()
# #     except:
# #         pass
# #     return redirect('cart:cart_view')
#
#
# # cart/views.py
# from django.shortcuts import render, redirect
# from .forms import AddToCartForm  # Import the form
# from .models import AdventurePackage, Cart
#
# def add_to_cart(request, p):
#     if request.method == 'POST':
#         form = AddToCartForm(request.POST)
#         if form.is_valid():
#             package_name = p
#             selected_date = form.cleaned_data['selected_date']
#             package = AdventurePackage.objects.get(name=package_name)
#             user = request.user
#             try:
#                 cart = Cart.objects.get(user=user, items=package, selected_date=selected_date)
#                 cart.total_persons += 1
#                 cart.save()
#             except Cart.DoesNotExist:
#                 if selected_date:
#                     cart = Cart.objects.create(items=package, user=user, total_persons=1, selected_date=selected_date)
#                     cart.save()
#                 else:
#                     error_message = "Please select a date for the package."
#                     return render(request, 'home/detailed_view.html', {'a': package, 'error_message': error_message})
#             return redirect('cart:cart_view')
#     else:
#         package = AdventurePackage.objects.get(name=p)
#         form = AddToCartForm()
#     return render(request, 'home/detailed_view.html', {'a': package, 'form': form})
#
# def cart_view(request):
#     user = request.user
#     cart = Cart.objects.filter(user=user)
#     return render(request, 'cart/cart_view.html', {'cart': cart})
#
# def cart_remove(request, p):
#     package = AdventurePackage.objects.get(name=p)
#     user = request.user
#     try:
#         cart = Cart.objects.get(user=user, items=package)
#         if cart.total_persons > 1:
#             cart.total_persons -= 1
#             cart.save()
#         else:
#             cart.delete()
#     except:
#         pass
#     return redirect('cart:cart_view')
#
# def full_remove(request, p):
#     package = AdventurePackage.objects.get(name=p)
#     user = request.user
#     try:
#         cart = Cart.objects.get(user=user, items=package)
#         cart.delete()
#     except:
#         pass
#     return redirect('cart:cart_view')


# def add_to_cart(request,p):
#     return redirect('cart:cart_view')
#
#
# def cart_view(request):
#
#     user = request.user
#     cart = Cart.objects.filter(user=user)
#     return render(request, 'cart/cart_view.html', {'cart': cart})
  # real


from django.shortcuts import render, redirect
from .models import AdventurePackage, Cart

def add_to_cart(request, p):
    if request.method == 'POST':
        package_name = p
        selected_date = request.POST.get('selected_date')
        total_persons = request.POST.get('total_persons')
        package = AdventurePackage.objects.get(name=package_name)
        user = request.user
        try:
            cart = Cart.objects.get(user=user, items=package, selected_date=selected_date)
            cart.total_persons += int(total_persons)
            cart.save()
        except Cart.DoesNotExist:
            if selected_date:
                cart = Cart.objects.create(items=package, user=user, total_persons=int(total_persons), selected_date=selected_date)
                cart.save()
            else:
                error_message = "Please select a date for the package."
                return render(request, 'your_detailed_view_template.html', {'a': package, 'error_message': error_message})
        return redirect('cart:cart_view')
    else:
        package = AdventurePackage.objects.get(name=p)
        return render(request, 'home/detailed_view.html', {'a': package})


def cart_view(request):
    user = request.user
    cart_items = Cart.objects.filter(user=user)
    total = 0
    for item in cart_items:
        item.subtotal = item.total_persons * item.items.price
        total += item.subtotal
    return render(request, 'cart/cart_view.html', {'cart_items': cart_items, 'total': total})



from django.shortcuts import render, redirect, get_object_or_404
from .models import Cart

def edit_cart_item(request, pk):
    cart_item = get_object_or_404(Cart, pk=pk)
    if request.method == 'POST':
        cart_item.total_persons = request.POST.get('total_persons')
        cart_item.selected_date = request.POST.get('selected_date')
        cart_item.save()
        return redirect('cart:cart_view')
    return render(request, 'cart/edit_cart_item.html', {'cart_item': cart_item})


from django.shortcuts import redirect, get_object_or_404
from .models import Cart,Account

def delete_cart_item(request, pk):
    cart_item = get_object_or_404(Cart, pk=pk)
    cart_item.delete()
    return redirect('cart:cart_view')



from django.shortcuts import render, redirect
from .models import Cart, Order, Account

def show_booking_form(request):
    user = request.user
    cart_items = Cart.objects.filter(user=user)
    total = 0
    for item in cart_items:
        item.subtotal = item.total_persons * item.items.price
        total += item.subtotal

    if request.method == "POST":
        address = request.POST.get('address')
        phone_number = request.POST.get('phone_number')
        account_number = request.POST.get('number')

        acct = Account.objects.get(accnumber=account_number)

        # Check if the user has enough balance to proceed with the order
        if acct.balance >= total:
            # Process the order
            for item in cart_items:
                order = Order.objects.create(
                    user=user,
                    package=item.items,
                    no_of_persons=item.total_persons,
                    address=address,
                    phone=phone_number,
                    order_status="paid",
                    selected_date=item.selected_date
                )
            # Clear the cart
            cart_items.delete()
            # Deduct the total amount from the user's account balance
            acct.balance -= total
            acct.save()
            msg = 'Order placed successfully'
            return render(request, 'cart/order_confirm.html', {'msg': msg})
        else:
            msg = "Insufficient balance. Please recharge your account."
            return render(request, 'cart/order_confirm.html', {'msg': msg})

    return render(request, 'cart/booking_form.html', {'total_amount': total})


def order_view(request):
    user = request.user
    o = Order.objects.filter(user=user)


    return render(request,'cart/order_view.html', {'o': o,'u':user.username})





