# from django.contrib.auth.decorators import login_required
# from cart.models import Order
#
# def menu_links(request):
#     user = request.user
#     if user.is_authenticated:
#         # Retrieve notifications for the logged-in user
#         links = Order.objects.filter(user=user)
#     else:
#         # If the user is not authenticated, set links to an empty queryset
#         links = Order.objects.none()
#     return {'links': links}
#


# from cart.models import Order
# from app1.models import Rating  # Import your Rating model
#
# def menu_links(request):
#     user = request.user
#     if user.is_authenticated:
#         # Retrieve notifications for the logged-in user
#         orders = Order.objects.filter(user=user)
#         user_has_rated = set(Rating.objects.filter(user=user, has_rated=True).values_list('package__id', flat=True))
#         for order in orders:
#             order.user_has_rated = order.package_id in user_has_rated
#     else:
#         # If the user is not authenticated, set orders to an empty queryset
#         orders = Order.objects.none()
#     return {'orders': orders}



from cart.models import Order
from app1.models import Rating

def menu_links(request):
    user = request.user
    context = {}

    if user.is_authenticated:
        # Retrieve notifications for the logged-in user
        orders = Order.objects.filter(user=user)
        user_has_rated = set(Rating.objects.filter(user=user, has_rated=True).values_list('package__id', flat=True))
        for order in orders:
            order.user_has_rated = order.package_id in user_has_rated
        context['orders'] = orders

        # Add rating information to the context
        user_ratings = Rating.objects.filter(user=user)
        context['user_ratings'] = user_ratings

    return context



# cart/context_processors.py

# cart/context_processors.py

# from cart.models import Order
#
# def menu_links(request):
#     user = request.user
#     context = {}
#
#     if user.is_authenticated:
#         # Retrieve orders for the logged-in user
#         orders = Order.objects.filter(user=user)
#
#         # Calculate subtotal for each order dynamically
#         for order in orders:
#             try:
#                 subtotal = order.no_of_persons * order.package.food_and_accommodation_price_per_person
#             except AttributeError:
#                 # Handle case where the attribute doesn't exist
#                 subtotal = order.no_of_persons * order.package.price
#
#             # Assign the calculated subtotal to the order object
#             order.subtotal = subtotal
#
#         # Add orders to the context
#         context['orders'] = orders
#
#     return context
#



# from cart.models import Order
# from app1.models import Rating
#
# def menu_links(request):
#     user = request.user
#     context = {}
#
#     if user.is_authenticated:
#         # Retrieve orders for the logged-in user
#         orders = Order.objects.filter(user=user)
#
#         # Calculate subtotal for each order dynamically and check if the user has rated the package
#         for order in orders:
#             try:
#                 subtotal = order.no_of_persons * order.package.food_and_accommodation_price_per_person
#             except AttributeError:
#                 # Handle case where the attribute doesn't exist
#                 subtotal = order.no_of_persons * order.package.price
#
#             # Assign the calculated subtotal to the order object
#             order.subtotal = subtotal
#
#             # Check if the user has rated the package
#             order.user_has_rated = Rating.objects.filter(user=user, package=order.package, has_rated=True).exists()
#
#         # Add orders to the context
#         context['orders'] = orders
#
#         # Retrieve rating information for the logged-in user
#         user_ratings = Rating.objects.filter(user=user)
#         context['user_ratings'] = user_ratings
#
#     return context
