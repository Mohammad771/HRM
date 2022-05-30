from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(bank_account)
admin.site.register(allowances)
admin.site.register(annual_bonuses)
admin.site.register(punishments)
admin.site.register(rewards)
admin.site.register(payrolls)