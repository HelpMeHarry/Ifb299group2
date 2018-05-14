from django.db import models
import cgi


field1 = cgi.FieldStorage()
value1 = field1.getvalue('firstname')
 
class Teacher(models.Model):
    FirstName = models.CharField(max_length=100)
    LastName = models.CharField(max_length=100)
    Gender = models.CharField(max_length=10)
    DOB = models.CharField(max_length=20)
    EmailAd = models.CharField(max_length=200)
    PhoneNumber = models.CharField(max_length=10)
    Qualifications = models.CharField(max_length=100)

    def __str__(self):
        return self.FirstName + "_" + self.LastName + "-" + self.Qualifications


# Defines a student database with fields:
class Student(models.Model):
    FirstName = models.CharField(max_length=100)
    LastName = models.CharField(max_length=100)
    Gender = models.CharField(max_length=10)
    DOB = models.CharField(max_length=20)
    EmailAd = models.CharField(max_length=200)
    PhoneNumber = models.CharField(max_length=100)
    Address = models.CharField(max_length=100)
    TeacherID = models.ForeignKey(Teacher, on_delete=models.CASCADE) #deletes students attached to teacher
 # Defines a teacher table with columns
 
    
