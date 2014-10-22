from django.db import models
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, related_name="Profile")
    points = models.BigIntegerField(default=0)
    is_app = models.BooleanField(default=False)
    app_key = models.CharField(max_length=255, blank=True)


class Task(models.Model):
    user = models.ForeignKey(User, related_name="Tasks")
    worth = models.FloatField()
    accuracy = models.IntegerField()
    data = models.TextField()


class Result(models.Model):
    task = models.ForeignKey(Task, related_name="Results")
    user = models.ForeignKey(User, related_name="Results")
    submit_date = models.DateField(auto_now_add=True)
    data = models.TextField()
