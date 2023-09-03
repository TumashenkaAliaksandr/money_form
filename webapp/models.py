from django.db import models

class Payment(models.Model):
    owner = models.CharField(max_length=255)
    card_number = models.CharField(max_length=16, default=0)
    cvv = models.CharField(max_length=4)
    expiration_date_month = models.CharField(max_length=2)
    expiration_date_year = models.CharField(max_length=4)

    def __str__(self):
        return f"Payment by {self.owner}"
