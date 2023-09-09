from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'lessons/lessons.html')

def lesson(request, lesson_id):
    return render(request, 'lessons/lesson.html', {'lesson_id':lesson_id})