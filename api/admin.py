from django.contrib import admin
#to import database model
from . models import *
# Register your models here to admin page
admin.site.register(ApiTable)

#python manage.py createsuperuser