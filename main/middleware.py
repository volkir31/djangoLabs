import datetime
import os


def timing(get_response):
    def middleware(request):
        with open(f"{os.getenv('LOG_FILE')}", 'a') as f:
            f.write(f"{datetime.datetime.now()} {request.META.get('REMOTE_ADDR')}\n")
        response = get_response(request)
        return response

    return middleware
