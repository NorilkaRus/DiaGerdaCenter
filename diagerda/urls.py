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
    path('appointments/my/', AppointmentUserListView.as_view(), name='user_appointments'),
    path('appointments/archive/', AppointmentArchiveListView.as_view(), name='appointments_archive'),
    path('appointments/<int:pk>/add/', AppointmentAddView.as_view(), name='appointments_add'),
    path('appointments/<int:pk>/cancel/', AppointmentCancelView.as_view(), name='appointments_cancel'),
    path("speciality/<int:pk>/", SpecialityDetailView.as_view(), name="speciality_detail"),
]
