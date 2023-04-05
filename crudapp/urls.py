from django.urls import path
from crudapp import views

#Code starts here

urlpatterns = [
    path('', views.data_input, name = 'home'),
    path('update/<int:id>/',views.update_data, name = 'update'),
    path('delete/<int:id>/',views.delete_data, name = 'delete'),
    
    
]
