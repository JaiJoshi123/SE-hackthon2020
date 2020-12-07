# Generated by Django 2.1.5 on 2020-12-05 16:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=120)),
                ('password', models.CharField(max_length=120)),
                ('uid', models.CharField(max_length=10)),
                ('name', models.CharField(max_length=30)),
                ('interests', models.TextField()),
                ('grade', models.DecimalField(decimal_places=1, max_digits=2)),
                ('projects', models.TextField()),
            ],
        ),
    ]