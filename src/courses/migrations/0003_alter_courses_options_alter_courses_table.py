# Generated by Django 5.1.4 on 2024-12-28 01:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0002_alter_courses_access'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='courses',
            options={'verbose_name': 'Courses', 'verbose_name_plural': 'Courses'},
        ),
        migrations.AlterModelTable(
            name='courses',
            table='courses',
        ),
    ]
