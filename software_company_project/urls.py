# software_company_project/urls.py

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('project-info/', include('software_company_app.urls')),
]
