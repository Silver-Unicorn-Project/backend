from django.contrib.auth.models import AbstractUser
from django.db import models
from django.contrib.auth.validators import UnicodeUsernameValidator


class User(AbstractUser):
    """Модель пользователя"""
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ('username', 'password')

    email = models.EmailField(
        'Электронная почта',
        unique=True,
        blank=False,
        max_length=100,
        help_text='Введите вашу электронную почту',
    )
    username = models.CharField(
        'Логин',
        unique=True,
        max_length=100,
        help_text='Введите уникальный логин',
        validators=[
            UnicodeUsernameValidator
        ]
    )
    password = models.CharField(
        'Пароль',
        max_length=100,
        help_text='Введите пароль',
    )
    first_name = models.CharField(
        'Имя',
        max_length=100,
        blank=False,
        help_text='Введи вашем имя',
    )
    last_name = models.CharField(
        'Фамилия',
        max_length=100,
        blank=False,
        help_text='Введите вашу фамилию',
    )

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
        ordering = ('id',)

    def __str__(self):
        return f'{self.username}, {self.email}'
