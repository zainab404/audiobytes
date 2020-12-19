from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    NATURE_TRACKS = [
      '1y7pIwI5ocoutzF66TIBk9',
      '7lakKIL70bIDxfj2umABVS',
      '1H7zXMcEx0PPW62NCSHbUV',
      '0ggwBO4x4XWDYHDnCpz3TJ',
      '0Q7oSvv9r8xRxqOJc3uWte'
    ]
    return render(request, 'listen/index.html', { 'nature_tracks': NATURE_TRACKS })

