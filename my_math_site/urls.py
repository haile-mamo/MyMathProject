from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('math_app.urls')), # ይህ መስመር ነው ዋናውን ገጽ የሚከፍተው
]