from django.db import models
from django.conf import settings
from Payment.models import Payment

STATUS_CHOICES = (
        ('completed', 'Completed'),
        ('failed', 'Failed'),
    )

class Paymenthistory(models.Model):
    user	= models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.PROTECT,related_name='Payment_User',null=True,blank=True)
    Payment = models.ForeignKey(Payment, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='due')
    date = models.DateTimeField(auto_now_add=True)

