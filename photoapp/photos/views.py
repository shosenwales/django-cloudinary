from django.shortcuts import render
from .models import photos

def index(request):
    photo = photos.objects.all()
    ctx = {'photo':photo}
    return render(request, 'index.html', ctx)
