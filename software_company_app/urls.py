# software_company_app/urls.py

from django.urls import path
from .views import project_info

urlpatterns = [
    path('', project_info, name='project_info'),
]
