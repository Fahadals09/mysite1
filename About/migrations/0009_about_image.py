# Generated by Django 3.2.6 on 2021-08-24 12:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('About', '0008_auto_20210819_1251'),
    ]

    operations = [
        migrations.AddField(
            model_name='about',
            name='image',
            field=models.ImageField(default=1, upload_to='posts/'),
            preserve_default=False,
        ),
    ]
