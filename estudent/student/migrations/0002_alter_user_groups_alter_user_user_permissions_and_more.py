# Generated by Django 5.0.1 on 2024-02-01 07:04

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('student', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='groups',
            field=models.ManyToManyField(related_name='%(app_label)s_%(class)s_related', related_query_name='%(app_label)s_%(class)ss', to='auth.group'),
        ),
        migrations.AlterField(
            model_name='user',
            name='user_permissions',
            field=models.ManyToManyField(related_name='%(app_label)s_%(class)s_related', related_query_name='%(app_label)s_%(class)ss', to='auth.permission'),
        ),
        migrations.CreateModel(
            name='ResultLearning',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
                ('active', models.BooleanField(default=True)),
                ('midterm_score', models.FloatField()),
                ('final_score', models.FloatField()),
                ('flag', models.BooleanField(default=False)),
                ('score_column', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='student.scorecolumn')),
                ('student', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='student.student')),
                ('study_class', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student.studyclass')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
