# forms.py trong ứng dụng "english_course"
from django import forms
from .models import Lesson, Quiz, Student
from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User

class LessonForm(forms.ModelForm):
    class Meta:
        model = Lesson
        fields = ['course', 'title', 'content']

class QuizForm(forms.ModelForm):
    class Meta:
        model = Quiz
        fields = ['lesson', 'title', 'questions']


class CombinedAuthenticationForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ('username', 'password')

class RegistrationForm(UserCreationForm):
    # email = forms.EmailField(required=True)
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
class StudentInfoForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['profile_image', 'bio', 'birth_date']