# Generated by Django 2.1.5 on 2020-12-06 05:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0004_auto_20201206_1003'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stud_ans',
            name='q_id',
            field=models.DecimalField(blank=True, decimal_places=0, max_digits=4, null=True),
        ),
    ]
