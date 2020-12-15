from django import forms
from .models import Timetable

class uploadForm(forms.ModelForm):
    class Meta:
        model = Timetable
        fields = ('timetable',)
        labels = {
            'timetable': ''
        }
