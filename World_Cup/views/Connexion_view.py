from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.http import *
from django.views.generic import TemplateView
from django.conf import settings


class LoginView(TemplateView):
    template_name = 'connexion.html'

    def post(self, request, **kwargs):
        username = request.POST.get('username', False)
        password = request.POST.get('password', False)
        user = authenticate(request, username=username, password=password)
        if user is not None and user.is_active:
            login(request, user)
            return redirect('/home')
        else:
            return HttpResponse("Email or password is incorrect")


class LogoutView(TemplateView):
    template_name = 'connexion.html'

    def get(self, request, **kwargs):
        logout(request)
        return render(request, self.template_name, {'error': 'You have been logged out'})
