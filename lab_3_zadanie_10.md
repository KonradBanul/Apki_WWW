Osoba.objects.all(),
Osoba.objects.get(id=3),
Osoba.objects.filter(nazwisko__startswith='B'),
Stanowisko.objects.filter(id__in=Osoba.objects.values_list('stanowisko')),
Stanowisko.objects.order_by('-nazwa'),
Osoba.objects.create(imie='Anna', nazwisko='Bielki', plec=1, stanowisko_id=Stanowisko.objects.first().id)









