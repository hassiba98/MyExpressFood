from django.shortcuts import render
from .models import Meal
# Create your views here.
from django.http import HttpResponse

# Create your views here.
def index(request):
    meal_object = Meal.objects.all()
    return render(request, 'expressFoodTemplates/index.html',{'meal_object': meal_object})

