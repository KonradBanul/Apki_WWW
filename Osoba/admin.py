from django.contrib import admin
from .models import Osoba, Stanowisko

# Register your models here.


class OsobaAdmin(admin.ModelAdmin):
    readonly_fields = ['data_dodania']
    list_display = ['imie', 'nazwisko', 'plec', 'stanowisko_id']
    list_filter = ('stanowisko', 'data_dodania')

    @admin.display(empty_value="nieznane")
    def stanowisko_id(self, obj):
        return f'{obj.stanowisko.nazwa} ({obj.stanowisko.id})'


class StanowiskoAdmin(admin.ModelAdmin):
    list_filter = 'nazwa'


admin.site.register(Osoba, OsobaAdmin)
admin.site.register(Stanowisko)
