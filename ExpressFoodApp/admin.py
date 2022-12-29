from django.contrib import admin
from .models import Category, Meal, Commande

# Register your models here.
admin.site.register(Meal)
admin.site.register(Category)
admin.site.register(Commande)

#class AdminCategory (admin.ModelAdmin):
 #   list_display = ('name')
#admin.site.register(AdminCategory)
