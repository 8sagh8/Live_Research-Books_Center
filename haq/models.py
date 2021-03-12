from django.db import models
from django.db.models.deletion import CASCADE

# Create your models here.

    # Authorized Persons
class Authorized_Person(models.Model):
    auth_name = models.CharField(max_length=10)

    def __str__(self):
        return self.auth_name

 # research Topics
class Topic(models.Model):
    _topic = models.CharField(max_length=50)

    def __str__(self):
        return self._topic

# Person either a reportor, writer or well known personality
class Person(models.Model):
    _p_name = models.CharField(max_length = 40)
    _birth_year = models.CharField(max_length=4)
    _death_year = models.CharField(max_length=4)

    def __str__(self):
        if eval(self._birth_year) > 0 and eval(self._death_year) > 0:
                return self._p_name + ' birth: ' + self._birth_year + ' & death: ' + self._death_year
        elif eval(self._birth_year) < 1 and eval(self._death_year) > 0:
            return self._p_name + ' & death: ' + self._death_year
        elif eval(self._birth_year) > 0 and eval(self._death_year) < 1:
            return self._p_name + ' birth: ' + self._birth_year
        else:
            return self._p_name

    def __str__(self):
        return self._p_name

# Category models here.
class Category(models.Model):
    _category = models.CharField(max_length=22)

    def __str__(self):
        return self._category

# Language models here.
class Language(models.Model):
    _language = models.CharField(max_length=7)

    def __str__(self):
        return self._language

# Need models here.
class Need(models.Model):
    _need = models.CharField(max_length=9)

    def __str__(self):
        return self._need


# Religion / Sect models here.
class Religion(models.Model):
    _sect = models.CharField(max_length=20)

    def __str__(self):
        return self._sect


# Status models here.
class Status(models.Model):
    _status = models.CharField(max_length=16)

    def __str__(self):
        return self._status


# Book models here.
class Book(models.Model):
    name = models.CharField(max_length=50)
    author = models.ForeignKey(Person, on_delete=models.CASCADE)
    sect = models.ForeignKey(Religion, on_delete=models.CASCADE)
    cat = models.ForeignKey(Category, on_delete=models.CASCADE)
    status = models.ForeignKey(Status, on_delete=models.CASCADE)
    need = models.ForeignKey(Need, on_delete=models.CASCADE)
    lang = models.ForeignKey(Language, on_delete=models.CASCADE)
    data_status = models.CharField(max_length=1, default='P')

    def __str__(self):
        return self.name.capitalize() + ' sect: ' + str(self.sect) + ' & language: ' + str(self.lang)

#####################################
########### IMPROVE ABOVE #############
#####################################
# Reference Model
class Reference(models.Model):
    subject = models.ForeignKey(Topic, on_delete=models.CASCADE)
    speaker = models.ForeignKey(Person, related_name="speaker", on_delete=models.CASCADE)
    personFor = models.ForeignKey(Person, related_name="personFor", on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    vol_para = models.IntegerField()
    page_chapter = models.IntegerField()
    hadees_verse = models.IntegerField()
    description = models.TextField(max_length=500, null=True)

    def __str__(self):
        return str(self.subject) + ' ' + self.description