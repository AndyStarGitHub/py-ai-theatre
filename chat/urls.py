from django.urls import path
from . import views

urlpatterns = [
    path('', views.chat_view, name='chat'),
    path('clear/', views.clear_history_view, name='clear_history'),
]
