# Generated by Django 3.1.2 on 2020-11-12 07:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CityRouters', '0003_auto_20201112_1046'),
    ]

    operations = [
        migrations.AlterField(
            model_name='station',
            name='name',
            field=models.CharField(max_length=250),
        ),
    ]