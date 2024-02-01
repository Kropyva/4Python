# admin.py

from django.contrib import admin
from .models import Error, Programmer, ErrorCorrection

admin.site.register(Error)
admin.site.register(Programmer)
admin.site.register(ErrorCorrection)
