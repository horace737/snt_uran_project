from django.shortcuts import render

# Create your views here.

from django.shortcuts import render


def get_forum(request):
    return render(request, 'forum/forum.html',)
