from django.urls import path
from . import views

urlpatterns = [
    path('', views.get_facts),
    path('user/', views.user_facts),
    path('<int:pk>/', views.get_fact),
    path('update/<int:pk>/', views.update_fact),
    path('delete/<int:pk>/', views.delete_fact),
]