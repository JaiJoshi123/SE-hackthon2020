# Generated by Django 2.1.5 on 2020-12-06 19:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='file',
            field=models.FileField(null=True, upload_to=''),
        ),
    ]