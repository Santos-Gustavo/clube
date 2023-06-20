from django.contrib import admin

from .models import WorkModel, ServiceModel

admin.site.register([WorkModel, ServiceModel])
