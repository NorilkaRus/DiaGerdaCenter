from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
NULLABLE = {'blank':  True, 'null': True}

class User(AbstractUser):
    username = None
    first_name = models.CharField(max_length=20, verbose_name='Имя')
    last_name = models.CharField(max_length=20, verbose_name='Фамилия')
    birthday = models.DateField(verbose_name='дата рождения')
    email = models.EmailField(unique=True, verbose_name='E-mail')
    telegram = models.CharField(unique=True, max_length=20, verbose_name='Telegram')
    phone = models.CharField(unique=True, max_length=20, verbose_name='Номер телефона')
    avatar = models.ImageField(upload_to='avatars/', verbose_name='Аватар', **NULLABLE)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
