# Generated by Django 5.1.3 on 2024-11-18 15:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='emp_info',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('emid', models.IntegerField(null=True)),
                ('role', models.CharField(max_length=250)),
                ('join', models.DateField(null=True)),
            ],
        ),
    ]