# Generated by Django 3.0.3 on 2020-04-11 10:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('covid_app', '0005_auto_20200410_2054'),
    ]

    operations = [
        migrations.CreateModel(
            name='data_base',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.FileField(blank=True, upload_to='File')),
            ],
        ),
    ]
