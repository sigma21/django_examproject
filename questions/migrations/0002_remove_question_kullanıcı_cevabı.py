# Generated by Django 2.2.6 on 2019-10-25 12:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='kullanıcı_cevabı',
        ),
    ]
