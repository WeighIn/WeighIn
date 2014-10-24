from django.db import models
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, related_name="Profile")
    points = models.BigIntegerField(default=0)


class Application(models.Model):
    weight = models.IntegerField(default=1)
    owners = models.ManyToManyField(User)
    points = models.BigIntegerField(default=0)

    class Meta:
        permissions = (
            ("add", "Create a new Application instance"),
            ("change", "Alter a current Application instance"),
            ("delete", "Delete an Application instance"),
        )


class Task(models.Model):
    user = models.ForeignKey(User, related_name="Tasks")
    worth = models.FloatField()
    accuracy = models.IntegerField()
    data = models.TextField()

    class Meta:
        permissions = (
            ("add", "Create a new Task"),
            ("change", "Alter a current Task"),
            ("delete", "Delete a Task"),
        )


class Result(models.Model):
    task = models.ForeignKey(Task, related_name="Results")
    user = models.ForeignKey(User, related_name="Results")
    submit_date = models.DateField(auto_now_add=True)
    data = models.TextField()

    class Meta:
        permissions = (
            ("add", "Create a new Result"),
            ("change", "Alter a current Result"),
            ("delete", "Delete a Result"),
        )
