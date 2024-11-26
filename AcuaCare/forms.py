from django import forms
from accounts.models import Feedback

class FormularioChatBot(forms.Form):
    texto = forms.CharField(widget=forms.TextInput(attrs={'class': 'TextInput-Question'}))

class FormularioWeather(forms.Form):
    texto = forms.CharField(widget=forms.TextInput)


class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = '__all__'

    
