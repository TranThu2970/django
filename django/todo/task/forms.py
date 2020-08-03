from django import forms
from django.forms import ModelForm
from .models import * 

class TaskForm(forms.ModelForm):
    #Hiển thị placeholder
    title = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Add new task....'}))
    
    class Meta:
        model = Task
        fields = '__all__'