from django.shortcuts import render
from .models import Meal, Commande
from django.core.paginator import Paginator
# Create your views here.


# Create your views here.
def index(request):
    meal_object = Meal.objects.all()
    item_name = request.GET.get('item-name')
    if item_name != '' and item_name is not None:
        meal_object = Meal.objects.filter(title__icontains=item_name)
    paginator = Paginator(meal_object, 8)
    page = request.GET.get('page')
    meal_object = paginator.get_page(page)
    return render(request, 'expressFoodTemplates/index.html', {'meal_object': meal_object})


def detail(request, myid):
    meal_object = Meal.objects.get(id=myid)
    return render(request, 'expressFoodTemplates/detail.html', {'meal_object': meal_object})


def checkout(request):
    if request.method == "POST":
        nom = request.POST.get('nom')
        prenom = request.POST.get('prenom')
        email = request.POST.get('email')
        adress = request.POST.get('adress')
        ville = request.POST.get('ville')
        pays = request.POST.get('pays')
        zipcode = request.POST.get('zipcode')
        com = Commande(nom=nom, prenom=prenom, email=email, adress=adress, ville=ville, pays=pays, zipcode=zipcode)
        com.save()

    return render(request, 'expressFoodTemplates/checkout.html')
