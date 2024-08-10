from .exceptions import PlayerNotFoundException
from rest_framework.views import APIView
from rest_framework import status
from .models import PlayerRequests
from .functions.decorator import player_data, player_ratings, is_player_online
from utils.api_response import fail_response


class PlayerProfile(APIView):

    @staticmethod
    def get(request, username):
        try:
            response = player_data(username)
            #request_log = PlayerRequests(
                #username=username,
                #service_used="PlayerProfile",
            #)
            #request_log.save()
        except PlayerNotFoundException as e:
            response = fail_response(
                message=e.message,
                status=status.HTTP_404_NOT_FOUND
            )
        except Exception as e:
            response = fail_response(
                message=f"An unexpected error occurred: {str(e)}",
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

        return response


class PlayerRatings(APIView):

    @staticmethod
    def get(request, username):
        try:
            response = player_ratings(username)
            # request_log = PlayerRequests(
            # username=username,
            # service_used="PlayerProfile",
            # )
            # request_log.save()
        except PlayerNotFoundException as e:
            response = fail_response(
                message=e.message,
                status=status.HTTP_404_NOT_FOUND
            )
        except Exception as e:
            response = fail_response(
                message=f"An unexpected error occurred: {str(e)}",
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

        return response


class IsPlayerOnline(APIView):

    @staticmethod
    def get(request, username):
        try:
            response = is_player_online(username)
            # request_log = PlayerRequests(
            # username=username,
            # service_used="PlayerProfile",
            # )
            # request_log.save()
        except PlayerNotFoundException as e:
            response = fail_response(
                message=e.message,
                status=status.HTTP_404_NOT_FOUND
            )
        except Exception as e:
            response = fail_response(
                message=f"An unexpected error occurred: {str(e)}",
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

        return response
