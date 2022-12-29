from django.shortcuts import render
from .models import Meal
from django.core.paginator import Paginator
# Create your views here.
from django.http import HttpResponse

# Create your views here.
def index(request):
    meal_object = Meal.objects.all()
    item_name =  request.GET.get('item-name')
    if item_name !='' and item_name is not None:
        meal_object = Meal.objects.filter(title__icontains=item_name)
    paginator = Paginator(meal_object, 8)
    page = request.GET.get('page')
    meal_object = paginator.get_page(page)
    return render(request, 'expressFoodTemplates/index.html',{'meal_object': meal_object})


def detail(request, myid):
    meal_object = Meal.objects.get(id=myid)
    return render(request, 'expressFoodTemplates/detail.html', {'meal_object': meal_object})

def checkout(request):
    return render(request, 'expressFoodTemplates/checkout.html')
