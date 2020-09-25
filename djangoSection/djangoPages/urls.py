from django.urls import path
from django.views.generic import RedirectView

from . import views
from djangoPages.views import home


urlpatterns = [
    path('', home, name='home'),  # TODO add URL redirect
    path('home', home, name='home')
]
