from django.db import models
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User


class Profile(models.Model):
    user_id = models.OneToOneField(User, related_name="Profile")
    points = models.BigIntegerField(default=0)

    def __unicode__(self):
        return str(self.user_id)

class Application(models.Model):
    app_id = models.BigIntegerField(primary_key=True)
    user_id = models.OneToOneField(User, related_name="Application")  # Owner
    weight = models.IntegerField(default=1)
    points = models.BigIntegerField(default=1)

    def __unicode__(self):
        return str(self.app_id)

    class Meta:
        permissions = (
            ("add", "Create a new Application instance"),
            ("change", "Alter a current Application instance"),
            ("delete", "Delete an Application instance"),
        )


class Task(models.Model):
    task_id = models.BigIntegerField(primary_key=True)
    app_id = models.ForeignKey(Application, related_name="Tasks")
    worth = models.FloatField()
    accuracy = models.IntegerField()
    data = models.TextField()
    complete = models.BooleanField()

    def __unicode__(self):
        return str(self.task_id)

    class Meta:
        permissions = (
            ("add", "Create a new Task"),
            ("change", "Alter a current Task"),
            ("delete", "Delete a Task"),
        )


class Result(models.Model):
    result_id = models.BigIntegerField(primary_key=True)
    task_id = models.ForeignKey(Task, related_name="Results")
    user_id = models.ForeignKey(User, related_name="Results")
    submit_date = models.DateField(auto_now_add=True)
    data = models.TextField()

    def __unicode__(self):
        return str(self.result_id)

    class Meta:
        permissions = (
            ("add", "Create a new Result"),
            ("change", "Alter a current Result"),
            ("delete", "Delete a Result"),
        )
