from django.shortcuts import render
from django.http import HttpResponse

from lessons.models import Lesson

# Create your views here.
def index(request):
    lessons = Lesson.objects.all()
    
    context = {
        'lessons': lessons
    }
    return render(request, 'pages/index.html', context)

def about(request):
    return render(request, 'pages/about.html')