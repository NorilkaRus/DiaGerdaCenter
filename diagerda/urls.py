from .views import *
from django.urls import path
from diagerda.apps import DiagerdaConfig
from django.views.decorators.cache import cache_page

app_name = DiagerdaConfig.name

urlpatterns = [
    path('', SpecialityListView.as_view(), name='index'),
    path('about/', about, name='about'),
    path('doctors/', DoctorsListView.as_view(), name='doctors'),
    path('appointments/', AppointmentListView.as_view(), name='appointments'),
    path('appointments/update/<int:pk>/', AppointmentUpdateView.as_view(), name='appointments_update'),
    path("speciality/<int:pk>/", SpecialityDetailView.as_view(), name="speciality_detail"),
]
