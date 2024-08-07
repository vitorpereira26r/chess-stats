from rest_framework.response import Response


def success_response(data=None, message=None):
    response_data = {
        'data': data if data is not None else {},
        'message': message if message is not None else ''
    }
    return Response(response_data, status=200)


def fail_response(message=None, status=501):
    response_data = {
        'message': message if message is not None else 'Error'
    }
    return Response(response_data, status=status)
