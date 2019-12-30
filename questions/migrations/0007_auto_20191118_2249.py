# Generated by Django 2.2.6 on 2019-11-18 22:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0006_auto_20191111_0036'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='account_question',
            name='test_completed',
        ),
        migrations.AlterField(
            model_name='account_question',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='questions.Question'),
        ),
    ]
