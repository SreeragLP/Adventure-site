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



