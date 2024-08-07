import requests
from django.conf import settings
from player.exceptions import PlayerNotFoundException
from utils.date_format import format_timestamp
from utils.api_response import success_response

API_URL = settings.CHESS_DOT_COM_URL
HEADERS = settings.CHESS_DOT_COM_HEADERS


def player_data(request, username):
    endpoint = f'{API_URL}pub/player/{username}'
    response = requests.get(endpoint, headers=HEADERS)

    if response.status_code == 404:
        raise PlayerNotFoundException(message=f'Player {username} not found')

    data = response.json()

    format_data = {
        "profile_url": data.get("url", None),
        "username": data.get('username', None),
        "player_id": data.get('player_id', None),
        "status": data.get('status', None),
        "name": data.get('name', None),
        "user_avatar": data.get('avatar', None),
        "location": data.get('location', None),
        "country": data.get('country', None),
        "joined_at": format_timestamp(data.get("joined", None)),
        "last_online": format_timestamp(data.get('last_online', None)),
        "followers": data.get('followers', None),
        "league": data.get('league', None),
        "is_streamer": data.get('is_streamer', None),
        "twitch_url": data.get('twitch_url', None),
        "fide_rating": data.get('fide', None),
    }

    return success_response(data=format_data, message="Player data was successfully retrieved")
