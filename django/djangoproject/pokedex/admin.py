from django.contrib import admin

# Register your models here.
from .models import Student, Room, Course

admin.site.register(Student)
admin.site.register(Room)
admin.site.register(Course)