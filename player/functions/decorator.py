import requests
from django.conf import settings
from player.exceptions import PlayerNotFoundException
from utils.date_format import format_timestamp
from utils.api_response import success_response

API_URL = settings.CHESS_DOT_COM_URL
HEADERS = settings.CHESS_DOT_COM_HEADERS


def player_data(username):
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


def player_ratings(username):
    endpoint = f'{API_URL}pub/player/{username}/stats'
    response = requests.get(endpoint, headers=HEADERS)

    if response.status_code == 404:
        raise PlayerNotFoundException(message=f'Player {username} not found')

    data = response.json()
    chess_daily_json = data.get("chess_daily", {})
    chess_rapid_json = data.get("chess_rapid", {})
    chess_bullet_json = data.get("chess_bullet", {})
    chess_blitz_json = data.get("chess_blitz", {})

    daily = daily_chess_record(chess_daily_json)
    rapid_chess = normal_chess_record(chess_rapid_json)
    bullet_chess = normal_chess_record(chess_bullet_json)
    blitz_chess = normal_chess_record(chess_blitz_json)

    format_data = {
        "username": username,
        "daily": daily,
        "rapid": rapid_chess,
        "blitz": blitz_chess,
        "bullet": bullet_chess,
    }

    return success_response(data=format_data, message="Rating data was successfully retrieved")


def is_player_online(username):
    endpoint = f'{API_URL}pub/player/{username}/is-online'
    response = requests.get(endpoint, headers=HEADERS)

    if response.status_code == 404:
        raise PlayerNotFoundException(message=f'Player {username} not found')

    data = response.json()

    format_data = {
        "username": username,
        "is_online": data.get('online', False),
    }

    return success_response(data=format_data, message="Player data was successfully retrieved")


def daily_chess_record(json):
    daily = {}

    # Rating information
    if json.get("last"):
        daily["rating"] = {
            "rating": json.get("last", {}).get("rating", None),
            "date": format_timestamp(json.get("last", {}).get("date", None)),
        }

    # Best rating
    if json.get("best"):
        daily["best_rating"] = {
            "rating": json.get("best", {}).get("rating", None),
            "date": format_timestamp(json.get("best", {}).get("date", None)),
        }

    # Record
    if json.get("record"):
        daily["record"] = {
            "win": json.get("record", {}).get("win", None),
            "lost": json.get("record", {}).get("loss", None),  # corrected from "lost" to "loss"
            "draw": json.get("record", {}).get("draw", None),
            "time_per_move": json.get("record", {}).get("time_per_move", None),
        }

    # Tournament (only if it exists)
    if json.get("tournament"):
        daily["tournament"] = {
            "points": json.get("tournament", {}).get("points", None),
            "withdraw": json.get("tournament", {}).get("withdraw", None),
            "count": json.get("tournament", {}).get("count", None),
            "highest_finish": json.get("tournament", {}).get("highest_finish", None),
        }

    return daily


def normal_chess_record(json):
    record = {}

    # Rating information
    if json.get("last"):
        record["rating"] = {
            "rating": json.get("last", {}).get("rating", None),
            "date": format_timestamp(json.get("last", {}).get("date", None)),
        }

    # Best rating
    if json.get("best"):
        record["best_rating"] = {
            "rating": json.get("best", {}).get("rating", None),
            "date": format_timestamp(json.get("best", {}).get("date", None)),
        }

    # Record
    if json.get("record"):
        record["record"] = {
            "win": json.get("record", {}).get("win", None),
            "lost": json.get("record", {}).get("loss", None),  # corrected from "lost" to "loss"
            "draw": json.get("record", {}).get("draw", None),
            "time_per_move": json.get("record", {}).get("time_per_move", None),
        }

    return record
