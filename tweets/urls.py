''' tweets.urls '''

from django.urls import path    

from .views import Index

app_name = 'tweets'

urlpatterns = [
    path('', Index.as_view()),
]