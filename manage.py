#!/usr/bin/env python
import os
import sys
import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.handlers.wsgi import WSGIRequest
from django.http import HttpResponse
from django.urls import path

def chatbot_response(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        message = data.get('message', '')
        
        # Generate a response based on the user's message
        response_message = "This is a placeholder response. You said: " + message

        return JsonResponse({'response': response_message})
    return JsonResponse({'response': 'Invalid request'}, status=400)

# Define URL pattern for the chatbot response
urlpatterns = [
    path('chatbot_response/', chatbot_response, name='chatbot_response'),
]

# Define a simple application to handle requests
def application(environ, start_response):
    request = WSGIRequest(environ)
    response = None
    for urlpattern in urlpatterns:
        if request.path == urlpattern.pattern:
            response = urlpattern.callback(request)
            break
    if response is None:
        response = HttpResponse("404 Not Found", status=404)
    return response(environ, start_response)

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "hospitalmanagement.settings")
    try:
        from django.core.management import execute_from_command_line
        
        # Run the application using Django's development server
        from django.core.management.commands.runserver import Command as runserver
        runserver.default_port = "8001"  # Change the port if needed
        execute_from_command_line(['manage.py', 'runserver', 'localhost:8000'])
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "forget to activate a virtual environment?"
        ) from exc
