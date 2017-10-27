from django.shortcuts import render
from django.http import request

from django.contrib.auth.decorators import login_required

@login_required(login_url='/Account/login/')
def index(request):
    return render(request, 'Gym/index.html', {'message': "Welcome back"})
