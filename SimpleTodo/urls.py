
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('tasks/', include('Task.urls')),
    path('user/', include('accounts.urls')),


]
