from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'teachers/teachers.html')

def teacher(request, teacher_id):
    return render(request, 'teachers/teacher.html', {'teacher_id':teacher_id})