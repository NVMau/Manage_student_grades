from django.contrib import admin
from .models import Course, Semester, StudyClass, ResultLearning, User, ScoreColumn
# Register your models here.


class CourseAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "created_date", "active"]

class SemesterAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "created_date", "active"]

class StudyClassAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "semester", "course", "lecturer",  "created_date", "active"]

class ResultLearningAdmin(admin.ModelAdmin):
    list_display = ["id", "student", "midterm_score", "final_score", "flag", "created_date", "active"]

class UserAdmin(admin.ModelAdmin):
    list_display = ["id", "last_name", "first_name", "username"]


class ScoreColumnAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "score", "created_date", "active"]

admin.site.register(Course, CourseAdmin)
admin.site.register(Semester, SemesterAdmin)
admin.site.register(StudyClass, StudyClassAdmin)
admin.site.register(ResultLearning, ResultLearningAdmin)
admin.site.register(User, UserAdmin)
admin.site.register(ScoreColumn, ScoreColumnAdmin)



