from django.shortcuts import render

from django.http import HttpResponse

# Create your views here.


def home(request):
    return render(request, 'home.html')


def result(request):
    return render(request, "thankyou.html")


def handler404(request, exception):
    context = {}
    response = render(request, "custom_404.html", context=context)
    response.status_code = 400
    return response


def handler500(request, exception=None):
    context = {}
    response = render(request, "custom_500.html", context=context)
    response.status_code = 500
    return response
