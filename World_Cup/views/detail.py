from django.shortcuts import render
from World_Cup.models.AllsProducts import Product
from World_Cup.models.AllProductsFootball import ProductFoot
from World_Cup.models.AllProductsNFL import ProductNFL


def detail(request, myid):
    product_objet = Product.objects.get(id=myid)
    print(product_objet)
    return render(request, 'detail.html', {'product_objet': product_objet})


def detailfoot(request, myid):
    product_objet = ProductFoot.objects.get(id=myid)
    print(product_objet)
    return render(request, 'detailfoot.html', {'product_objet': product_objet})


def detailnfl(request, myid):
    product_objet = ProductNFL.objects.get(id=myid)
    print(product_objet)
    return render(request, 'detailnfl.html', {'product_objet': product_objet})
