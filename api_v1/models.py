from django.db import models
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField("auth.User", related_name="Profile")
    points = models.BigIntegerField()
    app_key = models.CharField(max_length=255)


class Task(models.Model):
    app = models.ForeignKey("auth.User", related_name="Tasks")
    worth = models.FloatField()
    accuracy = models.IntegerField()
    data = models.TextField()


class Result(models.Model):
    task = models.ForeignKey("Task", related_name="Results")
    user = models.ForeignKey("auth.User", related_name="Results")
    submit_date = models.DateField(auto_now_add=True)
    data = models.TextField()
