from django.db import models
from datetime import date
import uuid

# Create your models here.

class Reservation(models.Model):
    
    id = models.UUIDField(primary_key=True,default=uuid.uuid4,null=False,blank=False,editable=False) # O editable=False faz com que o id nao fique visivel para edicao
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    cpf = models.CharField(max_length=11)
    bike_model = models.TextField()
    number_allocation = models.IntegerField()
    date_entry = models.DateField(default=date.today)
    date_output = models.DateField(default=date.today)

