from django.db import models

class Payment(models.Model):
    order_id = models.CharField(max_length=200)
    payment_id = models.CharField(max_length=200)
    amount = models.IntegerField()
    status = models.CharField(max_length=50)

    def __str__(self):
        return self.payment_id