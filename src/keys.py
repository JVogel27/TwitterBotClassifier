import random


class KeySet():
	"""
	
	"""
	def __init__(self, consumer_key, consumer_secret, access_token, access_secret):
		self.consumer_key = consumer_key
		self.consumer_secret = consumer_secret
		self.access_token = access_token
		self.access_secret = access_secret

	def to_string(self):
		return "consumer key: " + self.consumer_key + "\nconsumer_secret: " + self.consumer_secret + "\naccess token: " \
		       + self.access_token + "\naccess_secret: " + self.access_secret


def read_key_file(path):
	"""
	parse a file containing a list of auth keys
	:param path: the path to the key file
	:return: a list of KeySet objects that contain the appropriate values needed to auth with the twitter API
	"""
	keys = []
	with open(path) as file:
		parts = file.readline().split(',')
		while len(parts) is 4:
			keys.append(KeySet(parts[0], parts[1], parts[2], parts[3]))
			parts = file.readline().split(',')
	return keys


def pick_random_key(keys):
	"""
	choose a random key object to use for the twitter API
	:param keys: the list of keys to choose from
	:return: the random key object
	"""
	return random.choice(keys)