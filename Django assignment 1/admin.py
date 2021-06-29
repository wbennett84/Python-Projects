from django.contrib import admin



# Registering my models here
from .models import djangoClasses

admin.site.register(djangoClasses)

