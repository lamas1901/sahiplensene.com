# Generated by Django 4.0.4 on 2022-04-16 17:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pets', '0004_rename_animale_type_pet_animal_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pet',
            name='sex',
            field=models.CharField(choices=[('male', 'Erkek'), ('female', 'Dişi')], default='male', max_length=50),
        ),
    ]