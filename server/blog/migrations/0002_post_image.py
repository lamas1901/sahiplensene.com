# Generated by Django 4.0.4 on 2022-04-13 16:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(default=None, upload_to='blog/posts'),
            preserve_default=False,
        ),
    ]