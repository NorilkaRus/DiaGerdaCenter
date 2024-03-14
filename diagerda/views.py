from django.shortcuts import render
from django.http import HttpResponse
from .models import User
from django.contrib.auth import get_user
from django.template import loader
from .models import *
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from .forms import AppointmentForm
from django.urls import reverse_lazy

# Create your views here.
def index(request):
    return render(request, 'diagerda/index.html')

def about(request):
    return render(request, 'diagerda/about.html')

class DoctorsListView(ListView):
    model = Doctor
    template_name = 'diagerda/doctors.html'

    def get_context(self):
        context_data = get_category_cache()
        return context_data

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset


class AppointmentListView(ListView):
    model = Appointment
    template_name = 'diagerda/appointments.html'

    def get_context(self):
        context_data = get_category_cache()
        return context_data

    def get_queryset(self):
        queryset = super().get_queryset().filter(user=None)
        return queryset


class AppointmentUpdateView(UpdateView):
    pass
#     model = Appointment
#     form_class = AppointmentForm
#     success_url = reverse_lazy('diagerda:index')
#     user = request.user
#
#     def __init__(self):
#         self.object.user = self.request.user


