import uuid

from django.db import models

# Create your models here.

#Pokemon
#Type
#Abilites
#Users


class EleType(models.Model):
    name = models.TextField(primary_key=True)
    
    effective = models.ManyToManyField("self", related_name='+', blank=True, symmetrical=False)
    weakness = models.ManyToManyField("self", blank=True, symmetrical=False)
    no_effect_on = models.ManyToManyField("self",  related_name="+", blank=True, symmetrical=False)

    def __str__(self):
        return f"<name: {self.name}>"

class Ability(models.Model):
    abilityID = models.IntegerField(primary_key=True)
    name = models.TextField(db_index=True)
    affect = models.TextField()

    class Meta:
        verbose_name_plural = "Abilities"
        
    def __str__(self):
        return f"<ID: {self.abilityID} Name: {self.name} Desc: {self.affect}>"

class Pokemon(models.Model):
    number = models.IntegerField(primary_key=True)
    name = models.TextField()
    classification = models.TextField()
    primary_image = models.ForeignKey("PokemonImage", on_delete=models.CASCADE, related_name="primary_image_of", null=True, blank=True)
    height = models.FloatField()
    weight = models.FloatField()
    prevevolution = models.ForeignKey("self", on_delete=models.CASCADE, null=True, blank=True, related_name="postevolutions")
    type = models.ManyToManyField(EleType)
    abilities = models.ManyToManyField(Ability)

    class Meta:
        verbose_name_plural = "Pokemon"

    def __str__(self):
        return f"<ID: {self.number} Name: {self.name} Types: >"

class PokemonImage(models.Model):
    image = models.ImageField(upload_to="pokeimages")
    description = models.CharField(max_length=64)
    pokemon = models.ForeignKey(Pokemon, on_delete=models.CASCADE,db_index=True)

    class Meta:
        unique_together = ('pokemon', 'description',)
    
class User(models.Model):
    userid=models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    username=models.TextField()
    favorites=models.ManyToManyField(Pokemon)

    def __str__(self):
        return f"<ID: {self.userid} Username: {self.username}>" 