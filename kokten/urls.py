from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('multienv.urls')),
    path('venv/<str:venv_name>/', views.venv, name='venv'),
    path('create_venv/', views.create_venv, name='create_venv'),
]
