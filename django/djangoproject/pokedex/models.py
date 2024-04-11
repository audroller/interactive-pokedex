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
<<<<<<< Updated upstream
=======
    
class Type(models):
    Name = models.TextField(primary_key=True)
    Effective = models.ManyToManyField("self")
    Weakness = models.ManyToManyField("self")
    Pokemon = models.ManyToManyRel(Pokemon)

'''
class Room(models.Model):
    number = models.TextField(primary_key=True)
    capacity = models.IntegerField()
>>>>>>> Stashed changes

class Ability(models.Model):
    abilityID = models.IntegerField(primary_key=True)
    name = models.TextField()
    affect = models.TextField()
    def __str__(self):
        return f"<AbilityID: {self.abilityID} Name: {self.name} Affect: {self.affect}>"

'''
class Course(models.Model):
    co_number = models.TextField(primary_key=True)
    title = models.TextField()
    room = models.ForeignKey(Room, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "Courses"

    def __str__(self):
        return f"<Course {self.co_number}, {self.title} is in {self.room}>"

class Student(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    stud_id = models.IntegerField()
    name = models.CharField(max_length=100)
    enrolled = models.ManyToManyField(Course, verbose_name="enrollments")

    def __str__(self):
        return "<Profile id={} name={} >".format(
            self.stud_id, self.name,
        )
'''
