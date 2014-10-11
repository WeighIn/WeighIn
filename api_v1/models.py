from django.db import models
from passlib.hash import bcrypt


class User(models.Model):
    username = models.CharField(max_length=32, unique=True, db_index=True)
    email = models.EmailField(max_length=254)
    password = models.CharField(max_length=60)
    points = models.BigIntegerField()

    def password_crypt(password, rounds=8):
        return bcrypt.encrypt(password, rounds=rounds)

    def password_crypt_insert(self, password, rounds=8):
        """ Encrypts and inserts a password into the object """
        self.password = self.password_crypt(password, rounds)

    def password_crypt_compare(self, password, rounds=8):
        """ Compares an unencrypted password to the stored encrypted password """
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
