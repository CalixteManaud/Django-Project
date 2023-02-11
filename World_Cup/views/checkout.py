from django.shortcuts import redirect, render
from World_Cup.models.AllsProducts import Commande


def checkout(request):
    if request.method == "POST":
        items = request.POST.get('items')
        total = request.POST.get('total')
        nom = request.POST.get('nom')
        email = request.POST.get('email')
        address = request.POST.get('address')
        ville = request.POST.get('ville')
        pays = request.POST.get('pays')
        zipcode = request.POST.get('zipcode')
        com = Commande(items=items, total=total, nom=nom, email=email, address=address, ville=ville, pays=pays,
                       zipcode=zipcode)
        com.save()
        return redirect('confirmation')

    return render(request, 'checkout.html')


