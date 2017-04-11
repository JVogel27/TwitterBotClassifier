import tweepy
from get_api import get_api
import datetime as dt
import numpy as np
import requests

dow_ratios = {0:0, 1:0, 2:0, 3:0, 4:0, 5:0, 6:0}


def get_data(user_id, api):
    tweets_parsed = 0
    
    hashtags_recorded = 0
    user_mentions_recorded = 0
    
    urls = []

    mal_urls_ratio = 0
    
    tweets_per_day = [-1]
    cur_date = dt.datetime.today()
    date_count = 0


    user = api.get_user(user_id)

    age = dt.datetime.today().timestamp() - user.created_at.timestamp()

    in_out_ratio = 1
    if user.friends_count != 0:     
        in_out_ratio = user.followers_count / user.friends_count

    favourites_ratio = 86400 * user.favourites_count / age

    status_ratio = 86400 * user.statuses_count / age

    acct_rep = 0
    if user.followers_count + user.friends_count != 0:
        acct_rep = user.followers_count / (user.followers_count + user.friends_count)  
    
    user_data = [age, in_out_ratio, favourites_ratio, \
            status_ratio, acct_rep,]
    
    
    #If this account is protected we cannot see their tweets and should skip

    #Once further progress is made, this check will likely be done at a higher level,
    #   and the user account will not even make it to this stage
    if not user.protected:
        #Iterate through all (3200 max) tweets. items() can take a lower max to limit
        for tweet in tweepy.Cursor(api.user_timeline, id=user_id, tweet_mode='extended').items(1000):
            update_dow_ratios(tweet.created_at.weekday())
        
            #If this tweet contained urls, count them
            if len(tweet.entities['urls']) > 0:
                for url in tweet.entities['urls']:
                    urls.append(url['expanded_url'])
                
            #If this tweet conatained hashtags, count them
            if len(tweet.entities['hashtags']) > 0:
                   hashtags_recorded += len(tweet.entities['hashtags'])
            
            #If this tweet contained user mentions, count them
            if len(tweet.entities['user_mentions']) > 0:
                   user_mentions_recorded += len(tweet.entities['user_mentions'])
            
            #Count up the tweets for each day
            #First if block captures date of most recent tweet
            if date_count == 0: 
                cur_date = tweet.created_at
                tweets_per_day.append(0)
                date_count += 1
                tweets_per_day[date_count] += 1
            #elif block handles first tweet of next day
            elif tweet.created_at.day != cur_date.day:
                cur_date = tweet.created_at
                date_count += 1
                tweets_per_day.append(0)
                tweets_per_day[date_count] += 1
            #Else block handles more tweets on the same day
            else:
                tweets_per_day[date_count] += 1

            tweets_parsed += 1

        #Well this data sucks
        if tweets_parsed == 0:
            return user_data + [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        
        #Calculate dow_ratios from values
        for key in dow_ratios:
            flat_val = dow_ratios[key]
            dow_ratios[key] = flat_val/tweets_parsed

        #Calculate ratio of total urls posted over tweets parsed
        urls_ratio = len(urls)/tweets_parsed

        #Calculate ratio of total hashtags over tweets parsed
        hashtags_ratio = hashtags_recorded/tweets_parsed

        #Calculate ratio of total user mentions over tweets parsed
        user_mentions_ratio = user_mentions_recorded/tweets_parsed
        
        #Slice the tweets_per_day list to remove the first -1 value
        tweets_per_day = tweets_per_day[1:]
        avg_tpd = np.average(tweets_per_day)

        #Get ratio of malicious urls to total urls posted
        if len(urls) > 0:
            mal_urls_ratio = num_malicious_urls(urls) / len(urls)
        
        return (user_data + [urls_ratio, dow_ratios[0], dow_ratios[1], \
                dow_ratios[2], dow_ratios[3], dow_ratios[4], dow_ratios[5], \
                dow_ratios[6], avg_tpd, hashtags_ratio, user_mentions_ratio, mal_urls_ratio])
        
    else:
        print("Protected Account: {}".format(user_id))
        return user_data + [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]
    
#Send all the urls out to Google's SafeBrowsing API to check for
# malicious urls, and return the number found
def num_malicious_urls(urls):
    key = 'AIzaSyAAPunMDPhArqLnE_zH9ZK91VDGWxka8K8'
    lookup_url = 'https://safebrowsing.googleapis.com/v4/threatMatches:find?key={}'.format(key)

    url_list = ''
    for url in urls:
        url_list += '{{\"url\": \"{}\"}},\n'.format(url)
    
    payload = '{{\"client\" : \
               {{\"clientId\" : \"csci455\", \"clientVersion\" : \"0.0.1\"}}, \
               \"threatInfo\" : \
               {{\"threatTypes\" : [\"MALWARE\",\"SOCIAL_ENGINEERING\",\"UNWANTED_SOFTWARE\",\"MALICIOUS_BINARY\"], \
                \"platformTypes\" : [\"ANY_PLATFORM\"], \
                \"threatEntryTypes\" : [\"URL\"], \
                \"threatEntries\": [ {} ] \
                }} \
                }}'.format(url_list)
    r = requests.post(lookup_url, data = payload)
    if r.status_code == 200 and len(r.json()) > 0:
        return (len(r.json()['matches']))
    return 0


def update_dow_ratios(weekday):
    dow_ratios[weekday] += 1
