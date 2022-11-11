# standard imports
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

def return_sentiment_message(input_message):

    # create the sentiment intensity analyzer
    vader = SentimentIntensityAnalyzer()

    sentiment_message = 'Sentiment Score for '

    sentiment_score = vader.polarity_scores(input_message)

    result_message = sentiment_message + input_message + ':\n' + str(sentiment_score)

    return result_message
