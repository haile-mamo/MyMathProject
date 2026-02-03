from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('math_app.urls')), 
]
# ከላይ 'from . import views' የሚል መስመር ካለ አጥፋው!