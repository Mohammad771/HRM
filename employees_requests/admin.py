from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(loans)
admin.site.register(vacations)
admin.site.register(overtime_categories)
admin.site.register(overtime)