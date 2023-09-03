# from django.shortcuts import render
#
# def index(request):
#     """money form"""
#     return render(request, 'webapp/index.html')

from django.shortcuts import render
from .forms import PaymentForm

def index(request):
    if request.method == 'POST':
        form = PaymentForm(request.POST)
        if form.is_valid():
            # Обработка данных формы
            form.save()  # Сохранение данных в базе данных
            # Добавьте здесь свою логику для обработки платежей и валидации карты

    else:
        form = PaymentForm()

    return render(request, 'webapp/index.html', {'form': form})
