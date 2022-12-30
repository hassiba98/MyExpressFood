from django.urls import path

from . import views

urlpatterns = [path('',views.index,name='home'),
               path('<int:myid>', views.detail, name="detail"),
               path('checkout', views.checkout, name="checkout"),
               path('confirmation', views.confirmation, name="confirmation")
               ]