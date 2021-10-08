from django.db import models


# Create your models here.

class Student(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=200)
    contact = models.CharField(max_length=50)
    address = models.CharField(max_length=200)
    lat = models.CharField(max_length=30)
    lng = models.CharField(max_length=30)
    state = models.CharField(max_length=50, null=True)
    city = models.CharField(max_length=50, null=True)

    def __str__(self):
        return self.email + " --> " + self.password + " --> " + self.name

class Institute(models.Model):
    name = models.CharField(max_length=200)
    adminName = models.CharField(max_length=100)
    email = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=200)
    landmark = models.CharField(max_length=200, null=True)
    contact = models.CharField(max_length=50)
    address = models.CharField(max_length=200)
    lat = models.CharField(max_length=30)
    lng = models.CharField(max_length=30)
    state = models.CharField(max_length=50, null=True)
    city = models.CharField(max_length=50, null=True)

    def __str__(self):
        return self.email + " --> " + self.password + " --> " + self.name

class Course(models.Model):
    courseName = models.CharField(max_length=200)
    courseFees = models.IntegerField()
    institute = models.ForeignKey(Institute, on_delete=models.CASCADE)


class Enquiry(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    # admission = 1 , enquiry = 0;
    admissionStatus = models.IntegerField(default=0);
    readStatus = models.IntegerField();


class Rating(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    rate = models.IntegerField();
