# Generated by Django 2.2.6 on 2019-10-26 21:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_auto_20191026_2129'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='first_name',
            field=models.CharField(default='x', max_length=60),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='account',
            name='last_name',
            field=models.CharField(default='y', max_length=60),
            preserve_default=False,
        ),
    ]
