import datetime
from django.utils import timezone
from django.db.models import Q
from django.db import models

class PaymentQuerySet(models.QuerySet):
    def due_payments(self):
        today = timezone.now().date()
        return self.filter(Q(status = 'due') & Q(next_due = today) )
    

class PaymentManager(models.Manager):
    def get_queryset(self):
        return PaymentQuerySet(self.model,using=self._db) #important
    
    def due_payment(self):
        return self.get_queryset().due_payments()