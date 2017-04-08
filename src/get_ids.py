import tweepy
from get_api import get_api
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

def write_ids():
    humans = []
    bots = []

    with open('..//ASONAM_honeypot_data/honeypot.txt', 'r') as f:
        for line in f:
            tokens = line.split(' ')
            if tokens[0] == 'human':
                humans.append(tokens[1])
                humans.append('\n')
            elif tokens[0] == 'bot':
                bots.append(tokens[1])
                bots.append('\n')

    with open('..//all_humans.txt', 'w') as f:
        f.write(''.join(humans))

    with open('..//all_bots.txt', 'w') as f:
        f.write(''.join(bots))

def lookup_humans():
    api = get_api(key1[0], key1[1], key1[2], key1[3])
    ids = []
    good_ids = []
    with open('..//all_humans.txt', 'r') as f:
        for count, line in enumerate(f):
            ids.append(line.rstrip())
            if count % 100 == 0:
                for user in api.lookup_users(ids):
                    good_ids.append(user.id_str)
                    good_ids.append('\n')
                ids = []
    with open('..//existing_humans.txt', 'w') as f:
        f.write(''.join(good_ids))

def lookup_bots():
    api = get_api(key1[0], key1[1], key1[2], key1[3])
    ids = []
    good_ids = []
    with open('..//all_bots.txt', 'r') as f:
        for count, line in enumerate(f):
            ids.append(line.rstrip())
            if count % 100 == 0:
                for user in api.lookup_users(ids):
                    good_ids.append(user.id_str)
                    good_ids.append('\n')
                ids = []
    with open('..//existing_bots.txt', 'w') as f:
        f.write(''.join(good_ids))


def check_human_accounts():
    api = get_api(key3[0], key3[1], key3[2], key3[3])
    ids = []
    try:
        with open('..//humans.txt', 'r') as f:
            for line in f:
                ids.append(line.rstrip())
                ids.append('\n')

        os.remove('..//humans.txt')
                  
        with open('..//existing_humans_copy.txt', 'r') as f_read:
            with open('..//humans.txt', 'w') as f_write:
                f_write.write(''.join(ids))
                for line in f_read:
                    user = api.get_user(line.rstrip())
                    print(line)
                    if not user.protected:
                        f_write.write(line)
    except tweepy.TweepError:
        f_read.close()
        f_write.close()

def check_bot_accounts():
    api = get_api(key2[0], key2[1], key2[2], key2[3])
    ids = []

    try:
        with open('..//bots.txt', 'r') as f:
                for line in f:
                    ids.append(line.rstrip())
                    ids.append('\n')

        os.remove('..//bots.txt')
        with open('..//existing_bots_copy.txt', 'r') as f_read:
            with open('..//bots.txt', 'w') as f_write:
                f_write.write(''.join(ids))
                for line in f_read:
                    user = api.get_user(line.rstrip())
                    print(line)
                    if not user.protected:
                        f_write.write(line)
    except tweepy.TweepError:
        f_read.close()
        f_write.close()















