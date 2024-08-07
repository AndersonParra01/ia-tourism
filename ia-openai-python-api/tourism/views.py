from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.conf import settings

import requests
@api_view(['GET'])
def get_completion(request):
    prompt = request.query_params.get('prompt')
    headers = {
        'content-type': 'application/json',
        'Authorization': f'Bearer {settings.OPENAI_API_KEY}'
    }

    data = {
        'model': 'gpt-3.5-turbo-instruct',
        'prompt': prompt,
        'max_tokens': 100,
    }

    response = requests.post('https://api.openai.com/v1/completions', json=data, headers=headers)
    return Response(response.json())
