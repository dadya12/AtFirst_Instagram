from django.contrib import admin
from accounts.models import User


@admin.register(User)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'username']
    list_filter = ['id', 'username']
    search_fields = ['username', 'id']
    fields = ['username', 'email', 'avatar', 'password', 'first_name', 'info', 'phone', 'gender']
