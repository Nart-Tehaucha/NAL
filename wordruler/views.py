from django.shortcuts import render
from .models import Wordruler, Letter
from students.models import Student
from teachers.models import Teacher

def index(request):
    wordruler = Wordruler.objects.first()
    letters = wordruler.letters.all()
    all_letters = Letter.objects.all()
    
    context = {
        'letters': letters,
        'all_letters' : all_letters
    }
    return render(request, 'wordruler/wordruler.html', context)

def wr_students(request):
    students = Student.objects.all()
    
    context = {
        'students': students
    }
    return render(request, 'wordruler/student_grid.html', context)

def wr_student(request, student_id):
    curr_student = Student.objects.get(pk=student_id)
    curr_teacher = Teacher.objects.first() # Hard coded, change later

    wordruler_by_student, wr_created = Wordruler.objects.get_or_create(
        student = curr_student,
        teacher = curr_teacher
    )

    if wr_created:
        print(f"Created new WR for: {curr_student.name}")

    letters = wordruler_by_student.letters.all()
    all_letters = Letter.objects.all()
    
    context = {
        'student': curr_student,
        'wordruler': wordruler_by_student,
        'letters': letters,
        'all_letters' : all_letters
    }
    return render(request, 'wordruler/wordruler.html', context)