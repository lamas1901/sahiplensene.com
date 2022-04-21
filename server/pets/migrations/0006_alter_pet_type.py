# Generated by Django 4.0.4 on 2022-04-17 13:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pets', '0005_alter_pet_sex'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pet',
            name='type',
            field=models.CharField(choices=[('normal', 'Normal'), ('super', 'Süper'), ('platinum', 'Platinum'), ('gold', 'Gold'), ('silver', 'Gümüş')], default='normal', max_length=50),
        ),
    ]