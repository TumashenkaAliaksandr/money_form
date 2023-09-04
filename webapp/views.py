import stripe
from django.shortcuts import render
from .forms import PaymentForm
from .models import Payment
from stripe.error import StripeError


# Определите собственное исключение для ошибок Stripe
class StripePaymentError(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)


def index(request):
    if request.method == 'POST':
        form = PaymentForm(request.POST)
        if form.is_valid():
            owner = form.cleaned_data['owner']
            card_number = form.cleaned_data['card_number']
            cvv = form.cleaned_data['cvv']
            expiration_date_month = form.cleaned_data['expiration_date_month']
            expiration_date_year = form.cleaned_data['expiration_date_year']

            try:
                stripe.api_key = 'YOUR_STRIPE_SECRET_KEY'
                token = stripe.Token.create(
                    card={
                        "number": card_number,
                        "exp_month": expiration_date_month,
                        "exp_year": expiration_date_year,
                        "cvc": cvv,
                    },
                )

                charge = stripe.Charge.create(
                    amount=1000,
                    currency="usd",
                    source=token,
                    description=f"Payment by {owner}",
                )

                if charge.status == "succeeded":
                    payment = Payment(
                        owner=owner,
                        card_number=card_number,
                        cvv=cvv,
                        expiration_date_month=expiration_date_month,
                        expiration_date_year=expiration_date_year,
                    )
                    payment.save()
                    return render(request, 'webapp/payment_success.html', {'form': form})

                else:
                    # Создаем собственное исключение для ошибок Stripe и вызываем его
                    raise StripePaymentError('Платеж не был выполнен. Пожалуйста, попробуйте еще раз.')

            except stripe.error.StripeError as e:
                # Обработка других ошибок Stripe
                return render(request, 'webapp/payment_error.html',
                              {'form': form, 'error_message': f'Ошибка Stripe: {e}'})

            except StripePaymentError as e:
                # Обработка собственного исключения StripePaymentError
                return render(request, 'webapp/payment_error.html',
                              {'form': form, 'error_message': str(e)})

    else:
        PaymentForm()

    return render(request, 'webapp/index.html')


def payment_success(request):
    # Предположим, что у вас есть объект Payment, который вы хотите передать
    payment = Payment.objects.first()  # Здесь предполагается, что вы получаете платеж из базы данных
    return render(request, 'webapp/payment_success.html', {'payment': payment})

def payment_error(request):
    return render(request, 'webapp/payment_error.html')
