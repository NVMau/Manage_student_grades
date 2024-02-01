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
    user_name = models.CharField(max_length=100)
    birthDate = models.DateField(null=True)
    address = models.CharField(max_length=128)

    #them do loi xung dot
    # groups = models.ManyToManyField(
    #     Group,
    #     related_name="%(app_label)s_%(class)s_related",
    #     related_query_name="%(app_label)s_%(class)ss"
    # )
    # user_permissions = models.ManyToManyField(
    #     Permission,
    #     related_name="%(app_label)s_%(class)s_related",
    #     related_query_name="%(app_label)s_%(class)ss"
    # )
    # #####

    class UserRole(models.TextChoices):
        ADMIN = 'admin'
        LECTURER = 'lecturer'
        STUDENT = 'student'
    role = models.CharField(max_length=10, choices=UserRole.choices, default=UserRole.STUDENT)


class Student(ModelBase):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='student_profile')
    avatar = models.ImageField(upload_to='uploads/%Y/%m')
    description = models.TextField(null=True, blank=True)
    # Các trường khác của sinh viên


class Lecturer(ModelBase):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='lecturer_profile')
    description = models.TextField(null=True, blank=True)
    # Các trường khác của giảng viên

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
    students = models.ManyToManyField(Student, related_name='enrolled_classes')
    lecturer = models.ForeignKey(Lecturer, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name
class ScoreColumn(ModelBase):
    name = models.CharField(max_length=100, unique=False, null=False)
    score = models.FloatField()
    def __str__(self):
        return self.name

class ResultLearning(ModelBase):
    student = models.ForeignKey(Student, on_delete=models.SET_NULL, null=True)
    study_class = models.ForeignKey(StudyClass, on_delete=models.CASCADE)
    midterm_score = models.FloatField()
    final_score = models.FloatField()
    flag = models.BooleanField(default=False)#Dùng để check xem đa luu chua
    score_column = models.ForeignKey(ScoreColumn, on_delete=models.SET_NULL, null=True)

