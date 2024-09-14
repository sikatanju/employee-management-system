from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('add/', views.add_employee,name='add-employee'),
    path('update/', views.update_employee_list, name='update-employee-list'),
    path('update/<int:pk>', views.update_an_employee, name='update-employee'),
    path('login/', views.authorize_admin, name='authorize-admin'),
    path('logout/', views.unauthorize_admin, name='unauthorize-admin'),
]