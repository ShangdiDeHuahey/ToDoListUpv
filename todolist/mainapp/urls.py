from django.urls import path
from .views import *

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('list/', ListTodo.as_view(), name='list-todo'),
    path('<int:pk>/', DetailTodo.as_view(), name='detail-todo'),
    path('create/', CreateTodo.as_view(), name='create-todo'),
    path('delete/<int:pk>/', DeleteTodo.as_view(), name='delete-todo'),
    path('update/<int:pk>/completion/', UpdateCompletion.as_view(), name='update-completion'),
]
