from django.urls import path
from django.contrib.auth import views as auth_views

from authentication import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', auth_views.LoginView.as_view(template_name='authentication/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('signup/', views.signup, name='signup'),
]



# from atexit import register
# from django.urls import path , include
# from . import views

# urlpatterns = [
#     path('', views.login, name='login'),
#     path('register', views.register, name='register'),
#     path('dashboard', views.dashboard, name='dashboard'),
