from django.shortcuts import render
from django.http import HttpResponse
from .models import User
from django.contrib.auth import get_user
from django.template import loader
from .models import *
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from .forms import AppointmentForm
from django.urls import reverse_lazy
from django.forms import inlineformset_factory
from datetime import datetime
from django.views.generic.base import View
from django.shortcuts import redirect, get_object_or_404

# Create your views here.
def index(request):
    return render(request, 'diagerda/index.html')

def about(request):
    if request.method=="POST":
        print(request.POST.get('review_name'))
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
    """"Показ списка всех записей на диагностику"""
    model = Appointment
    template_name = 'diagerda/appointments.html'

    def get_context(self):
        context_data = get_category_cache()
        return context_data

    def get_queryset(self):
        user = self.request.user
        current_datetime = datetime.now()

        if user.is_authenticated:  # для зарегистрированных пользователей
            if user.is_staff or user.is_superuser:  # для работников и суперпользователя
                queryset = super().get_queryset().order_by('diagnostic')
            else:  # для остальных пользователей
                queryset = super().get_queryset().filter(user=None, date__gte = current_datetime).order_by('diagnostic')
        else:  # для незарегистрированных пользователей
            queryset = None
        return queryset


class AppointmentUserListView(ListView):
    """"Показ списка забронированных пользователем записей на диагностику"""
    model = Appointment
    template_name = 'diagerda/user_appointments.html'

    def get_context(self):
        context_data = get_category_cache()
        return context_data

    def get_queryset(self):
        user = self.request.user
        current_datetime = datetime.now()

        if user.is_authenticated:  # для зарегистрированных пользователей
            queryset = super().get_queryset().filter(user=user, date__gte = current_datetime).order_by('date')
        else:  # для незарегистрированных пользователей
            queryset = None
        return queryset


class AppointmentArchiveListView(ListView):
    """"Показ списка прошедших записей на диагностику"""
    model = Appointment
    template_name = 'diagerda/appointments_archive.html'

    def get_context(self):
        context_data = get_category_cache()
        return context_data

    def get_queryset(self):
        user = self.request.user
        current_datetime = datetime.now()

        if user.is_authenticated:  # для зарегистрированных пользователей
            queryset = super().get_queryset().filter(user=user, date__lt = current_datetime).order_by('-date')
        else:  # для незарегистрированных пользователей
            queryset = None
        return queryset


class AppointmentAddView(View):
    """"Запись пациента на диагностику"""
    success_url = reverse_lazy('diagerda:user_appointments')

    def post(self, request, pk, *args, **kwargs):
        appointment = get_object_or_404(Appointment, pk=pk)
        appointment.user = request.user
        appointment.save()
        return redirect(self.success_url)


class AppointmentCancelView(View):
    """"Отмена записи на прием"""
    success_url = reverse_lazy('diagerda:user_appointments')

    def post(self, request, pk, *args, **kwargs):
        appointment = get_object_or_404(Appointment, pk=pk)
        appointment.user = None
        appointment.save()
        return redirect(self.success_url)


class SpecialityListView(ListView):
    """"Показ списка всех специализаций"""
    model = Speciality
    template_name = 'diagerda/index.html'

    def get_context(self):
        context_data = get_category_cache()
        return context_data

    def get_queryset(self):
        queryset = super().get_queryset().order_by('title')
        return queryset


class SpecialityDetailView(DetailView):
    model = Speciality

    def get(self, request, pk):
        speciality = Speciality.objects.get(id=pk)
        doctor = Doctor.objects.filter(speciality = speciality)
        context = {
            'speciality': speciality,
            'doctor':doctor,
            'title': f'{speciality.title}'
        }
        return render(request, 'diagerda/speciality.html', context)
