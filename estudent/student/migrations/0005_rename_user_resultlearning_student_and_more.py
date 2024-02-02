# Generated by Django 5.0.1 on 2024-02-02 02:26

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0004_remove_studyclass_lecturer_remove_student_user_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='resultlearning',
            old_name='User',
            new_name='student',
        ),
        migrations.RenameField(
            model_name='studyclass',
            old_name='user',
            new_name='lecturer',
        ),
        migrations.AddField(
            model_name='studyclass',
            name='student',
            field=models.ManyToManyField(related_name='enrolled_classes', to=settings.AUTH_USER_MODEL),
        ),
    ]
