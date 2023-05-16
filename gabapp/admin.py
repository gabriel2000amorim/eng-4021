from django.contrib import admin
from .models import Task

# Registra o modelo Task no painel de administração do Django
admin.site.register(Task)
