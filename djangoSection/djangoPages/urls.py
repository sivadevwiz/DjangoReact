from django.urls import path
from django.views.generic import RedirectView

from . import views
from djangoPages.views import home, result


urlpatterns = [
    path('', home, name='home'),  # TODO add URL redirect
    path('home', home, name='home'),
    path('result', result, name='thank_you')
]
