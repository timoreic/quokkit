from django.contrib import admin
from .models import Instruction, Step, Item, Category

admin.site.register(Instruction)
admin.site.register(Step)
admin.site.register(Item)
admin.site.register(Category)
