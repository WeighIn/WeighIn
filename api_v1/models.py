from django.db import models
from passlib.hash import bcrypt


class User(models.Model):
    username = models.CharField(max_length=32, unique=True, db_index=True)
    email = models.EmailField(max_length=254)
    _password = models.CharField(db_column='password', max_length=60)
    points = models.BigIntegerField()

    @staticmethod
    def password_crypt(self, password, rounds=8):
        return bcrypt.encrypt(password, rounds=rounds)

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, password, rounds=8):
        self.password = self.password_crypt(password, rounds)

    def password_verify(self, password, rounds=8):
        return self.password_crypt(password, rounds) == self.password


class Application(models.Model):
    name = models.CharField(max_length=32, unique=True, db_index=True)
    owner = models.ForeignKey("User")
    app_key = models.CharField(max_length=255)


class Task(models.Model):
    application = models.ForeignKey("Application")
    worth = models.FloatField()
    accuracy = models.IntegerField()
    data = models.TextField()


class Result(models.Model):
    task = models.ForeignKey("Task")
    user = models.ForeignKey("User")
    submit_date = models.DateField(auto_now_add=True)
    data = models.TextField()
