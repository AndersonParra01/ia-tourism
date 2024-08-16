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
    path('users/addToPlace', views.add_users_to_place, name='add_users_to_place' ),
    path('users/remove-users-from-place', views.remove_users_from_place, name='remove_users_from_place'),
    
]
""" path('auth/logout', views.logout, name='logout'), """