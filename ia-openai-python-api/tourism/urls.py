from django.urls import path
from .views import get_completion

urlpatterns = [
    path('openai/completion', get_completion),
]
