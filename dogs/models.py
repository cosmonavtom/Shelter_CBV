from django.db import models
from django.conf import settings

from users.models import NULLABLE


class Category(models.Model):
    ''' Модель для породы собак. Содержит название породы и описание '''
    name = models.CharField(max_length=100, verbose_name='breed')
    description = models.CharField(max_length=1000, verbose_name='descriptions')

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'breed'
        verbose_name_plural = 'breeds'


class Dog(models.Model):
    ''' Модель для собаки. Содержит имя, породу, изображение, дату рождения, активность
        владельца и кол-во просмотров '''
    name = models.CharField(max_length=250, verbose_name='dog_name')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='breed')
    photo = models.ImageField(upload_to='dogs/', **NULLABLE, verbose_name='image')
    birth_date = models.DateField(**NULLABLE, verbose_name='birth_date')
    is_active = models.BooleanField(default=True, verbose_name='active')

    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, **NULLABLE,
                              verbose_name='владелец')
    views = models.IntegerField(default=0, verbose_name='просмотры')

    def __str__(self):
        return f'{self.name} ({self.category})'

    class Meta:
        verbose_name = 'dog'
        verbose_name_plural = 'dogs'

    def views_count(self):
        self.views += 1
        self.save()


class Parent(models.Model):
    ''' Родословная собаки. Содержит имя, породу и дату рождения родителя собаки '''
    dog = models.ForeignKey(Dog, on_delete=models.CASCADE)
    name = models.CharField(max_length=250, verbose_name='dog_name')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='breed')
    birth_date = models.DateField(**NULLABLE, verbose_name='birth_date')

    def __str__(self):
        return f'{self.name} ({self.category})'

    class Meta:
        verbose_name = 'parent'
        verbose_name_plural = 'parents'
