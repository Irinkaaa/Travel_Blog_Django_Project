# Generated by Django 3.1.3 on 2020-12-13 08:44

import Travel_blog.app.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20201212_1629'),
    ]

    operations = [
        migrations.AlterField(
            model_name='destination',
            name='year',
            field=models.IntegerField(validators=[Travel_blog.app.validators.year_validator]),
        ),
    ]