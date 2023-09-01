from django.shortcuts import render

def index(request):
    """money form"""
    return render(request, 'main/index.html')
