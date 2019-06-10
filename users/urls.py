from django.urls import path
from .views import Profile

app_name = 'users'

urlpatterns = [
    path('<str:username>/', Profile.as_view()),
]
