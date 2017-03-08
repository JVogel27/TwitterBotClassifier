import tweepy
from get_api import get_api
from agg_user_data import agg_user_data
import datetime as dt

#Once we are doing large-scale tests we can replace with a func that reads keys from a pickle
consumer_key = 'UqqhoQSyTE0nhgMV1CpgdIeLU'
consumer_secret = '8kRZxE2DPJnNBmfiIKxJg8FWYHf4eYmwwZ2Sx0tMcegRT71XTG'
access_token = '837307303120551937-pUbSOzM3bISJI0J9zsPSQ4MesU5w7YH'
access_secret = '3ohOMAmGkYsPKcq1zDTwNmGnUzPnQwqnV0m9ujy71Ta1p'

source_ratios = {}
dow_ratios = {0:0, 1:0, 2:0, 3:0, 4:0, 5:0, 6:0}



#Takes a user_id and returns a 4-Tuple (A, B, C, D)
#A: int
    #How many tweets were iterated through
#B: float
    #Ratio of URLs posted to total tweets
#C: dict
    #Keys are the sources of all the users tweets
    #Values are the relative frequencies of tweets from each source
#D: dict
    #Keys are day of week, 0-6 maps to Sun-Sat
    #Values are relative frequencies of tweets on each day
def get_tweet_ratios(user_id):
    api = get_api(consumer_key, consumer_secret, access_token, access_secret)

    user_data = agg_user_data(user_id)  

    total_tweets_recorded = 0

    urls_recorded = 0
    
    #If this account is protected we cannot see thier tweets and should skip
    #Once further progress is made, this check will likely be done at a higher level,
    #   and the user account will not even make it to this stage
    if not user_data['protected']:
        #Iterate through all (3200 max) tweets. items() can take a lower max to limit
        for tweet in tweepy.Cursor(api.user_timeline, id=user_id, tweet_mode='extended').items():
            update_source_ratios(tweet.source)
            update_dow_ratios(tweet.created_at.weekday())

            #If this tweet contained urls, count them - later will use Google or Cymon API
            #   to check if the urls are threats/malicious
            if len(tweet.entities['urls']) > 0:
                urls_recorded += len(tweet.entities['urls'])
                
            #Summing the total recorded values here, rather than user_data[statuses_count]
            #   in case we want to change items() to some number items(n), to only pull n tweets
            #Not sure how to do this with variable args, as we don't have a constant default for n
            total_tweets_recorded += 1

        #Calculate source_ratios from values
        for key in source_ratios:
            flat_val = source_ratios[key]
            source_ratios[key] = flat_val/total_tweets_recorded

        #Calculate dow_ratios from values
        for key in dow_ratios:
            flat_val = dow_ratios[key]
            dow_ratios[key] = flat_val/total_tweets_recorded

        #Calculate ratio of total urls posted over total tweets
        urls_ratio = urls_recorded/total_tweets_recorded
        
        return total_tweets_recorded, urls_ratio, source_ratios, dow_ratios

    else:
        print("Protected: {}".format(user_id))
        return -1, -1, {}, {}
    

def update_source_ratios(source):
    if source in source_ratios:
        source_ratios[source] += 1
    else:
        source_ratios[source] = 1


def update_dow_ratios(weekday):
    dow_ratios[weekday] += 1

        
#Example

#Non-protected case
#print(get_tweet_ratios('1536488724'))

#Protected case
#print(get_tweet_ratios('2663852887'))
