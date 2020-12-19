import requests
import json
from django.shortcuts import render
from django.http import HttpResponse

TOKEN = "BQD0G2MDxEneP34RN74X-ZJyd0eQwCAXUG9wbG12omnrWoApdJmmdM7G4j3EzAEb57jj-08GxJOsT9GwPBBnDkIzmIIjPLmWIh9cqsadArIjwHHr_VdN3z_yUVspPiHy8BVXdyU3w4gvH0-3jRE7vW1aGB_iLiESUqmpA_6zh-YT28_nQnnnMmw42SXk4HQ09vwHdU5BoEisyW1nf4-SdswZl4mgH2azVZQ35n0oo_gJaPljMNQYT-QWeRX_-de03xwNZzVbPR5nsxUUYBzn9_VyxwCMqG9Q0Saw1Lo"

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
