from django.urls import path  
from . import views
urlpatterns = [  
        
    path('show', views.show, name='show'),
    path('add', views.add, name='add'),
    path('edit/<str:pk>', views.edit, name='edit'),
    path('delete<str:pk>', views.delete, name='delete')

]