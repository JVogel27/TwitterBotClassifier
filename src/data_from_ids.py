from get_tweet_ratios import get_data
from get_api import get_api
import tweepy
import csv
import os

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

api = get_api(key1[0], key1[1], key1[2], key1[3])
##api = get_api(key2[0], key2[1], key2[2], key2[3])
##api = get_api(key3[0], key3[1], key3[2], key3[3])

def get_data_from_humans():
    try:
        x = []
        with open('..//human_x.txt', 'r') as f:
            reader = csv.reader(f)
            for row in reader:
                x.append(row)

        os.remove('..//human_x.txt')
        
        with open('..//humans_copy.txt', 'r') as f_read:
            with open('..//human_x.txt', 'w') as f_write:
                writer = csv.writer(f_write, lineterminator='\n')
                for row in x:
                    writer.writerow(row)
                for count, line in enumerate(f_read):
                    
                    row = get_data(line.rstrip(), api)

                    writer.writerow(row)

                    print(line)
         
    except tweepy.TweepError:
        f_write.close()


def get_data_from_bots():
    try:
        x = []
        with open('..//bot_x.txt', 'r') as f:
            reader = csv.reader(f)
            for row in reader:
                x.append(row)

        os.remove('..//bot_x.txt')
        
        with open('..//bots_copy.txt', 'r') as f_read:
            with open('..//bot_x.txt', 'w') as f_write:
                writer = csv.writer(f_write, lineterminator='\n')
                for row in x:
                    writer.writerow(row)
                for count, line in enumerate(f_read):
                    
                    row = get_data(line.rstrip(), api)

                    writer.writerow(row)

                    print(line)
         
    except tweepy.TweepError:
        f_write.close()

        

##get_data_from_humans()
##get_data_from_bots()
