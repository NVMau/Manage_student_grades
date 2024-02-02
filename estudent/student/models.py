from django.db import models
# Create your models here.
from django.contrib.auth.models import AbstractUser, Permission, Group


class ModelBase(models.Model):
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now = True)
    active = models.BooleanField(default=True)

    class Meta:
        abstract = True

class User(AbstractUser):
    birthDate = models.DateField(null=True)
    address = models.CharField(max_length=128)
    first_name = models.CharField(max_length=150, blank=True)
    last_name = models.CharField(max_length=150, blank=True)
    avatar = models.ImageField(upload_to='uploads/%Y/%m', null=True, blank=True)


    class UserRole(models.TextChoices):
        ADMIN = 'admin'
        LECTURER = 'lecturer'
        STUDENT = 'student'
    role = models.CharField(max_length=10, choices=UserRole.choices, default=UserRole.STUDENT)


class Course(ModelBase):
    name = models.CharField(max_length=100, unique=True, null=False)

    def __str__(self):
        return self.name

class Semester(ModelBase):
    name = models.CharField(max_length=100, unique=True, null=False)

    def __str__(self):
        return self.name

class StudyClass(ModelBase):
    name = models.CharField(max_length=100, unique=True, null=False)
    semester = models.ForeignKey(Semester, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    student = models.ManyToManyField(User, related_name='enrolled_classes')#Sinh viên
    lecturer = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)#Giang viên

    def __str__(self):
        return self.name
class ScoreColumn(ModelBase):
    name = models.CharField(max_length=100, unique=False, null=False)
    score = models.FloatField()
    def __str__(self):
        return self.name

class ResultLearning(ModelBase):
    student = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)#sinh vien
    study_class = models.ForeignKey(StudyClass, on_delete=models.CASCADE)
    midterm_score = models.FloatField()
    final_score = models.FloatField()
    flag = models.BooleanField(default=False)#Dùng để check xem đa luu chua
    score_column = models.ForeignKey(ScoreColumn, on_delete=models.SET_NULL, null=True)

