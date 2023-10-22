import time
import sqlite3

from .models import Parameters


class LogMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.

    def __call__(self, request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.
        start_time = time.time()

        response = self.get_response(request)

        # Code to be executed for each request/response after
        # the view is called.
        execution_time = time.time() - start_time
        data = [request.method, request.path, execution_time]
        with open("parameters.txt", "w") as file:
            for i in data:
                file.write(f"{str(i)} ")

        params = Parameters(
            request_method=request.method,
            request_path=request.path,
            execution_time=execution_time,
        )
        params.save()
        return response
