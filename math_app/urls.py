from django.urls import path 
from django.urls import path
from . import views # እዚህ ጋር መኖሩ ትክክል ነው

urlpatterns = [
    path('', views.home, name='home'),
]