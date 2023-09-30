# views.py trong ứng dụng "english_course"
from django.contrib.auth import logout, login, authenticate
from django.shortcuts import render, get_object_or_404, redirect
from .models import Course, Lesson, Quiz, Student
from .forms import LessonForm, QuizForm, CombinedAuthenticationForm, RegistrationForm


def home(request):
    courses = Course.objects.all()
    return render(request, 'home.html', {'courses': courses})

def lesson_detail(request, lesson_id):
    lesson = get_object_or_404(Lesson, pk=lesson_id)

    if request.method == 'POST':
        form = LessonForm(request.POST, request.FILES, instance=lesson)
        if form.is_valid():
            form.save()
    else:
        form = LessonForm(instance=lesson)

    return render(request, 'lesson_detail.html', {'lesson': lesson, 'form': form})

def quiz_detail(request, lesson_id):
    lesson = get_object_or_404(Lesson, pk=lesson_id)
    quiz = Quiz.objects.get(lesson=lesson)

    if request.method == 'POST':
        form = QuizForm(request.POST, request.FILES, instance=quiz)
        if form.is_valid():
            form.save()
    else:
        form = QuizForm(instance=quiz)

    return render(request, 'quiz_detail.html', {'lesson': lesson, 'quiz': quiz, 'form': form})

def register_view(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            # Tạo một tài khoản người dùng Django
            user = form.save()

            # Lấy thông tin từ form
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')

            # Xác thực và đăng nhập người dùng
            user = authenticate(username=username, password=password)
            login(request, user)

            # Lưu thông tin Student
            student = Student(user=user, profile_image='', bio='', birth_date=None)
            student.save()

            return redirect('course_list')
    else:
        form = RegistrationForm()
    return render(request, 'register.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = CombinedAuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('course_list')
    else:
        form = CombinedAuthenticationForm()
    return render(request, 'login.html', {'form': form})
def logout_view(request):
    logout(request)
    return redirect('home')