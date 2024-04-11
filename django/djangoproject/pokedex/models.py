import uuid

from django.db import models

# Create your models here.

#Pokemon
#Type
#Abilites
#Users


class Pokemon(models.Model):
    Number = models.IntegerField(primary_key=True)
    Name = models.TextField()
    JapaneseName=models.TextField()
    Generation=models.PositiveIntegerField()
    LegendaryStatus=models.IntegerField()
    Classification = models.TextField()
    ImageLink = models.TextField()
    Height = models.IntegerField()
    Weight = models.IntegerField()
    Attack= models.IntegerField()
    Defense=models.IntegerField()
    SpAttack=models.IntegerField()
    SpDefense=models.IntegerField()
    Speed=models.IntegerField()
    HP=models.IntegerField()
    StatTotal=models.IntegerField()
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
    
class User(models.Model):
    userid=models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    username=models.TextField()
    ranking=models.ManyToManyField(Pokemon)

    def __str__(self):
        return f"<ID: {self.userid} Username: {self.username}>"