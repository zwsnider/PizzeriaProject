from django.shortcuts import render, redirect
from .models import Pizza, Topping
# Create your views here.

def index(request):
    """The home page for Pizzeria"""
    return render(request, 'pizzas/index.html')

def pizzas(request):
    pizzas = Pizza.objects.order_by('date_added')
    #build context dictionary for the template to use to access
    # the data you're looking for.
    context = {'pizzas':pizzas}
    #pass the data from context to the template for display
    return render(request, 'pizzas/pizzas.html', context)

def pizza(request, pizza_id):
    pizza = Pizza.objects.get(id=pizza_id)
    #foreign key
    toppings = pizza.topping_set.order_by('-date_added') # minus sign sets it in descending order
    context = {'pizza':pizza, 'toppings':toppings}
    
    return render(request, 'pizzas/pizza.html', context)