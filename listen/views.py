import requests
import json
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
    dashboard_tracks = []

    for track in NATURE_TRACKS:
        url = "https://api.spotify.com/v1/tracks/{}".format(track)
        response = requests.get(
          url,
          headers={
            "Content-Type":"application/json",
            "Authorization":"Bearer BQAkoALbVnAioLjVipoUVXDpjIptIU5DX9UVOF749l7HJknLIU7b9whPtjho4h_Y519Nij7sVoW00_mok2K2jOhSypdOs5MHg8xD9w_GVD9s9K_7_khXuWBRnHQsTbKdrzHqkoLWpmgpiCoHbnJRhtmGoeAtrdGGRyv2wFC3OzomQXoeDNi2UxqDdoCZXo6cuLuk1hcoAUXE22VbByA2GGIqpmVbS1sHj4DbqKk6FwguR_eFyVs1K-y7tbxiIg7oc7Ll7itxvRgaYX24tOer69kvbMYmOnlIjbOtEY0"
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
