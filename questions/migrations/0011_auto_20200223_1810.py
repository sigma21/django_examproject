# Generated by Django 3.0.3 on 2020-02-23 18:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0010_auto_20200223_1809'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account_question',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='questions.Question'),
        ),
    ]