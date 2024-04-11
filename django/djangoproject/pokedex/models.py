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
    classification = models.TextField()
    image_link = models.TextField()
    height = models.IntegerField()
    weight = models.IntegerField()
    PrevEvolution = models.ForeignKey("self")

    class Meta:
        verbose_name_plural = "Pokemon"

    def __str__(self):
        return f"<ID: {self.number} Name: {self.name} Types: >"
    
class EleType(models.Model):
    Name = models.TextField(primary_key=True)
    Effective = models.ManyToManyField("self")
    Weakness = models.ManyToManyField("self")
    Pokemon = models.ManyToManyField(Pokemon)
    def __str__(self):
        return f"<name: {self.Name}>"

class Ability(models.Model):
    abilityID = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.TextField()
    affect = models.TextField()

    class Meta:
        verbose_name_plural = "Abilities"
        
    def __str__(self):
        return f"<ID: {self.abilityID} Name: {self.name} Desc: {self.affect}>"