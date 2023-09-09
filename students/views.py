from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'students/students.html')

def student(request, student_id):
    return render(request, 'students/student.html', {'student_id':student_id})