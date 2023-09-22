from django.shortcuts import render


from .models import Lesson

def index(request):
    lessons = Lesson.objects.all()
    
    context = {
        'lessons': lessons
    }
    return render(request, 'lessons/lessons.html', context)

def lesson(request, lesson_id):
    lesson_by_id = Lesson.objects.get(pk= lesson_id)

    context = {
    'lesson': lesson_by_id
    }
    return render(request, 'lessons/lesson.html', context)