import tweepy
from get_api import get_api
from agg_user_data import agg_user_data

#Once we are doing large-scale tests we can replace with a func that reads keys from a pickle
consumer_key = 'UqqhoQSyTE0nhgMV1CpgdIeLU'
consumer_secret = '8kRZxE2DPJnNBmfiIKxJg8FWYHf4eYmwwZ2Sx0tMcegRT71XTG'
access_token = '837307303120551937-pUbSOzM3bISJI0J9zsPSQ4MesU5w7YH'
access_secret = '3ohOMAmGkYsPKcq1zDTwNmGnUzPnQwqnV0m9ujy71Ta1p'


#Takes a user_id and returns a dictionary
#Dictionary keys are the sources of all the users tweets
#Dictionary values are the relative frequencies of each
def tweet_source_ratios(user_id):
    api = get_api(consumer_key, consumer_secret, access_token, access_secret)

    user_data = agg_user_data(user_id)

    source_ratios = {}

    if not user_data['protected']:
        for tweet in tweepy.Cursor(api.user_timeline, id=user_id).items():
            if tweet.source in source_ratios:
                source_ratios[tweet.source] += 1
            else:
                source_ratios[tweet.source] = 1
                total_sources_recorded = 0


        #Summing the total recorded values here, rather than user_data[statuses_count]
        #   in case we want to change items() to some number items(n), to only pull n tweets
        #Not sure how to do this with variable args, as we don't have a constant default for n
        for key in source_ratios:
            total_sources_recorded += source_ratios[key]

        for key in source_ratios:
            flat_val = source_ratios[key]
            source_ratios[key] = flat_val/total_sources_recorded
    
        return total_sources_recorded, source_ratios, 

    else:
        print("protected")
        return 0, {}




#Example

#Non-protected case
#print(tweet_source_ratios('1536488724'))

#Protected case
#print(tweet_source_ratios('2663852887'))
