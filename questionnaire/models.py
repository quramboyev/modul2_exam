from django.db import models

class ContestCategory(models.Model):
    name = models.CharField(max_length=255, verbose_name="Категория конкурса")

    def __str__(self):
        return self.name


class Questionnaire(models.Model):
    GENDER_CHOICES = [
        ('male', 'Мужской'),
        ('female', ' Женский')
    ]

    CITIES_CHOICES = [
        ('tashkent', 'Ташкент'),
        ('qaraqalpakistan', 'Каракалпакистан'),
        ('andijan', 'Андижан'),
        ('buxara', 'Бухара'),
        ('djizakh', 'Жиззах'),
        ('fergana', 'Фергана'),
        ('qashqadaryo', 'Кашкадаря'),
        ('xorezm', 'Хорезм'),
        ('namangan', 'Наманган'),
        ('navoi', 'Навои'),
        ('samarkand', 'Самарканд'),
        ('surhandaryo', 'Сурхандаря'),
        ('sirdaryo', 'Сирдарья'),
    ]
    
    first_name = models.CharField(max_length=50, verbose_name='Имя')
    last_name  = models.CharField(max_length=50, verbose_name='Фамилия')
    age = models.PositiveBigIntegerField(verbose_name='Лет')
    category = models.ForeignKey(ContestCategory, on_delete=models.CASCADE, verbose_name='Категория конкурса')
    city = models.CharField(max_length=15, choices=CITIES_CHOICES, verbose_name='Город')
    phone = models.CharField(max_length=13, verbose_name='Телефон')
    gender = models.CharField(max_length=6, choices=GENDER_CHOICES, verbose_name='Пол')
    comment = models.TextField(blank=True, null=True, verbose_name='Коммент')

    def __str__(self):
        return f"{self.first_name}-{self.category}"