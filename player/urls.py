from django.urls import path
from .views import PlayerProfile

urlpatterns = [
    path('data/<str:username>/', PlayerProfile.as_view(), name='player_data'),
]