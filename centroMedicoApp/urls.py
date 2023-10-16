from django.urls import path
from . import views
from .views import GetEspecialidadPriceView

urlpatterns = [
    path('index',views.index, name='index'),
    path('appointmentNew',views.appointmentNew, name='appointmentNew'),
    path('medicoList',views.medicoList, name='medicoList'),
    path('medicoDetails/<int:rut_med>/', views.medicoDetails, name='medicoDetails'),
    path('especialidad_detail/<int:id_esp>/', views.especialidad_detail, name='especialidad_detail'),
   path('get_especialidad_price/', GetEspecialidadPriceView.as_view(), name='get_especialidad_price'),
]