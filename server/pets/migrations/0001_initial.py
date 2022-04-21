# Generated by Django 4.0.4 on 2022-04-13 20:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='PetType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('slug', models.SlugField(max_length=255, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Pet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('slug', models.SlugField(max_length=255, unique_for_date='publish')),
                ('publish', models.DateTimeField(default=django.utils.timezone.now)),
                ('type', models.CharField(choices=[('super', 'Süper'), ('platinum', 'Platinum'), ('gold', 'Gold'), ('silver', 'Gümüş')], default='super', max_length=50)),
                ('price', models.IntegerField()),
                ('animale_type', models.CharField(choices=[('dog', 'Dog')], default='dog', max_length=50)),
                ('age', models.IntegerField()),
                ('color', models.CharField(max_length=50)),
                ('height', models.IntegerField()),
                ('sex', models.CharField(choices=[('male', 'Male'), ('female', 'Female')], default='male', max_length=50)),
                ('breed', models.CharField(max_length=255)),
                ('city', models.CharField(choices=[('adana', 'Adana'), ('adiyaman', 'Adıyaman'), ('afyon', 'Afyon'), ('agri', 'Ağrı'), ('amasya', 'Amasya'), ('ankara', 'Ankara'), ('antalya', 'Antalya'), ('artvin', 'Artvin'), ('aydin', 'Aydın'), ('balikesir', 'Balıkesir'), ('bilecik', 'Bilecik'), ('bingol', 'Bingöl'), ('bitlis', 'Bitlis'), ('bolu', 'Bolu'), ('burdur', 'Burdur'), ('bursa', 'Bursa'), ('canakkale', 'Çanakkale'), ('cankiri', 'Çankırı'), ('corum', 'Çorum'), ('denizli', 'Denizli'), ('diyarbakir', 'Diyarbakır'), ('edirne', 'Edirne'), ('elazig', 'Elâzığ'), ('erzincan', 'Erzincan'), ('erzurum', 'Erzurum'), ('eskisehir', 'Eskişehir'), ('gaziantep', 'Gaziantep'), ('giresun', 'Giresun'), ('gumushane', 'Gümüşhane'), ('hakkari', 'Hakkâri'), ('hatay', 'Hatay'), ('isparta', 'Isparta'), ('mersin', 'Mersin'), ('istanbul', 'İstanbul'), ('izmir', 'İzmir'), ('kars', 'Kars'), ('kastamonu', 'Kastamonu'), ('kayseri', 'Kayseri'), ('kirklareli', 'Kırklareli'), ('kirsehir', 'Kırşehir'), ('kocaeli', 'Kocaeli'), ('konya', 'Konya'), ('kutahya', 'Kütahya'), ('malatya', 'Malatya'), ('manisa', 'Manisa'), ('kahramanmaras', 'Kahramanmaraş'), ('mardin', 'Mardin'), ('mugla', 'Muğla'), ('mus', 'Muş'), ('nevsehir', 'Nevşehir'), ('nigde', 'Niğde'), ('ordu', 'Ordu'), ('rize', 'Rize'), ('sakarya', 'Sakarya'), ('samsun', 'Samsun'), ('siirt', 'Siirt'), ('sinop', 'Sinop'), ('sivas', 'Sivas'), ('tekirdag', 'Tekirdağ'), ('tokat', 'Tokat'), ('trabzon', 'Trabzon'), ('tunceli', 'Tunceli'), ('sanliurfa', 'Şanlıurfa'), ('usak', 'Uşak'), ('van', 'Van'), ('yozgat', 'Yozgat'), ('zonguldak', 'Zonguldak'), ('aksaray', 'Aksaray'), ('bayburt', 'Bayburt'), ('karaman', 'Karaman'), ('kirikkale', 'Kırıkkale'), ('batman', 'Batman'), ('sirnak', 'Şırnak'), ('bartin', 'Bartın'), ('ardahan', 'Ardahan'), ('igdir', 'Iğdır'), ('yalova', 'Yalova'), ('karabuk', 'Karabük'), ('kilis', 'Kilis'), ('osmaniye', 'Osmaniye'), ('duzce', 'Düzce')], default='adana', max_length=50)),
                ('photo', models.ImageField(upload_to='pets/photos')),
                ('description', models.TextField()),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
