from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('add/', views.add_employee),
    path('update/<int:pk>', views.update_employee)
]