# HealthHub_BE/views.py

from django.http import HttpResponse

def root_route(request):
    return HttpResponse("Welcome to the HealthHub!")
