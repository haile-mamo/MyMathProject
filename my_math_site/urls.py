from django.contrib import admin
from django.urls import path
from math_app import views 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('eee/', views.index), # እዚህ ጋር 'calculate' የነበረውን 'index' አድርገው
]