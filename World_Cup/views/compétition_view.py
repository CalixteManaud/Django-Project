from django.shortcuts import render
from World_Cup.models.AllsProducts import Product
from django.core.paginator import Paginator


def competition_view(request):
    product_objet = Product.objects.all()
    item_name = request.GET.get('item-name')
    print(product_objet)
    if item_name != '' and item_name is not None:
        product_objet = Product.objects.filter(titre__icontains=item_name)
    paginator = Paginator(product_objet, 8)
    page = request.GET.get('page')
    product_objet = paginator.get_page(page)

    return render(request, 'competition.html', {'product_objet': product_objet})

