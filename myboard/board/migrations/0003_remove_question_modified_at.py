# Generated by Django 4.1.1 on 2022-10-05 15:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0002_question_modified_at'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='modified_at',
        ),
    ]