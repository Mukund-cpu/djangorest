from django.db import models

# Create your models here.
class ApiTable(models.Model):
    name = models.CharField(max_length=20)
    age = models.IntegerField()


#python manage.py makemigrations
#python manage.py migrate
