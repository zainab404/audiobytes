from django import forms

class AudioFeedbackForm(forms.Form):
    name = forms.CharField()
    feedback = forms.CharField(widget=forms.Textarea)
