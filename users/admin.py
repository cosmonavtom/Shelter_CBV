from django.contrib import admin
from users.models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    ''' Пользователи с полями и сортировкой для админки '''
    list_display = ('last_name', 'first_name', 'email', 'role', 'pk', 'is_active')
    list_filter = ('last_name',)
