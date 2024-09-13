# Generated by Django 5.1.1 on 2024-09-13 09:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='phone',
            field=models.CharField(max_length=15, unique=True),
        ),
        migrations.AlterField(
            model_name='employee',
            name='salary',
            field=models.PositiveIntegerField(),
        ),
    ]
