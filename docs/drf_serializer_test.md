from Osoba.models import Osoba\
from Osoba.serializers import OsobaSerializer\
from rest_framework.renderers import JSONRenderer\
from rest_framework.parsers import JSONParser\
person = Osoba(imie='Adam', nazwisko='Bugajowski', plec=2)\
person.save()\
serializer = OsobaSerializer(person)\
serializer.data\
{'id': None, 'imie': 'Adam', 'nazwisko': 'Bugajowski', 'plec': 2, 'data_dodania': '2023-11-02'}\
content = JSONRenderer().render(serializer.data)\
content\
b'{"id":null,"imie":"Adam","nazwisko":"Bugajowski","plec":2,"data_dodania":"2023-11-02"}'\
import io\
stream = io.BytesIO(content)\
data = JSONParser().parse(stream)\
deserializer = OsobaSerializer(data=data)\
deserializer.is_valid()\
True\
deserializer.errors\
{}\
deserializer.fields\
{'id': IntegerField(read_only=True), 'imie': CharField(max_length=20), 'nazwisko': CharField(max_length=40), 'plec': IntegerField(), 'data_dodania': DateField()}\
deserializer.validated_data\
OrderedDict([('imie', 'Adam'), ('nazwisko', 'Bugajowski'), ('plec', 2), ('data_dodania', datetime.date(2023, 11, 2))])\
deserializer.save()\
deserializer.data
