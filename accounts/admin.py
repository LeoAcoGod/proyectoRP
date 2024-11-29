from django.contrib import admin
from .models import Feedback

# Register your models here.
@admin.register(Feedback)
class AllfeedbackAdmin(admin.ModelAdmin):
    list_display=("id","nombre","email","mensaje","fecha")
