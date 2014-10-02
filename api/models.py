from django.db import models
from passlib.hash import bcrypt


class User(models.Model):
    username = models.CharField(max_length=32, unique=True, db_index=True)
    email = models.EmailField(max_length=254, unique=True)
    password = models.CharField(max_length=60)
    points = models.BigIntegerField()

    class Meta:
        bcrypt_rounds = 8

    def password_crypt_insert(self, password):
        """ Encrypts and inserts a password into the object """
        self.password = bcrypt.encrypt(password, rounds=self.Meta.bcrypt_rounds)

    def password_crypt_compare(self, password):
        """ Compares an unencrypted password to the stored encrypted password """
        return bcrypt.encrypt(password, rounds=self.Meta.bcrypt_rounds) == self.password


class Application(models.Model):
    name = models.CharField(max_length=32, unique=True, db_index=True)
    owner = models.ForeignKey("User")
    app_key = models.CharField(max_length=255)


class Task(models.Model):
    application = models.ForeignKey("Application")
    worth = models.DecimalField()
    accuracy = models.IntegerField()
    data = models.TextField()


class Result(models.Model):
    task = models.ForeignKey("Task")
    user = models.ForeignKey("User")
    submit_date = models.DateField(auto_now_add=True)
    data = models.TextField()