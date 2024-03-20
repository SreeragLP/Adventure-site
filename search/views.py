from django.shortcuts import render
from app1.models import AdventurePackage
from django.db.models import Q


# Create your views here.
def searchresult(request):
    query = ""
    packages=None
    if (request.method=="POST"):
        query=request.POST['q']
        if query:
            packages=AdventurePackage.objects.filter(Q(name__icontains=query) | Q(description__icontains=query))

    return render(request,'search/search.html',{'p':packages,'q':query})



def price_range(request):
    if request.method == "POST":
        max_price = request.POST.get('q', '')
        if max_price:
            packages = AdventurePackage.objects.filter(price__lte=max_price)
            return render(request, 'search/search.html', {'p': packages, 'q': '', 'max_price': max_price})
    return render(request, 'search/search.html')