#path function to map URLs to views
from django.urls import path

#import views from same directory as urls.py (app directory)
from . import views

#app name to distinguish URLs
app_name = 'pizzas'

#Build out URLs to individual pages
urlpatterns = [
    #Empty string represents home page, 2nd arg gives the function
    # to call from views.py, 3rd arg gives the URL its name
    path('', views.index, name='index'),
    path('pizzas', views.pizzas, name='pizzas'),
    path('pizzas/<int:pizza_id>/', views.pizza, name='pizza'),
]
