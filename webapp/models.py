from django.db import models

class Payment(models.Model):
    name = models.CharField(max_length=255)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_date = models.DateField()
    # Добавьте другие поля, если это необходимо
