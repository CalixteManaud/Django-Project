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

from World_Cup.views.Registration_view import LogoutView, LoginView, RegistrationView
from World_Cup.views.compétition_view import CompetitionView
from World_Cup.views.competitionfoot_view import CompetitionFootView
from World_Cup.views.checkout import CheckoutView
from World_Cup.views.detail import DetailViewProduct, DetailViewProductFoot, DetailViewProductNFL
from World_Cup.views.index_view import IndexView
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from World_Cup.views.competitionnfl_view import CompetitionNFLView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', IndexView.as_view(), name='index'),
    path('Registration/', RegistrationView.as_view(), name='registration'),
    path('Competition', CompetitionView.as_view(), name='competition'),
    path('Competition/<int:pk>', DetailViewProduct.as_view(), name='detail_product'),
    path('Competitionfootball', CompetitionFootView.as_view(), name='competitionfootball'),
    path('Competitionfootball/<int:pk>', DetailViewProductFoot.as_view(), name='detail_foot'),
    path('Competitionnfl/', CompetitionNFLView.as_view(), name='competitionnfl'),
    path('Competitionnfl/<int:pk>', DetailViewProductNFL.as_view(), name='detail_nfl'),
    path('checkout/', CheckoutView, name='checkout'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
]

urlpatterns += staticfiles_urlpatterns()
