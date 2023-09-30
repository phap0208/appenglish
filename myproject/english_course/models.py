# models.py trong ứng dụng "english_course"
from django.db import models
from django.contrib.auth.models import User

class Course(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return self.title

class Lesson(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    content = models.TextField()

    def __str__(self):
        return self.title

class Quiz(models.Model):
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    questions = models.TextField()

    def __str__(self):
        return self.title
# Import model User từ Django

class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)  # Liên kết với model User và xử lý xóa thông qua CASCADE
    profile_image = models.ImageField(upload_to='profile_images/')  # Ảnh đại diện
    bio = models.TextField()  # Mô tả cá nhân
    birth_date = models.DateField()  # Ngày sinh

    def __str__(self):
        return self.user.username
