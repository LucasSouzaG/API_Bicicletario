from django.urls import path
from reservation import views

urlpatterns = [
    path('',views.ReservationView.as_view()),
    path('<str:id>',views.ReservationByIdView.as_view()),
]