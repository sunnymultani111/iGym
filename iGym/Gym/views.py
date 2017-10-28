from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views import generic
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy

from .models import Trainee



@login_required(login_url='/Account/login/')
def index(request):
    return render(request, 'Gym/index.html', {'message': "Welcome back"})


class TraineeCreate(CreateView):
    model = Trainee
    fields = ['name', 'address', 'city', 'state', 'zip_code']


class TraineeUpdate(UpdateView):
    model = Trainee
    fields = ['name', 'address', 'city', 'state', 'zip_code']


class DetailView(generic.DetailView):
    model = Trainee
    template_name = 'Gym/detail.html'


class TraineeDelete(DeleteView):
    model = Trainee
    success_url = reverse_lazy('Gym:index')
