from django.db import models
import datetime

# Create your models here.
class clientinfo(models.Model):
    client_id=models.PositiveIntegerField()
    client_name=models.CharField(max_length=100)
    created_at=models.DateTimeField(default=datetime.datetime.now)
    created_by=models.CharField(max_length=100)

class user2(models.Model):
    user_id=models.PositiveIntegerField()
    user_name=models.CharField(max_length=120)
    project_name=models.CharField(max_length=100)
    created_at=models.DateTimeField(default=datetime.datetime.now)
    created_by=models.CharField(max_length=100)
    updated_at=models.DateTimeField(default=datetime.datetime.now)







