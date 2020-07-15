from django.contrib import admin

# Register your models here.
from app_challenge.models import Occurrence, Category

admin.site.register(Occurrence)
admin.site.register(Category)


