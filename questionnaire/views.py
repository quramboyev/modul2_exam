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

