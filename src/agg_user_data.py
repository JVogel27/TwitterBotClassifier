import tweepy
from get_api import get_api

#Once we are doing large-scale tests we can replace with a func that reads keys from a pickle
consumer_key = 'UqqhoQSyTE0nhgMV1CpgdIeLU'
consumer_secret = '8kRZxE2DPJnNBmfiIKxJg8FWYHf4eYmwwZ2Sx0tMcegRT71XTG'
access_token = '837307303120551937-pUbSOzM3bISJI0J9zsPSQ4MesU5w7YH'
access_secret = '3ohOMAmGkYsPKcq1zDTwNmGnUzPnQwqnV0m9ujy71Ta1p'

def agg_user_data(user_id):     
    api = get_api(consumer_key, consumer_secret, access_token, access_secret)
    user = api.get_user(user_id)
    return {'created_at' : user.created_at, 'favourites_count' : user.favourites_count, 'protected' : user.protected, 'statuses_count' : user.statuses_count, 'friends_count' : user.friends_count, 'followers_count' : user.followers_count, 'location' : user.location, 'default_profile' : user.default_profile, 'default_profile_image' : user.default_profile_image, 'lang' : user.lang}

