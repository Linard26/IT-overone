from .models import Task
from django.forms import ModelForm, TextInput, Textarea

class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ["title","task"]
        widgets = {"title": TextInput(attrs={'class':'form-control', 'placeholder':'Введите название'}),
                   "task": Textarea(attrs={'class': 'p-4 mb-3 bg-body-tertiary rounded', 'placeholder': 'Введите задачу'}) }
