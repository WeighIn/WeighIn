from django.db import models


class User(models.Model):
    username = models.CharField(max_length=32, unique=True, db_index=True)
    email = models.EmailField(max_length=254, unique=True)
    password = models.CharField(max_length=60)


class Application(models.Model):
    name = models.CharField(max_length=32, unique=True, db_index=True)


class Task(models.Model):
    app = models.ForeignKey("Application")
    worth = models.DecimalField()
    data = models.BinaryField()


class Result(models.Model):
    task = models.ForeignKey("Task")
    user = models.ForeignKey("User")
    submit_date = models.DateField(auto_now_add=True)
    data = models.BinaryField()