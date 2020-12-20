import requests
import json
from django.shortcuts import render
from django.http import HttpResponse

TOKEN = "BQAzK6BUaAb1PauN2LYzQNaIqC_HPWPY7XLcd8f7m_mVtklEqly_d82uFXWKvPmsDJvzl87jm6eSwOmJrej9l25mNcKaMDoBmmrps4SqmT88FzrYqLtW1lREwaUrKgkWZvXpWtOzrUYo4pn6Oh8M6RsyLxcMIRvrqvBdlJe37lKAhvMwaQtKWt1vqqG0DxhVvsF3PNhtEEXQ10GA32yPpU-hNc7Fqa6_GvI8Ou-9etNvRz9yk2vYoDnvEYGP5X8xDcQHbqkyuU2A_YE3BuPu0VQY4RjqsNhyz0FCi24"

# Create your views here.
def dashboard(request):
    NATURE_TRACKS = [
      '1y7pIwI5ocoutzF66TIBk9',
      '7lakKIL70bIDxfj2umABVS',
      '1H7zXMcEx0PPW62NCSHbUV',
      '0ggwBO4x4XWDYHDnCpz3TJ',
      '0Q7oSvv9r8xRxqOJc3uWte'
    ]
    dashboard_tracks = []

    for track in NATURE_TRACKS:
        url = "https://api.spotify.com/v1/tracks/{}".format(track)
        response = requests.get(
          url,
          headers={
            "Content-Type":"application/json",
            "Authorization":"Bearer "+TOKEN
          }
        )
        dashboard_tracks.append(response.json())
    return render(request, 'listen/dashboard.html', { 'nature_tracks': dashboard_tracks})

def nature(request):
    NATURE_TRACKS = [
      '1y7pIwI5ocoutzF66TIBk9',
      '7lakKIL70bIDxfj2umABVS',
      '1H7zXMcEx0PPW62NCSHbUV',
      '0ggwBO4x4XWDYHDnCpz3TJ',
      '0Q7oSvv9r8xRxqOJc3uWte'
    ]

    dashboard_tracks = []

    for track in NATURE_TRACKS:
        url = "https://api.spotify.com/v1/tracks/{}".format(track)
        response = requests.get(
          url,
          headers={
            "Content-Type":"application/json",
            "Authorization":"Bearer "+TOKEN
          }
        )
        dashboard_tracks.append(response.json())
    return render(request, 'listen/nature.html', { 'nature_tracks': dashboard_tracks})

def office(request):
    NATURE_TRACKS = [
      '1FlbLSX8Fat3z4jLQkTAvf',
      '635hEgWYUnjbvQr0YTxzyj',
      '43xZo7aQ7UxTIacmAWx7Rw',
      '7lzpN2K7zbaq1iYCElsnMe'
    ]
    dashboard_tracks = []

    for track in NATURE_TRACKS:
        url = "https://api.spotify.com/v1/tracks/{}".format(track)
        response = requests.get(
          url,
          headers={
            "Content-Type":"application/json",
            "Authorization":"Bearer "+TOKEN
          }
        )
        dashboard_tracks.append(response.json())
    return render(request, 'listen/office.html', { 'nature_tracks': dashboard_tracks})

def public(request):
    NATURE_TRACKS = [
      '7gT0l4iDWrguvyyvwIOCi1',
      '2yY7B5cRxjoNymsaJjqMua',
      '2Fz11dL4CfITHw0GDt91bG',
      '26sy9DDRDqvJkvYxmKLhz0',
      '26sy9DDRDqvJkvYxmKLhz0',
      '26sy9DDRDqvJkvYxmKLhz0',
    ]

    dashboard_tracks = []

    for track in NATURE_TRACKS:
        url = "https://api.spotify.com/v1/tracks/{}".format(track)
        response = requests.get(
          url,
          headers={
            "Content-Type":"application/json",
            "Authorization":"Bearer "+TOKEN
          }
        )
        dashboard_tracks.append(response.json())

    return render(request, 'listen/public.html', { 'nature_tracks': dashboard_tracks})
