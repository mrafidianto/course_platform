# Generated by Django 5.1.4 on 2024-12-27 16:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Courses',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True)),
                ('image', models.ImageField(upload_to='')),
                ('access', models.CharField(choices=[('any', 'Anyone'), ('email', 'Email Required')], default='email', max_length=10)),
                ('status', models.CharField(choices=[('pub', 'Published'), ('soon', 'Coming Soon'), ('draft', 'Draft')], default='draft', max_length=10)),
            ],
        ),
    ]
