
from django import forms
from Messages.models import Message
class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['text']