# Generated by Django 4.0.4 on 2022-04-13 20:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pets', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pet',
            name='animale_type',
            field=models.CharField(choices=[], max_length=50),
        ),
    ]