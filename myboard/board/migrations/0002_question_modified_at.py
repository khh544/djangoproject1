# Generated by Django 4.1.1 on 2022-10-05 15:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='modified_at',
            field=models.DateTimeField(auto_now=True, verbose_name='수정날짜'),
        ),
    ]