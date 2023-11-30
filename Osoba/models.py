from django.db import models
from django.utils import timezone
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User

# Create your models here.


def validate_letters(value):
    if not value.isalpha():
        raise ValidationError("Nazwa może zawierać tylko litery.")


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
    data_dodania = models.DateField(default=timezone.now)
    wlasciciel = models.ForeignKey(User, related_name='persons', on_delete=models.CASCADE, default=1)

    def clean(self):
        if self.data_dodania > timezone.now():
            raise ValidationError("Data dodania nie może być z przyszłości.")

    def __str__(self):
        return f'{self.imie} {self.nazwisko}'

    class Meta:
        ordering = ["nazwisko"]
