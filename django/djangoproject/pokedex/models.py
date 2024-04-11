import uuid

from django.db import models

# Create your models here.

#Pokemon
#Type
#Abilites
#Users


class Pokemon(models.Model):
    number = models.IntegerField(primary_key=True)
    name = models.TextField()

    class Meta:
        verbose_name_plural = "Pokemon"

    def __str__(self):
        return f"<ID: {self.number} Name: {self.name} Types: >"
    
class Type(models):
    Name = models.TextField(primary_key=True)
    Effective = models.ManyToManyField("self")
    Weakness = models.ManyToManyField("self")
    Pokemon = models.ManyToManyRel(Pokemon)
    def __str__(self):
        return f"<ID: {self.number} Name: {self.name} Types: >"
    
class Type(models):
    Name = models.TextField(primary_key=True)
    Effective = models.ManyToManyField("self")
    Weakness = models.ManyToManyField("self")
    Pokemon = models.ManyToManyRel(Pokemon)

class Ability(models.Model):
    abilityID = models.IntegerField(primary_key=True)
    name = models.TextField()
    affect = models.TextField()

    class Meta:
        verbose_name_plural = "Pokemon"
        
    def __str__(self):
        return f"<ID: {self.abilityID} Name: {self.name} Desc: {self.affect}>"