# Generated by Django 3.1.4 on 2020-12-04 07:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sparkxmain', '0008_auto_20201204_1236'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='Comments',
            field=models.JSONField(blank=True, default='{}'),
        ),
        migrations.AlterField(
            model_name='post',
            name='Image',
            field=models.ImageField(upload_to='Posts'),
        ),
        migrations.AlterField(
            model_name='post',
            name='likes',
            field=models.JSONField(blank=True, default='{}'),
        ),
        migrations.AlterField(
            model_name='post',
            name='saved',
            field=models.JSONField(blank=True, default='{}'),
        ),
        migrations.AlterField(
            model_name='user',
            name='Dp',
            field=models.ImageField(upload_to='DPs'),
        ),
    ]
