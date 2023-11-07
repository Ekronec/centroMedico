from django.urls import path
from . import views

urlpatterns = [
    path('index',views.index, name='index'),
    path('appointmentNew',views.appointmentNew, name='appointmentNew'),
    path('medicoList',views.medicoList, name='medicoList'),
    path('med_index',views.med_index, name='med_index'),
    path('sec_index',views.sec_index, name='sec_index'),
    path('especialidadList',views.especialidad_medico_list, name='especialidadList'),
    path('appointments_details',views.appointment_details, name='appointments_details'),
    path('medicoDetails/<int:rut_med>/', views.medicoDetails, name='medicoDetails'),
    path('especialidad_detail', views.especialidad_detail, name='especialidad_detail'),
    path('get_precio/<int:id_esp>/', views.get_precio, name='get_precio'),
    path('login_view', views.login_view, name='login_view')
]