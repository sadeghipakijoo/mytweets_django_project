from django.shortcuts import render
from django.views import View


from tweets.models import Tweet
from .models import User


# Create your views here.
class Profile(View):
    def get(self, request, username):
        params = {}
        user = User.objects.get(username=username)
        tweet = Tweet.objects.filter(created_by=user)
        params['tweets'] = tweet
        params['user'] = user
        return render(request, 'pages/profile.html', params)