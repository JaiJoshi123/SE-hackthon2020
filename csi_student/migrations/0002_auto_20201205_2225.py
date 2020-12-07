# Generated by Django 2.1.5 on 2020-12-05 16:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('csi_student', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='grade',
            field=models.DecimalField(decimal_places=1, default=5.0, max_digits=2),
        ),
        migrations.AlterField(
            model_name='student',
            name='projects',
            field=models.TextField(blank=True, null=True),
        ),
    ]