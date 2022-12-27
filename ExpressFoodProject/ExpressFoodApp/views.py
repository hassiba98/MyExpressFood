from django.shortcuts import render
from .models import Meal
# Create your views here.
from django.http import HttpResponse

# Create your views here.
def index(request):
    meal_object = Meal.objects.all()
    item_name =  request.GET.get('item-name')
    if item_name !='' and item_name is not None:
        meal_object = Meal.objects.filter(title__icontains=item_name)
    return render(request, 'expressFoodTemplates/index.html',{'meal_object': meal_object})

