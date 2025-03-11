from django import forms
from .models import Questionnaire, ContestCategory

class QuestionnaireForm(forms.ModelForm):
    class Meta:
        model = Questionnaire
        fields = ['first_name', 'last_name', 'age', 'category', 'city', 'phone', 'gender', 'comment']
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите имя'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите фамилию'}),
            'age': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Введите возраст'}),
            'category': forms.Select(attrs={'class': 'form-select'}),
            'city': forms.Select(attrs={'class': 'form-select'}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите телефон'}),
            'gender': forms.Select(attrs={'class': 'form-select'}),
            'comment': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Введите комментарий'}),
        }
