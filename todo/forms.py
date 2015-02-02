import os
from django import forms
from settings import MEDIA_ROOT


class TaskForm(forms.Form):
    first_name = forms.CharField(max_length=200)
    last_name = forms.CharField(max_length=200)
    #task_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    #task_desc = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control'}))
    #priority = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    #task_state = forms.EmailField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Email'}))
    #due_date = forms.DateField(widget=forms.DateField(attrs={'class':'form-control'}))
