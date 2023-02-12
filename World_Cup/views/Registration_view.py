from django.shortcuts import render, redirect
from World_Cup.models.register import NewUser
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.views import View


class RegistrationView(View):
    def get(self, request):
        form = NewUser()
        return render(request, 'registration.html', {'form': form})

    def post(self, request):
        form = NewUser(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Inscription réussie")
            return redirect('index')
        messages.error(request, "Inscription échouée")
        return render(request, 'registration.html', {'form': form})


class LoginView(View):
    template_name = 'connexion.html'

    def get(self, request, *args, **kwargs):
        form = AuthenticationForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}.")
                return redirect("index")
            else:
                messages.error(request, "Invalid username or password.")
            return redirect('main::index')
        else:
            messages.error(request, "Invalid username or password.")
        return render(request, self.template_name, {'form': form})


class LogoutView(View):
    def get(self, request, *args, **kwargs):
        logout(request)
        messages.info(request, "You have successfully logged out.")
        return redirect("index")
