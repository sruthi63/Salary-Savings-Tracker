from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('add-salary/', views.add_salary, name='add_salary'),
    path('add-expense/', views.add_expense, name='add_expense'),
]