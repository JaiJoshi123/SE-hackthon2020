# Generated by Django 2.1.5 on 2020-12-06 15:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=70)),
                ('keywords', models.CharField(max_length=300)),
                ('code', models.TextField()),
                ('author', models.CharField(max_length=30)),
            ],
        ),
    ]