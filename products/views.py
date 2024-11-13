from django.shortcuts import render, redirect
from .models import Product

def Home(request):
    product = Product.objects.all()
    return render(request, 'home.html', {'product': product})


def Form(request):
    return render(request, 'form.html')

def Create(request):
    name = request.POST.get('name')
    price = request.POST.get('price')
    durability = request.POST.get('durability')
    description = request.POST.get('description')

    product = Product.objects.create(
        name = name,
        price = price,
        durability = durability,
        description = description
    )
    return render(request, 'form.html', {'product': product})


def Edit(request, id):
    product = Product.objects.get(id=id)
    return render(request, 'update.html', {'product': product})

def Update(request, id):
    product = Product.objects.get(id=id)
    name = request.POST.get('name')
    price = request.POST.get('price')
    description = request.POST.get('description')
    durability = request.POST.get('durability')

    product.name = name
    product.price = price
    product.description = description
    product.durability = durability
    product.save()
    return redirect('home')

def Delete(request, id):
    try:
        product = Product.objects.get(id=id)
        product.delete()
    except: 
        return print('Object not found.')

    return redirect('home')