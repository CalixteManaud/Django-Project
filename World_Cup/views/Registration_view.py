from django.shortcuts import render, redirect
from World_Cup.models.Registration import Registration


def registration_view(request):
    if request.method == 'POST':
        form = Registration(request.POST)
        if form.is_valid():
            name = request.POST.get('name')
            email = request.POST.get('email')
            password = request.POST.get('password')
            date_of_birth = request.POST.get('date_of_birth')
            competition_category = request.POST.get('competition_category')
            data = Registration(name=name, email=email, password=password, date_of_birth=date_of_birth,
                                competition_category=competition_category)
            data.save()
            return redirect('/login')
    else:
        form = Registration()
    return render(request, 'registration.html', {'form': form})

