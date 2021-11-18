from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
# Create your models here.
class Client(models.Model):
    nom=models.CharField(max_length=200,null =True)
    prenom=models.CharField(max_length=200,null =True)
    societe=models.CharField(max_length=150,null =True)
    telephone=PhoneNumberField()
    date_creation=models.DateTimeField(auto_now_add=True,null=True)