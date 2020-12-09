# Generated by Django 3.1.4 on 2020-12-08 07:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sparkxmain', '0013_user_postlist'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='Comments',
            field=models.JSONField(blank=True, default=[]),
        ),
        migrations.AlterField(
            model_name='post',
            name='likes',
            field=models.JSONField(blank=True, default=[]),
        ),
        migrations.AlterField(
            model_name='post',
            name='saved',
            field=models.JSONField(blank=True, default=[]),
        ),
        migrations.AlterField(
            model_name='user',
            name='Dp',
            field=models.ImageField(default='static/media/Dps/profileicon.png', upload_to='DPs'),
        ),
        migrations.AlterField(
            model_name='user',
            name='Followers',
            field=models.JSONField(blank=True, default=[]),
        ),
        migrations.AlterField(
            model_name='user',
            name='Following',
            field=models.JSONField(blank=True, default=[]),
        ),
        migrations.AlterField(
            model_name='user',
            name='Notifications',
            field=models.JSONField(blank=True, default=[]),
        ),
        migrations.AlterField(
            model_name='user',
            name='Postlist',
            field=models.JSONField(blank=True, default=[]),
        ),
    ]
