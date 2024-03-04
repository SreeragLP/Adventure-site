from django.contrib.auth.decorators import login_required
from cart.models import Order

def menu_links(request):
    user = request.user
    if user.is_authenticated:
        # Retrieve notifications for the logged-in user
        links = Order.objects.filter(user=user)
    else:
        # If the user is not authenticated, set links to an empty queryset
        links = Order.objects.none()
    return {'links': links}

