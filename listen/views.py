from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def dashboard(request):
    NATURE_TRACKS = [
      '1y7pIwI5ocoutzF66TIBk9',
      '7lakKIL70bIDxfj2umABVS',
      '1H7zXMcEx0PPW62NCSHbUV',
      '0ggwBO4x4XWDYHDnCpz3TJ',
      '0Q7oSvv9r8xRxqOJc3uWte'
    ]
    return render(request, 'listen/dashboard.html', { 'nature_tracks': NATURE_TRACKS })

def nature(request):
    NATURE_TRACKS = [
      '1y7pIwI5ocoutzF66TIBk9',
      '7lakKIL70bIDxfj2umABVS',
      '1H7zXMcEx0PPW62NCSHbUV',
      '0ggwBO4x4XWDYHDnCpz3TJ',
      '0Q7oSvv9r8xRxqOJc3uWte'
    ]
    return render(request, 'listen/nature.html', { 'nature_tracks': NATURE_TRACKS })

def office(request):
    NATURE_TRACKS = [
      '1FlbLSX8Fat3z4jLQkTAvf',
      '635hEgWYUnjbvQr0YTxzyj',
      '43xZo7aQ7UxTIacmAWx7Rw',
      '7lzpN2K7zbaq1iYCElsnMe'
    ]
    return render(request, 'listen/office.html', { 'nature_tracks': NATURE_TRACKS })

def public(request):
    NATURE_TRACKS = [
      '1y7pIwI5ocoutzF66TIBk9',
      '7lakKIL70bIDxfj2umABVS',
      '1H7zXMcEx0PPW62NCSHbUV',
      '0ggwBO4x4XWDYHDnCpz3TJ',
      '0Q7oSvv9r8xRxqOJc3uWte'
    ]
    return render(request, 'listen/public.html', { 'nature_tracks': NATURE_TRACKS })
