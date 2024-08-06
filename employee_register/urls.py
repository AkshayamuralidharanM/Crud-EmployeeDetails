from django.urls import path,include
from . import views


urlpatterns = [
    path('form/', views.employee_form, name='employee_insert'), #get and post req for insert operation
    path('<int:id>/', views.employee_form, name='employee_update'), #get and post reqfor update operation
    path('delete/<int:id>/',views.employee_delete,name='employee_delete'),
    path('list/',views.employee_list, name='employee_list') #get operation to retrieve all the records
    
]
