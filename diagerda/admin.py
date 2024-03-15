from django.contrib import admin
from .models import Doctor, Diagnostic, Appointment, Speciality
# Register your models here.

@admin.register(Speciality)
class SpecialityAdmin(admin.ModelAdmin):
    list_display = ('title',)

@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name',)
    list_filter = ('last_name', 'speciality',)
    search_fields = ('last_name', 'speciality',)

@admin.register(Diagnostic)
class DiagnosticAdmin(admin.ModelAdmin):
    list_display = ('title', 'price',)
    list_filter = ('price', 'doctor',)
    search_fields = ('title', 'price', 'doctor',)

@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ('user', 'doctor', 'diagnostic',)
    list_filter = ('user', 'doctor', 'diagnostic',)
    search_fields = ('user', 'doctor', 'diagnostic',)