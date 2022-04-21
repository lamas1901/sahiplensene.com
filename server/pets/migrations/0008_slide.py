# Generated by Django 4.0.4 on 2022-04-17 18:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pets', '0007_rename_type_pet_advert_type'),
    ]

    operations = [
        migrations.CreateModel(
            name='Slide',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('heading_pre', models.CharField(max_length=50)),
                ('heading', models.CharField(max_length=50)),
                ('heading_sub', models.CharField(max_length=100)),
                ('button_show', models.BooleanField(default=False)),
                ('button_text', models.CharField(max_length=50)),
                ('button_link', models.TextField()),
                ('image', models.ImageField(upload_to='pets/slider')),
            ],
        ),
    ]