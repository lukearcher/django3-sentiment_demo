from django.shortcuts import render
from django.http import HttpResponse
from .functions import return_sentiment_message

def home(request):
    return render(request, 'sentiment/home.html', {'message': ''})

def sentiment(request):

    sentiment_phrase = request.GET.get('phrase', '')

    return_message = return_sentiment_message(sentiment_phrase)

    return render(request, 'sentiment/home.html', {'message': return_message})
