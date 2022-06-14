from django.contrib import admin
from .models import Instruction


class InstructionAdmin(admin.ModelAdmin):
    list_display = ("title", "subtitle", "is_public")
