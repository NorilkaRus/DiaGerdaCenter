from django.db import models
from users.models import User
# Create your models here.
NULLABLE = {'blank':  True, 'null': True}

class Doctor(models.Model):

    first_name = models.CharField(max_length=30, verbose_name='Имя')
    last_name = models.CharField(max_length=30, verbose_name='Фамилия')
    photo = models.ImageField(upload_to='person/', verbose_name='Фото', **NULLABLE)
    speciality = models.CharField(max_length=50, verbose_name='Специализация')

    def __str__(self):
        return f'{self.first_name} {self.last_name}: {self.speciality}'

    class Meta:
        verbose_name = 'врач'
        verbose_name_plural = 'врачи'


class Diagnostic(models.Model):
    title = models.CharField(max_length=100, verbose_name= 'наименование')
    description = models.TextField(verbose_name= 'описание', **NULLABLE)
    price = models.PositiveIntegerField(verbose_name= 'стоимость')
    doctor = models.ManyToManyField('Doctor', related_name="doctor")

    def __str__(self):
        return f'{self.title}: {self.price}'

    class Meta:
        verbose_name = 'диагностика'
        verbose_name_plural = 'диагностики'


class Appointment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='записи', verbose_name='пациент', **NULLABLE)
    diagnostic = models.ForeignKey(Diagnostic, on_delete=models.CASCADE, related_name='записи', verbose_name='диагностика')
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, related_name='записи', verbose_name='врач')
    date = models.DateTimeField(verbose_name='дата и время приема')


    def __str__(self):
        return f'{self.user}: {self.date} {self.diagnostic}, {self.doctor}'

    class Meta:
        verbose_name = 'запись на диагностику'
        verbose_name_plural = 'записи на диагностику'
