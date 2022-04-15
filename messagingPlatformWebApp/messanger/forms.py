from django import forms
from .models import Message
from datetime import datetime

class MsgForm(forms.ModelForm):
    class Meta:
        msg = Message
        fields = ["msgText"]
