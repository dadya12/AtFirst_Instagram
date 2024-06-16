from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission


class User(AbstractUser):
    GENDER_CHOICES = [
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other')
    ]
    email = models.EmailField(unique=True, verbose_name='Почта', max_length=50)
    avatar = models.ImageField(upload_to='avatars/', verbose_name='Аватар')
    info = models.TextField(verbose_name='Информация о пользователе', max_length=500, blank=True, null=True)
    phone = models.CharField(verbose_name='Телефон', blank=True, null=True, max_length=20)
    gender = models.CharField(max_length=20, blank=True, null=True, choices=GENDER_CHOICES)
    publication_count = models.PositiveIntegerField(default=0, verbose_name='Публикации')
    subscription_count = models.PositiveIntegerField(default=0, verbose_name='Подписки')
    follower_count = models.PositiveIntegerField(default=0, verbose_name='Подписчики')

    def __str__(self):
        return self.username
