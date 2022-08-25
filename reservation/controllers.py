from django.shortcuts import get_object_or_404
from reservation.models import Reservation
from reservation.serializers import * 

class ControllerReservation():

    '''Listar todos os dados com base no modelo reservation'''
    def list_reservation():
        list_reservations = ListReservationSerializers(Reservation.objects.all(),many = True).data
        return list_reservations

    '''Criar um registro no sqlite com o dado vindo das Views'''
    def creat_reservation(data:dict):
        if allocation_and_range_date := Reservation.objects.filter(number_allocation = data['number_allocation']) and (Reservation.objects.filter(date_entry__lte = data['date_entry']) and Reservation.objects.filter(date_output__gte = data['date_output'])):
            return False
        else:
            if create_reservation := Reservation.objects.create(**data):
                return create_reservation
            else:
                return False


    '''Deletar um registro no sqlite com o dado vindo das Views'''
    def delete_reservation(id):

        if delete_reservation := get_object_or_404(Reservation, pk=id):
            return delete_reservation.delete()
        else:
            return False

    '''Atualizar um registro no sqlite com o dado vindo das Views'''
    def update_reservation(id:str, data:dict):
        if serch_reservation := get_object_or_404(Reservation, pk=id):
                
            for key, value in data.items():
                setattr(serch_reservation, key, value)
                    
            return serch_reservation.save()
        