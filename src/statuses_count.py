import tweepy
from get_api import get_api

#Once we are doing large-scale tests we can replace with a func that reads keys from a pickle
consumer_key = 'UqqhoQSyTE0nhgMV1CpgdIeLU'
consumer_secret = '8kRZxE2DPJnNBmfiIKxJg8FWYHf4eYmwwZ2Sx0tMcegRT71XTG'
access_token = '837307303120551937-pUbSOzM3bISJI0J9zsPSQ4MesU5w7YH'
access_secret = '3ohOMAmGkYsPKcq1zDTwNmGnUzPnQwqnV0m9ujy71Ta1p'

#Takes a user ID string and returns an int representing the number of tweets+retweets ever issued
def statuses_count(user_id):     
    api = get_api(consumer_key, consumer_secret, access_token, access_secret)
    user = api.get_user(user_id)
    return user.statuses_count

