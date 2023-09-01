from django.shortcuts import render

def index(request):
    """money form"""
    return render(request, 'webapp/index.html')
