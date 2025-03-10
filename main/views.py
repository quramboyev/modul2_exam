from django.shortcuts import render
from django.views.generic import ListView, TemplateView

def main_list_view(request):
    return render(request, 'main.html')