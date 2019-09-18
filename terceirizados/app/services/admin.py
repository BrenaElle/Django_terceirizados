from django.contrib import admin
from app.services import models as services

admin.site.register(services.Services)

