from django.urls import path
from . import views

urlpatterns = [
    path('index',views.index, name='index'),
    path('appointmentNew',views.appointmentNew, name='appointmentNew'),
    path('medicoList',views.medicoList, name='medicoList'),
    path('medicoDetails/<int:rut_med>/', views.medicoDetails, name='medicoDetails'),
]