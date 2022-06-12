CITIES = (
	('adana', 'Adana'), 
	('adiyaman', 'Adıyaman'), 
	('afyon', 'Afyon'), 
	('agri', 'Ağrı'), 
	('amasya', 'Amasya'), 
	('ankara', 'Ankara'), 
	('antalya', 'Antalya'), 
	('artvin', 'Artvin'), 
	('aydin', 'Aydın'), 
	('balikesir', 'Balıkesir'), 
	('bilecik', 'Bilecik'), 
	('bingol', 'Bingöl'), 
	('bitlis', 'Bitlis'), 
	('bolu', 'Bolu'), 
	('burdur', 'Burdur'), 
	('bursa', 'Bursa'), 
	('canakkale', 'Çanakkale'), 
	('cankiri', 'Çankırı'), 
	('corum', 'Çorum'), 
	('denizli', 'Denizli'), 
	('diyarbakir', 'Diyarbakır'), 
	('edirne', 'Edirne'), 
	('elazig', 'Elâzığ'), 
	('erzincan', 'Erzincan'), 
	('erzurum', 'Erzurum'), 
	('eskisehir', 'Eskişehir'), 
	('gaziantep', 'Gaziantep'), 
	('giresun', 'Giresun'), 
	('gumushane', 'Gümüşhane'), 
	('hakkari', 'Hakkâri'), 
	('hatay', 'Hatay'), 
	('isparta', 'Isparta'), 
	('mersin', 'Mersin'), 
	('istanbul', 'İstanbul'), 
	('izmir', 'İzmir'), 
	('kars', 'Kars'), 
	('kastamonu', 'Kastamonu'), 
	('kayseri', 'Kayseri'), 
	('kirklareli', 'Kırklareli'), 
	('kirsehir', 'Kırşehir'), 
	('kocaeli', 'Kocaeli'), 
	('konya', 'Konya'), 
	('kutahya', 'Kütahya'), 
	('malatya', 'Malatya'), 
	('manisa', 'Manisa'), 
	('kahramanmaras', 'Kahramanmaraş'), 
	('mardin', 'Mardin'), 
	('mugla', 'Muğla'), 
	('mus', 'Muş'), 
	('nevsehir', 'Nevşehir'), 
	('nigde', 'Niğde'), 
	('ordu', 'Ordu'), 
	('rize', 'Rize'), 
	('sakarya', 'Sakarya'), 
	('samsun', 'Samsun'), 
	('siirt', 'Siirt'), 
	('sinop', 'Sinop'), 
	('sivas', 'Sivas'), 
	('tekirdag', 'Tekirdağ'), 
	('tokat', 'Tokat'), 
	('trabzon', 'Trabzon'), 
	('tunceli', 'Tunceli'), 
	('sanliurfa', 'Şanlıurfa'), 
	('usak', 'Uşak'), 
	('van', 'Van'), 
	('yozgat', 'Yozgat'), 
	('zonguldak', 'Zonguldak'), 
	('aksaray', 'Aksaray'), 
	('bayburt', 'Bayburt'), 
	('karaman', 'Karaman'), 
	('kirikkale', 'Kırıkkale'), 
	('batman', 'Batman'), 
	('sirnak', 'Şırnak'), 
	('bartin', 'Bartın'), 
	('ardahan', 'Ardahan'), 
	('igdir', 'Iğdır'), 
	('yalova', 'Yalova'), 
	('karabuk', 'Karabük'), 
	('kilis', 'Kilis'), 
	('osmaniye', 'Osmaniye'), 
	('duzce', 'Düzce')
)

# PET_HIERARCHY 


ADVERT_CHOICES = (
	('normal','Sahiplenme'),
	# ('super','Süper'),
	# ('platinum','Platinum'),
	('gold','Gold'),
	# ('silver','Gümüş'),
	('marry','Eş Bul'),
	('lost','Kayıp')
)

ADVERT_NAMES = { i[0]:i[1] for i in ADVERT_CHOICES }
ADVERT_TYPES = ( item[0] for item in ADVERT_CHOICES )

SPECIAL_ADVERT_TYPES = ['gold']
PUBLIC_ADVERT_TYPES = list(filter(lambda x: x not in SPECIAL_ADVERT_TYPES,ADVERT_TYPES))

ADVERT_COLORS = {
	'super': 'red',
	'platinum':'blue',
	'gold':'gold',
	'silver':'silver',
}

COLORED_ADVERT_TYPES = [ i for i in ADVERT_COLORS.keys() ]

SEX_CHOICES = (
	('male','Erkek'),
	('female','Dişi')
)

SHOP_DATA = {
	'CONTACT_EMAIL':'desktek.sahiplensene@outlook.com.tr'
}
