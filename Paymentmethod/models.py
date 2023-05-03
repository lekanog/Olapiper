from django.db import models
# from django.contrib.auth.models import User
from django.conf import settings

class Card(models.Model):
    user	= models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.PROTECT,related_name='Method_User',null=True,blank=True)
    name_on_card = models.CharField(max_length=255)
    card_number = models.CharField(max_length=16)
    expiration_date = models.DateField()
    security_code = models.CharField(max_length=4)
