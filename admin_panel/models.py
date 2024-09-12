from django.db import models

class User(models.Model):
    name = models.CharField(max_length = 250)
    email = models.EmailField(max_length = 255)
    password = models.CharField(max_length = 300)

    def __str__(self):
        return self.name
    

class Course(models.Model):
    course_name = models.CharField(max_length = 250)
    fees = models.IntegerField()
    duration = models.CharField(max_length = 250)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.course_name
    

class Student(models.Model):
    name = models.CharField(max_length = 250)
    email = models.EmailField(max_length = 250)
    phonenum = models.BigIntegerField()
    address = models.CharField(max_length = 250)
    degree = models.CharField(max_length = 300)
    college = models.CharField(max_length = 250)
    totalamount = models.IntegerField()
    paidamount = models.IntegerField()
    dueamount = models.FloatField()
    course = models.ForeignKey(Course,on_delete=models.CASCADE)
    password = models.CharField(max_length = 250)

    def __str__(self):
        return self.name

class Teacher(models.Model):
    name = models.CharField(max_length = 250)
    email = models.EmailField(max_length = 300)
    course = models.ForeignKey(Course,on_delete=models.CASCADE)
    phonenum = models.CharField(max_length=20)
    password = models.CharField(max_length = 250,blank=True,null=True)
    
    def __str__(self):
        return self.name