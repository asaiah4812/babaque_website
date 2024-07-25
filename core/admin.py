from django.contrib import admin
from .models import Testimony

# Register your models here.

@admin.register(Testimony)
class TestimonyAdmin(admin.ModelAdmin):
    list_display = ['id','author']
