from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(users)
admin.site.register(attachments)
admin.site.register(attachment_types)
admin.site.register(attachments_users)
admin.site.register(countries)
admin.site.register(addresses)
admin.site.register(user_types)
admin.site.register(roles)
admin.site.register(permissions)
admin.site.register(roles_and_permissions)
admin.site.register(courses)
admin.site.register(skills)