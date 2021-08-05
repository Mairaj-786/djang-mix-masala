from django.db import models

# Create your models here.

class Department(models.Model):
    title = models.CharField(max_length=40)

    def __str__(self):
        return self.title    

class Student(models.Model):
    name = models.CharField(max_length=40)
    role = models.FloatField()
    part = models.CharField(max_length=5)
    dept = models.ForeignKey(Department,  on_delete=models.CASCADE)

    def __str__(self):
        return self.name 

class Book(models.Model):
    title = models.CharField(max_length=40)
    author = models.CharField(max_length=40)
    dept = models.ForeignKey(Department,  on_delete=models.CASCADE)

    
    def __str__(self):
        return self.title 


class Reserved_Book(models.Model):
    s_name = models.ForeignKey(Student,on_delete=models.CASCADE)
    b_name = models.ForeignKey(Book, on_delete=models.CASCADE)

    
    def __str__(self):
        return f"{self.s_name}, reserved {self.b_name} book"