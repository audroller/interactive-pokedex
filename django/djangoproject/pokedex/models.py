import uuid

from django.db import models

# Create your models here.

#Pokemon
#Type
#Abilites
#Users

class EleType(models.Model):
    Name = models.TextField(primary_key=True)
    Effective = models.ManyToManyField("self")
    Weakness = models.ManyToManyField("self")
    
    def __str__(self):
        return f"<name: {self.Name}>"

class Ability(models.Model):
    abilityID = models.IntegerField(primary_key=True)
    name = models.TextField()
    affect = models.TextField()

    class Meta:
        verbose_name_plural = "Abilities"
        
    def __str__(self):
        return f"<ID: {self.abilityID} Name: {self.name} Desc: {self.affect}>"

class Pokemon(models.Model):
    number = models.IntegerField(primary_key=True)
    name = models.TextField()
    classification = models.TextField()
    image_link = models.TextField()
    height = models.IntegerField()
    weight = models.IntegerField()
    PrevEvolution = models.ForeignKey("self", on_delete=models.CASCADE)
    Type = models.ManyToManyField(EleType)
    Abilities = models.ManyToManyField(Ability)

    class Meta:
        verbose_name_plural = "Pokemon"

    def __str__(self):
        return f"<ID: {self.number} Name: {self.name} Types: >"
    
    
class User(models.Model):
    userid=models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    username=models.TextField()
    favorites=models.ManyToManyField(Pokemon)

    def __str__(self):
        return f"<ID: {self.userid} Username: {self.username}>" 