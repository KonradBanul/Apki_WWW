from django.db import models

# Create your models here.


class Stanowisko(models.Model):
    nazwa = models.CharField(max_length=60)
    opis = models.TextField(blank=True, null=True)

    def __str__(self):
        return f'{self.nazwa}'


class Osoba(models.Model):
    class Plec(models.IntegerChoices):
        KOBIETA = 1
        MEZCZYNZA = 2
        INNE = 3
    imie = models.CharField(max_length=20)
    nazwisko = models.CharField(max_length=40)
    plec = models.IntegerField(choices=Plec.choices)
    stanowisko = models.ForeignKey(Stanowisko, on_delete=models.CASCADE)
    data_dodania = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'{self.imie} {self.nazwisko}'

    class Meta:
        ordering = ["nazwisko"]
