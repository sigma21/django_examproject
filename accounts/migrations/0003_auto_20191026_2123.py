# Generated by Django 2.2.6 on 2019-10-26 21:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20191026_1039'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='username',
            field=models.CharField(blank=True, max_length=30, unique=True),
        ),
    ]
