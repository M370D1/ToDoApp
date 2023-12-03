from django import forms
from .models import ToDoItem


class ItemAddForm(forms.ModelForm):
    class Meta:
        model = ToDoItem
        fields = ['content']
        labels = {
            'content': 'TO DO:',
        }
