from django.urls import path
from . import views

urlpatterns = [
    path('', views.get_facts),
    path('user/', views.user_facts),
    path('int:pk/', views.factDetail.as_view()),
]