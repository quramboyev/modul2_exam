from string import digits
from django import forms
from .models import Questionnaire, ContestCategory

class QuestionnaireForm(forms.ModelForm):
    class Meta:
        model = Questionnaire
        fields = '__all__'
        widgets = {
            'first_name': forms.TextInput(attrs={
                'placeholder': 'Имя:'
            }),
            'last_name': forms.TextInput(attrs={
                'placeholder': 'Фамилия:'
            }),
            'age': forms.TextInput(attrs={
                'placeholder': 'Лет:'
            }),
            'city': forms.Select(attrs={
                'class': 'form-control'
            }),
            'phone': forms.TextInput(attrs={
                'placeholder': 'Телефон:'
                }),  
            'gender': forms.Select(attrs={
                'placeholder': 'Пол'
            }),
            'comment': forms.Textarea(attrs={
                'placeholder': 'Ваш коммент'
            })
        }