from django.contrib import admin
from .models import Profile


# Register your models here.

@admin.register(Profile)
class ProfileModelAdmin(admin.ModelAdmin):
  list_display = ['id', 'name', 'email', 'date', 'address', 'gender','pimage', 'rdoc']
