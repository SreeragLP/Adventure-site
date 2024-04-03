from django.shortcuts import render, redirect, get_object_or_404
from .models import AdventurePackage, Cart, Order, Account
from django.contrib.auth.decorators import login_required
import qrcode
from django.core.mail import EmailMessage
from io import BytesIO

from datetime import datetime, timedelta


# def add_to_cart(request, p):
#     if request.user.is_authenticated:
#
#         if request.method == 'POST':
#             package_name = p
#             selected_date = request.POST.get('selected_date')
#             total_persons = request.POST.get('total_persons')
#             package = AdventurePackage.objects.get(name=package_name)
#             user = request.user
#             try:
#                 cart = Cart.objects.get(user=user, items=package, selected_date=selected_date)
#                 cart.total_persons += int(total_persons)
#                 cart.save()
#             except Cart.DoesNotExist:
#                 if selected_date:
#                     cart = Cart.objects.create(items=package, user=user, total_persons=int(total_persons), selected_date=selected_date)
#                     cart.save()
#                 else:
#                     error_message = "Please select a date for the package."
#                     # return render(request, 'your_detailed_view_template.html', {'a': package, 'error_message': error_message})
#             return redirect('cart:cart_view')
#         else:
#             package = AdventurePackage.objects.get(name=p)
#             return render(request, 'home/detailed_view.html', {'a': package})
#     else:
#         return redirect('UserAuthentication:login')

def add_to_cart(request, p):
    if request.user.is_authenticated:
        if request.method == 'POST':
            package_name = p
            selected_date = request.POST.get('selected_date')
            total_persons = int(request.POST.get('total_persons'))
            include_food_and_accommodation = request.POST.get('include_food_and_accommodation') == 'on'
            package = AdventurePackage.objects.get(name=package_name)

            # Calculate accommodation amount per person
            accommodation_amount_per_person = package.accommodation_price_per_person

            user = request.user
            try:
                cart = Cart.objects.get(user=user, items=package, selected_date=selected_date)
                cart.total_persons += total_persons
                cart.include_food_and_accommodation = include_food_and_accommodation
                cart.accommodation_amount_per_person = accommodation_amount_per_person  # Set the accommodation amount per person
                cart.save()
            except Cart.DoesNotExist:
                cart = Cart.objects.create(
                    items=package,
                    user=user,
                    total_persons=total_persons,
                    selected_date=selected_date,
                    include_food_and_accommodation=include_food_and_accommodation,
                    accommodation_amount_per_person=accommodation_amount_per_person  # Set the accommodation amount per person
                )
            return redirect('cart:cart_view')
        else:
            package = AdventurePackage.objects.get(name=p)
            return render(request, 'home/detailed_view.html', {'a': package})
    else:
        return redirect('UserAuthentication:login')



# def cart_view(request):
#     if request.user.is_authenticated:
#
#         user = request.user
#         cart_items = Cart.objects.filter(user=user)
#         total = 0
#         for item in cart_items:
#             item.subtotal = item.total_persons * item.items.price
#             total += item.subtotal
#         return render(request, 'cart/cart_view.html', {'cart_items': cart_items, 'total': total})
#
#     else:
#         return redirect('UserAuthentication:login')



def cart_view(request):
    if request.user.is_authenticated:
        user = request.user
        cart_items = Cart.objects.filter(user=user)
        total = 0
        for item in cart_items:
            item.subtotal = item.total_persons * item.items.price
            if item.include_food_and_accommodation and item.items.accommodation_price_per_person is not None:
                item.subtotal += item.total_persons * item.items.accommodation_price_per_person
            total += item.subtotal
        return render(request, 'cart/cart_view.html', {'cart_items': cart_items, 'total': total})
    else:
        return redirect('UserAuthentication:login')






@login_required()
def edit_cart_item(request, pk):
    # Calculate the maximum date (90 days from today)
    max_date = (datetime.today() + timedelta(days=90)).strftime('%Y-%m-%d')
    cart_item = get_object_or_404(Cart, pk=pk)
    if request.method == 'POST':
        cart_item.total_persons = request.POST.get('total_persons')
        cart_item.selected_date = request.POST.get('selected_date')
        cart_item.save()
        return redirect('cart:cart_view')
    return render(request, 'cart/edit_cart_item.html', {'cart_item': cart_item,'max_date': max_date})



def delete_cart_item(request, pk):
    cart_item = get_object_or_404(Cart, pk=pk)
    cart_item.delete()
    return redirect('cart:cart_view')



