from rest_framework.generics import GenericAPIView
from reservation.serializers import *
from reservation.controllers import *
from django.http import JsonResponse
from rest_framework.permissions import IsAuthenticated

# Create your views here.

class ReservationView(GenericAPIView):
    #permission_classes = (IsAuthenticated,)
    
    def get_serializer_class(self):
        if self.request.method == "GET":
            return ListReservationSerializers
        if self.request.method == 'POST':
            return InsertReservationSerializers
    
    def get(self, request):  # Preciso especificar o metodo que eu preciso como nome da função no caso é DEF GET(), o mesmo do self.request.method
        return JsonResponse({"reservation":ControllerReservation.list_reservation()})
        #return JsonResponse({"reservation":f"{permission_classes}"})

    def post(self, request):  # Preciso especificar o metodo que eu preciso como nome da função no caso é DEF POST(), o mesmo do self.request.method
        try:
            serializer_obj = InsertReservationSerializers(data=request.data)
            serializer_obj.is_valid(raise_exception=True)
            
            if response_controller := ControllerReservation.creat_reservation(request.data):
                return JsonResponse({"result":f"Reservation Create"}, status=200)
            return JsonResponse({"result":f"Reservation filled"}, status=400)
        except Exception as error:
            return JsonResponse({'error':f'{error}'}, status=400)
    
class ReservationByIdView(GenericAPIView): 
    #permission_classes = (IsAuthenticated,)

    
    def get_serializer_class(self):

        if self.request.method == 'DELETE':
            return DeleteReservationSerializers
        if self.request.method == 'PUT':
            return UpdateReservationSerializers
    
    def delete(self, request, id):  # Preciso especificar o metodo que eu preciso como nome da função no caso é DEF DELETE(), o mesmo do self.request.method
        try: 
            ControllerReservation.delete_reservation(id)
            return JsonResponse({"result":"success"},status=200)
        except:
            return JsonResponse({"error":"Reservation not found"},status=404)

    def put(self, request, id): # Preciso especificar o metodo que eu preciso como nome da função no caso é DEF PUT(), o mesmo do self.request.method
        try:
            ControllerReservation.update_reservation(id, request.data)
            return JsonResponse({"result":f"id {id} success upedated"},status=200)
        except Exception as error:
            #return JsonResponse({"error":"Reservation not found"},status=404)
            return JsonResponse({"error":f"{error}"},status=404)
