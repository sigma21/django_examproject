# Generated by Django 2.2.6 on 2019-11-11 00:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('questions', '0003_auto_20191026_2236'),
    ]

    operations = [
        migrations.RenameField(
            model_name='question',
            old_name='dogru_cevap',
            new_name='answer',
        ),
        migrations.RenameField(
            model_name='question',
            old_name='soru',
            new_name='text',
        ),
        migrations.CreateModel(
            name='Account_Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_answer', models.CharField(max_length=20)),
                ('test_completed', models.BooleanField(default=False)),
                ('text', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='questions.Question')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='question',
            name='user',
            field=models.ManyToManyField(through='questions.Account_Question', to=settings.AUTH_USER_MODEL),
        ),
    ]
