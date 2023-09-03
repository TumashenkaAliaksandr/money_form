from django.shortcuts import render
from .forms import PaymentForm  # Импортируйте вашу форму PaymentForm
from .models import Payment  # Импортируйте модель Payment

def index(request):
    if request.method == 'POST':
        form = PaymentForm(request.POST)
        if form.is_valid():
            # Обработка данных формы
            owner = form.cleaned_data['owner']
            card_number = form.cleaned_data['card_number']
            cvv = form.cleaned_data['cvv']
            expiration_date_month = form.cleaned_data['expiration_date_month']
            expiration_date_year = form.cleaned_data['expiration_date_year']

            # Ваша логика для обработки платежей и валидации карты
            # Здесь вы можете использовать платежные шлюзы (например, Stripe, PayPal) или
            # библиотеки для валидации кредитных карт.

            # Пример валидации номера кредитной карты (логика может быть более сложной):
            if not is_valid_credit_card(card_number):
                return render(request, 'webapp/payment_error.html', {'form': form})

            # Создание и сохранение экземпляра модели Payment
            payment = Payment(
                owner=owner,
                card_number=card_number,
                cvv=cvv,
                expiration_date_month=expiration_date_month,
                expiration_date_year=expiration_date_year
            )
            payment.save()

            # После успешного платежа или обработки, вы можете перенаправить пользователя на другую страницу или
            # отобразить сообщение об успешном платеже.

            return render(request, 'webapp/payment_success.html', {'form': form})

    else:
        form = PaymentForm()

    return render(request, 'webapp/index.html', {'form': form})
