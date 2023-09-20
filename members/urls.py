from django.urls import path
from . import views

urlpatterns = [
    path('members/', views.members, name='members'),
    path('get_session_id/', views.get_session_id, name='get_session_id'),
    
]