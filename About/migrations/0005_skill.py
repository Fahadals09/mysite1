# Generated by Django 3.2.6 on 2021-08-18 13:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('About', '0004_about'),
    ]

    operations = [
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('number', models.IntegerField(default='')),
            ],
        ),
    ]
