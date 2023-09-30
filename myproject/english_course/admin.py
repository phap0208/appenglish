
from django.contrib import admin
from .models import Course,Lesson,Quiz,Student

admin.site.register(Lesson)
admin.site.register(Course)
admin.site.register(Quiz)
admin.site.register(Student)