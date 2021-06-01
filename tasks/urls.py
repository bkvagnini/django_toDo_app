from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = "list"),
    path('update_task/<str:pk>/', views.updateTask, name = "update_task"), 
    #the str:pk makes the url dynamic and makes it use the pk provides by the updateTask function pk parameter
    path('deleteTask/<str:pk>/', views.deleteTask, name = "delete") 
]