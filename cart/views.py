from django.shortcuts import render, redirect, get_object_or_404
from .models import AdventurePackage, Cart,Order, Account
from django.contrib.auth.decorators import login_required
from django.template.loader import render_to_string
from django.http import HttpResponse
from django.core.mail import EmailMessage
from io import BytesIO
from xhtml2pdf import pisa


def add_to_cart(request, p):
    if request.user.is_authenticated:

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
                    # return render(request, 'your_detailed_view_template.html', {'a': package, 'error_message': error_message})
            return redirect('cart:cart_view')
        else:
            package = AdventurePackage.objects.get(name=p)
            return render(request, 'home/detailed_view.html', {'a': package})
    else:
        return redirect('UserAuthentication:login')



def cart_view(request):
    if request.user.is_authenticated:

        user = request.user
        cart_items = Cart.objects.filter(user=user)
        total = 0
        for item in cart_items:
            item.subtotal = item.total_persons * item.items.price
            total += item.subtotal
        return render(request, 'cart/cart_view.html', {'cart_items': cart_items, 'total': total})

    else:
        return redirect('UserAuthentication:login')




@login_required()
def edit_cart_item(request, pk):
    cart_item = get_object_or_404(Cart, pk=pk)
    if request.method == 'POST':
        cart_item.total_persons = request.POST.get('total_persons')
        cart_item.selected_date = request.POST.get('selected_date')
        cart_item.save()
        return redirect('cart:cart_view')
    return render(request, 'cart/edit_cart_item.html', {'cart_item': cart_item})



def delete_cart_item(request, pk):
    cart_item = get_object_or_404(Cart, pk=pk)
    cart_item.delete()
    return redirect('cart:cart_view')




#OG

# def show_booking_form(request):
#     user = request.user
#     cart_items = Cart.objects.filter(user=user)
#     total = 0
#     for item in cart_items:
#         item.subtotal = item.total_persons * item.items.price
#         total += item.subtotal
#
#     if request.method == "POST":
#         address = request.POST.get('address')
#         phone_number = request.POST.get('phone_number')
#         account_number = request.POST.get('number')
#
#         acct = Account.objects.get(accnumber=account_number)
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
#             # Send receipt email
#             send_receipt_email(request, order)
#
#             msg = 'Order placed successfully'
#             return render(request, 'cart/order_confirm.html', {'msg': msg})
#         else:
#             msg = "Insufficient balance. Please recharge your account."
#             return render(request, 'cart/order_confirm.html', {'msg': msg})
#
#     return render(request, 'cart/booking_form.html', {'total_amount': total})




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
#         acct = Account.objects.get(accnumber=account_number)
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
#             # Send receipt email
#             send_receipt_email(request, order)
#
#             msg = 'Order placed successfully'
#             return render(request, 'cart/order_confirm.html', {'msg': msg})
#         else:
#             msg = "Insufficient balance. Please recharge your account."
#             return render(request, 'cart/order_confirm.html', {'msg': msg})
#
#     return render(request, 'cart/booking_form.html', {'total_amount': total})
#
#

def show_booking_form(request):
    user = request.user
    cart_items = Cart.objects.filter(user=user)
    total = 0
    order = None  # Initialize order variable

    for item in cart_items:
        item.subtotal = item.total_persons * item.items.price
        total += item.subtotal

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

            # Send receipt email
            send_receipt_email(request, order)

            msg = 'Booking successfully placed'
            return render(request, 'cart/order_confirm.html', {'msg': msg})
        else:
            msg = "Insufficient balance. Please recharge your account."
            return render(request, 'cart/order_confirm.html', {'msg': msg})

    return render(request, 'cart/booking_form.html', {'total_amount': total})





#workin
def send_receipt_email(request, latest_order):
    user = request.user

    # Render the HTML template with order details
    context = {'o': [latest_order], 'u': user.username}
    html_content = render_to_string('cart/receipt_template.html', context)

    # Create a PDF file
    result = BytesIO()
    pdf = pisa.pisaDocument(BytesIO(html_content.encode("UTF-8")), result)

    if not pdf.err:
        # PDF creation successful, attach it to the email
        email = EmailMessage(
            subject='Your Order Details',
            body='Please find attached your order details.',
            to=[user.email],
        )
        email.attach('order_details.pdf', result.getvalue(), 'application/pdf')
        email.send()

        return HttpResponse("Order details sent successfully")
    else:
        # PDF creation failed
        return HttpResponse("Error creating PDF: {}".format(pdf.err))




def order_view(request):
    user = request.user
    o = Order.objects.filter(user=user)
    return render(request,'cart/order_view.html', {'o': o,'u':user.username})





