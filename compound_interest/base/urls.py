from django.urls import path
from .views import index,calculate_profit

urlpatterns = [
    path('', index, name='index'),
    path('calculate/',calculate_profit, name = 'calculate'),
    
]
