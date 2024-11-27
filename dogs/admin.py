from django.contrib import admin

from dogs.models import Dog, Category


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    ''' Породы с полями и сортировкой для админки'''
    list_display = ('pk', 'name')
    ordering = ('pk', 'name')


@admin.register(Dog)
class Dog(admin.ModelAdmin):
    ''' Собаки с полями и сортировкой для админки '''
    list_display = ('name', 'category', 'is_active')
    list_filter = ('category',)
    ordering = ('name',)
