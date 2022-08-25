from rest_framework import serializers
from reservation.models import Reservation

class ListReservationSerializers(serializers.ModelSerializer):

    class Meta:
        model = Reservation
        fields = '__all__'

class InsertReservationSerializers(serializers.ModelSerializer):
   
    class Meta: 
        model = Reservation
        fields = '__all__'

class DeleteReservationSerializers(serializers.ModelSerializer):
   
    class Meta: 
        model = Reservation
        fields = ['id']

class UpdateReservationSerializers(serializers.ModelSerializer):

   
    first_name = serializers.CharField(max_length=255,required=False,default='string')
    last_name = serializers.CharField(max_length=255,required=False,default='string')
    bike_model = serializers.CharField(max_length=255,required=False,default='string')
    number_allocation = serializers.IntegerField(required=False,default=0)
    
    class Meta: 
        model = Reservation
        fields = ['first_name','last_name','bike_model','number_allocation']