# def show_booking_form(request):
#     user = request.user
#     cart_items = Cart.objects.filter(user=user)
#     total = 0
#     order = None  # Initialize order variable
#
#     for item in cart_items:
#         item.subtotal = item.total_persons * item.items.price
#         total += item.subtotal
#
#     if request.method == "POST":
#         address = request.POST.get('address')
#         phone_number = request.POST.get('phone_number')
#         account_number = request.POST.get('number')
#
#         try:
#             # Attempt to retrieve the account information
#             acct = Account.objects.get(accnumber=account_number)
#         except Account.DoesNotExist:
#             # If the account doesn't exist, return an error message
#             msg = "Account does not exist. Please enter a valid account number."
#             return render(request, 'cart/order_confirm.html', {'msg': msg})
#
#         # Check if the user has enough balance to proceed with the order
#         if acct.balance >= total:
#             # Process the order
#             for item in cart_items:
#                 order = Order.objects.create(
#                     user=user,
#                     package=item.items,
#                     no_of_persons=item.total_persons,
#                     address=address,
#                     phone=phone_number,
#                     order_status="paid",
#                     selected_date=item.selected_date
#                 )
#             # Clear the cart
#             cart_items.delete()
#             # Deduct the total amount from the user's account balance
#             acct.balance -= total
#             acct.save()
#
#             # Generate QR code
#             qr = qrcode.QRCode(
#                 version=2,
#                 error_correction=qrcode.constants.ERROR_CORRECT_L,
#                 box_size=20,
#                 border=4,
#             )
#             qr.add_data(str(order.id))  # Use order ID as the QR code data
#             qr.make(fit=True)
#             qr_image = qr.make_image(fill_color="black", back_color="white")
#
#             # Convert QR code image to bytes
#             img_buffer = BytesIO()
#             qr_image.save(img_buffer, format='PNG')
#             img_buffer.seek(0)
#
#             # Send email with QR code attachment
#             email_body = f"Hello {user.username},\n\n"
#             email_body += "Thank you for your booking. Attached is your booking QR code.\n\n"
#             email_body += "Please do not share your QR code with anybody.\n\n"
#             email_body += "This is your ticket.\n"
#
#             email = EmailMessage(
#                 subject='Your Booking QR Code',
#                 body=email_body,
#                 to=[user.email],
#             )
#             email.attach('booking_qr_code.png', img_buffer.getvalue(), 'image/png')
#             email.send()
#
#             msg = 'Booking successfully placed'
#             return render(request, 'cart/order_confirm.html', {'msg': msg})
#         else:
#             msg = "Insufficient balance. Please recharge your account."
#             return render(request, 'cart/order_confirm.html', {'msg': msg})
#
#     return render(request, 'cart/booking_form.html', {'total_amount': total})


def show_booking_form(request):
    user = request.user
    cart_items = Cart.objects.filter(user=user)
    total = 0  # Initialize total variable

    # Calculate total sum of items in the cart
    for item in cart_items:
        subtotal = item.total_persons * item.items.price
        if item.include_food_and_accommodation and item.items.accommodation_price_per_person:
            subtotal += item.items.accommodation_price_per_person * item.total_persons
        total += subtotal

    if request.method == "POST":
        address = request.POST.get('address')
        phone_number = request.POST.get('phone_number')
        account_number = request.POST.get('number')

        try:
            # Attempt to retrieve the account information
            acct = Account.objects.get(accnumber=account_number)
        except Account.DoesNotExist:
            # If the account doesn't exist, return an error message
            msg = "Account does not exist. Please enter a valid account number."
            return render(request, 'cart/order_confirm.html', {'msg': msg})

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

            # Generate QR code
            qr = qrcode.QRCode(
                version=2,
                error_correction=qrcode.constants.ERROR_CORRECT_L,
                box_size=20,
                border=4,
            )
            qr.add_data(str(order.id))  # Use order ID as the QR code data
            qr.make(fit=True)
            qr_image = qr.make_image(fill_color="black", back_color="white")

            # Convert QR code image to bytes
            img_buffer = BytesIO()
            qr_image.save(img_buffer, format='PNG')
            img_buffer.seek(0)

            # Send email with QR code attachment
            email_body = f"Hello {user.username},\n\n"
            email_body += "Thank you for your booking. Attached is your booking QR code.\n\n"
            email_body += "Please do not share your QR code with anybody.\n\n"
            email_body += "This is your ticket.\n"

            email = EmailMessage(
                subject='Your Booking QR Code',
                body=email_body,
                to=[user.email],
            )
            email.attach('booking_qr_code.png', img_buffer.getvalue(), 'image/png')
            email.send()

            msg = 'Booking successfully placed'
            return render(request, 'cart/order_confirm.html', {'msg': msg})
        else:
            msg = "Insufficient balance. Please recharge your account."
            return render(request, 'cart/order_confirm.html', {'msg': msg})

    return render(request, 'cart/booking_form.html', {'total_amount': total})



def order_view(request):
    user = request.user
    o = Order.objects.filter(user=user)
    return render(request,'cart/order_view.html', {'o': o,'u':user.username})



def delete_order_view(request, pk):
    order_view = get_object_or_404(Order, pk=pk)
    order_view.delete()
    return redirect('cart:refund')


def refund(request):
    return render(request,'cart/refund.html')