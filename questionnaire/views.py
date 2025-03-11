from django.shortcuts import render, redirect
from .forms import QuestionnaireForm
from .models import Questionnaire

def questionnaire_view(request):
    if request.method == 'POST':
        form = QuestionnaireForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('anketa')
    else:
        form = QuestionnaireForm()
    return render(request, 'anketa.html', context={
        'form': form
    })

def contest_view(request):
    colors = ['#F5C24D', '#ED6059']
    return render(request, 'contest.html', context={
        'colors': colors
    })

