from django.shortcuts import render
from World_Cup.models.AllsProducts import Product
from World_Cup.models.AllProductsFootball import ProductFoot
from World_Cup.models.AllProductsNFL import ProductNFL
from django.views.generic import DetailView


class DetailViewProduct(DetailView):
    model = Product
    template_name = 'detail.html'


class DetailViewProductFoot(DetailView):
    model = ProductFoot
    template_name = 'detailfoot.html'


class DetailViewProductNFL(DetailView):
    model = ProductNFL
    template_name = 'detailnfl.html'

