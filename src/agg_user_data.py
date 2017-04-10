import tweepy
from get_api import get_api
import datetime as dt

#Once we are doing large-scale tests we can replace with a func that reads keys from a pickle

key1 = ['UqqhoQSyTE0nhgMV1CpgdIeLU', \
        '8kRZxE2DPJnNBmfiIKxJg8FWYHf4eYmwwZ2Sx0tMcegRT71XTG', \
        '837307303120551937-pUbSOzM3bISJI0J9zsPSQ4MesU5w7YH', \
        '3ohOMAmGkYsPKcq1zDTwNmGnUzPnQwqnV0m9ujy71Ta1p']

key2 = ['uzfX6YkL5fQtdVPQHQhRzEPYq', \
        'UAoxjiPk4mxIrQ6hUScxYv8r3vWYLOnW07XEAuW1gdgqz121jZ', \
        '3453311595-IrMqmvxu42w6Gn68a9zWa0TCTg5ChSmm54KYMWe', \
        'gwLenWKeEJcLeYYZcj0gtYsn0irdZZwuxugUPr5zi0Bnu']

key3 = ['xYsEKjtxp2GLh04obgMYWUcgy', \
        'zvVCFZNvp2UdATHugoBmoSDWHFUpOpLZGvoHHU8UGk0ADTuBEH', \
        '850096655965859841-Y8Y1pDjaKJkDOiolJzO89R1e1dZten4', \
        'wqzoHkebEg9HwVL5shX5HdaPHmMAkMV9yJHyjKXgMsLhh']

def agg_user_data(user_id, api):     
##    api = get_api(key1[0], key1[1], key1[2], key1[3])
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
    
    return [1 if user.protected else 0, age, in_out_ratio, favourites_ratio, \
            status_ratio, acct_rep, 1 if user.default_profile else 0, \
            1 if user.default_profile_image else 0]
