# Generated by Django 3.0.3 on 2020-03-01 16:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exam_module', '0002_gradingsystem'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gradingsystem',
            name='grade',
            field=models.CharField(max_length=20, unique=True),
        ),
        migrations.AlterField(
            model_name='gradingsystem',
            name='greatest_lower_bound',
            field=models.DecimalField(decimal_places=2, max_digits=4, unique=True),
        ),
    ]