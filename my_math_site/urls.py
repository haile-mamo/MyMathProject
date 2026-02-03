from django.urls import path
from . import views

urlpatterns = [
    # እዚህ ጋር ባዶ ኮቴ ('') መኖሩን አረጋግጥ
    path('', views.home, name='home'), 
]