# Generated by Django 2.2.6 on 2019-10-26 10:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='dob',
            field=models.DateField(max_length=30, null=True, verbose_name='date of birth'),
        ),
    ]
