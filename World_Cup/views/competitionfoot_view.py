from django.shortcuts import render
from World_Cup.models.AllProductsFootball import ProductFoot
from django.core.paginator import Paginator


def competitionfoot_view(request):
    product_objet = ProductFoot.objects.all()
    item_name = request.GET.get('item-name')
    if item_name != '' and item_name is not None:
        product_objet = ProductFoot.objects.filter(titre__icontains=item_name)
    paginator = Paginator(product_objet, 8)
    page = request.GET.get('page')
    product_objet = paginator.get_page(page)

    return render(request, 'competitionfoot.html', {'product_objet': product_objet})