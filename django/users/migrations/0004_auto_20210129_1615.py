# Generated by Django 3.1.5 on 2021-01-29 16:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20210129_1427'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newuser',
            name='stars',
            field=models.IntegerField(default=0),
        ),
    ]