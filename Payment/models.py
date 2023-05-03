from django.db import models
from django.conf import settings
from Paymentmethod.models import Card
from .managers import PaymentManager
class Payment(models.Model):
    FREQUENCY_CHOICES = (
        ('monthly', 'Monthly'),
        ('weekly', 'Weekly'),
        ('yearly', 'Yearly'),
    )

    STATUS_CHOICES = (
        ('due', 'Due'),
        ('paid', 'Paid'),
        ('failed', 'Failed'),
        ('terminated', 'Terminated'),
    )

    # user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    user	= models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.PROTECT,related_name='User',null=True,blank=True)
    item = models.CharField(max_length=255)
    item_id = models.CharField(max_length=255, null=True, blank=True)
    description = models.CharField(max_length=255, null=True, blank=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    frequency = models.CharField(max_length=10, choices=FREQUENCY_CHOICES)
    last_paid = models.DateTimeField(null=True, blank=True)
    last_failed = models.DateTimeField(null=True, blank=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='due')
    created = models.DateTimeField(auto_now_add=True)
    terminated_date = models.DateTimeField(null=True, blank=True)
    next_due = models.DateTimeField(null=True, blank=True)
    is_paid = models.BooleanField(default=False)
    method = models.ForeignKey(Card, on_delete=models.SET_NULL, null=True, blank=True)

    objects = PaymentManager()

    def __str__(self):
        return f"{self.user.username} - {self.item} - ${self.amount} ({self.frequency})"
