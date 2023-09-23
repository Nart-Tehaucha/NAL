from django.shortcuts import render
from .models import Wordruler, Letter

def index(request):
    wordruler = Wordruler.objects.first()
    letters = wordruler.letters.all()
    all_letters = Letter.objects.all()
    
    context = {
        'letters': letters,
        'all_letters' : all_letters
    }
    return render(request, 'wordruler/wordruler.html', context)