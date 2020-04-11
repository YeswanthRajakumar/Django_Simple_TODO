from django.urls import path, include
from accounts import views
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('register/', views.register, name='user-register'),
    path('login/', LoginView.as_view(template_name='login.html'), name='user-login'),
    path('logout/', LogoutView.as_view(template_name='logout.html'), name='user-logout'),

]
