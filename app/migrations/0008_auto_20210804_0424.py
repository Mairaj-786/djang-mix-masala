# Generated by Django 3.1.3 on 2021-08-04 11:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_post'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='user',
        ),
        migrations.AddField(
            model_name='post',
            name='desc',
            field=models.CharField(default='test', max_length=40),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='img',
            field=models.ImageField(blank=True, null=True, upload_to='pic'),
        ),
    ]