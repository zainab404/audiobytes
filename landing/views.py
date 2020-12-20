from django.shortcuts import render
from .models import AudioFeedback

# Create your views here.
def index(request):
    return render(request, 'landing/index.html')

def feedback(request):

    if request.method == 'POST':
        data = request.POST
        feedback = AudioFeedback(name=data['name'], feedback=data['message'])
        feedback.save()

        return index(request)

    return render(request, 'landing/feedback.html')