# Generated by Django 3.2.6 on 2021-08-19 12:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('About', '0007_link'),
    ]

    operations = [
        migrations.RenameField(
            model_name='link',
            old_name='Facebook',
            new_name='url',
        ),
        migrations.RemoveField(
            model_name='link',
            name='Pinsterst',
        ),
        migrations.RemoveField(
            model_name='link',
            name='Twitter',
        ),
        migrations.RemoveField(
            model_name='link',
            name='instagram',
        ),
        migrations.AddField(
            model_name='link',
            name='icon',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
    ]
