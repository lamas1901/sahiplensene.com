# Generated by Django 4.0.4 on 2022-04-17 13:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_post_tags'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='for_pet_type',
            field=models.CharField(choices=[('dog', 'Köpek'), ('cat', 'Kedi'), ('bird', 'Kuş')], default='dog', max_length=20),
        ),
    ]
