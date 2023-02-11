"""djangoProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from World_Cup.views.Connexion_view import LogoutView, LoginView
from World_Cup.views.Registration_view import registration_view
from World_Cup.views.compétition_view import competition_view
from World_Cup.views.competitionfoot_view import competitionfoot_view
from World_Cup.views.checkout import checkout
from World_Cup.views.detail import detail, detailfoot, detailnfl
from World_Cup.views.index_view import index
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
from World_Cup.views.competitionnfl_view import competitionnfl_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('Registration/', registration_view, name='registration'),
    path('Competition/', competition_view, name='competition'),
    path('Competition/<int:myid>', detail, name='detail'),
    path('Competitionfootball/', competitionfoot_view, name='competitionfootball'),
    path('Competitionfootball/<int:myid>', detailfoot, name='detail'),
    path('Competitionnfl/', competitionnfl_view, name='competitionnfl'),
    path('Competitionnfl/<int:myid>', detailnfl, name='detail'),
    path('Connexion/', LogoutView.as_view(), name='connexion'),
    path('Deconnexion/', LoginView.as_view(), name='login'),
    path('message/', login_required(TemplateView.as_view(template_name='connect.html')), name='message'),
    path('checkout/', checkout, name='checkout'),
]

urlpatterns += staticfiles_urlpatterns()
