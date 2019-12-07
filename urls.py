from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name="index" ),

    path('about/',views.about,name="about"),
    path('check/',views.checkout,name="checkout"),
    path('contact/',views.contact,name="contact"),
    path('search/',views.search,name="search"),
    path('prodv/',views.productview,name="productview"),

]