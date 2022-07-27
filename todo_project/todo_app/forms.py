from django import forms
from .models import Task

class TaskForm(forms.ModelForm):
    class Meta :
        model = Task
        fields = ('name','description','complete')


        widgets = {
            'name' : forms.TextInput(attrs={'class':'form-control','placeholder':'Task'}),
            'description': forms.TextInput(attrs={'class': 'form-control','placeholder':'Description'}),
        }