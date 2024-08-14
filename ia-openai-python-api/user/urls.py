from django.urls import path
from . import views

urlpatterns = [
    path('users/all', views.getAll, name='getAll'),
    path('users/get/<int:id>', views.getById, name='getById'),
    path('users/create', views.create, name='create'),
    path('users/update/<int:id>', views.update, name='update'),
    path('users/patch/<int:id>', views.patch, name='patch'),
    path('users/delete/<int:id>', views.deleteById, name='deleteById'),
    path('auth/register', views.register, name='register'),
    path('auth/login', views.login, name='login'),
]
