# Generated by Django 4.1.1 on 2022-09-22 07:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exam', '0002_alter_person_table'),
    ]

    operations = [
        migrations.CreateModel(
            name='Musicion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('instrument', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'Musiction',
            },
        ),
    ]
