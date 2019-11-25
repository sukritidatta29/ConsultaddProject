<<<<<<< HEAD
from django.db import models
# Create your models here.


class Stu(models.Model):
    name=models.CharField(max_length=20)
    email=models.EmailField(max_length=30, unique=True)
    gender=models.CharField(max_length=20, default="Do not want to share")

    def __str__(self):
        return self.name

class TypeOfSession(models.Model):
    Session=models.CharField(max_length=20)

    def __str__(self):
        return self.Session

class StuSession(models.Model):
    name=models.CharField(max_length=20)
    Session=models.ForeignKey("TypeOfSession", on_delete=models.PROTECT)

    def __str__(self):
        return self.name

class SignUpForm(models.Model):
    firstname = models.CharField(max_length=20)
    lastname = models.CharField(max_length=20)
    email = models.EmailField()
    password = models.CharField(max_length=10)
    repassword = models.CharField(max_length=10)


class Post(models.Model):
    pid = models.CharField(max_length=20)
    pname = models.CharField(max_length=15)
    pemail = models.EmailField()
    blog = models.CharField(max_length=1000)

    class Meta:
        db_table = "post"
=======

# Create your models here.





>>>>>>> origin/master
