# Generated by Django 5.0.6 on 2024-05-20 21:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('residence_management', '0007_alter_building_availability_alter_building_faculty_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='building',
            name='sex_of_students',
        ),
    ]