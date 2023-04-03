from django.urls import path
from crudapp import views

#Code starts here

urlpatterns = [
    path('', views.data_input, name = 'home'),
    path('update/<int:id>/',views.update_data, name = 'update'),
    path('delete/<int:id>/',views.delete_data, name = 'delete'),
    path('signup/',views.sign_up, name = 'signup'),
    path('login/',views.log_in, name = 'login'),
    path('profile/',views.user_profile, name = 'userprofile'),
    path('logout/',views.user_logout, name = 'logout'),
    path('changepassword/',views.user_changepassword, name = 'changepass'),
    path('userdetail/<int:id>',views.user_detail, name = 'userdetail'),
    
]
