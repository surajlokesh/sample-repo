from django.db import models

# Create your models here.

class Student(models.Model):
    student_name=models.CharField('student Name',null=False,max_length=30)
    dept=(
        ('CSE','Computer Science'),
        ('MH','Mech'),
        ('CV','Civil')
    )
    department=models.CharField('Department',choices=dept,blank=True,null=True,max_length=30)
    timestamp= models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.student_name
    

class section(models.Model):
    section=models.CharField("Section",max_length=30,null=False)
    advisor=models.OneToOneField('teacher',on_delete=models.SET_NULL,null=True)
    students=models.ManyToManyField('student',null=False)
    def __str__(self):
        return self.section

class book(models.Model):
    book=models.CharField('book name',blank=True,null=False,max_length=30)
    def __str__(self):
        return self.book

class Teacher(models.Model):
    teacher=models.CharField('teacher name',max_length=100,null=False)
    timestamp= models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.teacher


class Library(models.Model):
    Library_name=models.CharField('library',null=True,max_length=30)
    books=models.ManyToManyField('Book',null=False)
    def __str__(self):
        return self.Library_name

