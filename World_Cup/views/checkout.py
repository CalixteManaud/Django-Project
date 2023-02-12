from django.shortcuts import redirect, render
from World_Cup.models.AllsProducts import Commande


class CheckoutView:
    def __init__(self, request):
        self.request = request

    def handle_request(self):
        if self.request.method == "POST":
            items = self.request.POST.get('items')
            total = self.request.POST.get('total')
            nom = self.request.POST.get('nom')
            email = self.request.POST.get('email')
            address = self.request.POST.get('address')
            ville = self.request.POST.get('ville')
            pays = self.request.POST.get('pays')
            zipcode = self.request.POST.get('zipcode')
            com = Commande(items=items, total=total, nom=nom, email=email, address=address, ville=ville, pays=pays,
                           zipcode=zipcode)
            com.save()
            return redirect('confirmation')

        return render(self.request, 'checkout.html')
