# Generated by Django 4.2.11 on 2024-04-28 22:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vege', '0006_department_studentid_student'),
    ]

    operations = [
        migrations.AlterField(
            model_name='department',
            name='department',
            field=models.CharField(max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='studentid',
            name='student_id',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]
