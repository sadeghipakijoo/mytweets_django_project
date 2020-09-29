''' tweets.views '''
from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View

# import templates

# from .models import Tweets

# function based index page
# def index(request):
#     if request.method == 'GET':
#         ''' GET request '''
#         return HttpResponse('i am get request in index page')
#     elif request.method == 'POST':
#         ''' POST request '''
#         return HttpResponse('i am post request in index page')

# class based views
class Index(View):
    def get(self, request):
        params = {}
        params['name'] = 'django'
        print("test")
        return render(request, 'pages/index.html', params)
    def post(self, request):
        return HttpResponse('post request in index')