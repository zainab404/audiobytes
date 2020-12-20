import requests
import json
from django.shortcuts import render
from django.http import HttpResponse

TOKEN = "BQB9B6m9ukPvNbXd2j9H0O0FXa1vEPyEfw71y8D5xGdpEQ22Di4dk9hWKXVd--oHBEMpBf27gHwTpdIdDPBEdgDRDEhu3l9l8bxxRWBapUxckn8KVpyQcdbKcjK9HLn0wrUT9KJT-D69yjW-oxHcYT0C__r620CenCM9wxydBs1R6QO638Q3FnT1IF2jK5uWoyVhNRQNNM7X76NVr1JYmU_gWo4FBIrTxgfmzJEf_lO7wZk1ZifvmxGBVAK3Syb4V75MYDeVf1bqSttVeotA8JP2ldEoZc85eMsCJDI"

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
