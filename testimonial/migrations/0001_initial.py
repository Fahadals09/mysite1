# Generated by Django 3.2.6 on 2021-08-16 17:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='testimonial',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('jobname', models.CharField(max_length=120)),
                ('image', models.ImageField(upload_to='posts/')),
                ('Comment', models.TextField(max_length=2000)),
            ],
        ),
    ]
