from django.urls import path
from . import views
from .views import get_completion

urlpatterns = [
    path('openai/completion', views.get_completion, name='get_completion'),
    path('places/all', views.getAll, name='getAll'),
    path('places/get/<int:id>', views.getById, name='getById'),
    path('places/create', views.create, name='create'),
    path('places/update/<int:id>', views.update, name='update'),
    path('places/patch/<int:id>', views.patch, name='patch'),
    path('places/delete/<int:id>', views.deleteById, name='deleteById'),
    path('places/delete/getUsersById/<int:id>', views.deleteUsersById, name='deleteUsersById'),
]
