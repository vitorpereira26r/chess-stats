from django.urls import path
from .views import PlayerProfile, PlayerRatings, IsPlayerOnline

urlpatterns = [
    path('data/<str:username>/', PlayerProfile.as_view(), name='player_data'),
    path('data/ratings/<str:username>/', PlayerRatings.as_view(), name='player_ratings'),
    path('data/is-online/<str:username>/', IsPlayerOnline.as_view(), name='player_is_online'),
]
