import uuid

from django.db import models

# Create your models here.

#Student
#Course
#Room
#Enrollment


class Room(models.Model):
    number = models.TextField(primary_key=True)
    capacity = models.IntegerField()

    def __str__(self):
        return f"<Room {self.number} can hold {self.capacity} people>"


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
