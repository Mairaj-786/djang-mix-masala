# Generated by Django 3.1.3 on 2021-08-04 08:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_question'),
    ]

    operations = [
        migrations.CreateModel(
            name='Choice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.question')),
            ],
        ),
    ]
