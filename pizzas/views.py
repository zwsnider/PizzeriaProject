from django.shortcuts import render, redirect
from .models import Pizza, Topping
from .forms import CommentForm
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

def comment(request, pizza_id):
    pizza = Pizza.objects.get(id=pizza_id)
    if request.method != 'POST':
        form = CommentForm()
    else:
        form = CommentForm(data=request.POST)
        
        if form.is_valid():
            #save data but don't commit
            comment = form.save(commit=False)
            #assign pizza that is being commented on
            comment.pizza = pizza
            comment.save()
            form.save()
            return redirect('pizzas:pizza',pizza_id=pizza_id)
    
    context = {'form': form, 'pizza':pizza}
    return render(request, 'pizzas/comment.html', context)