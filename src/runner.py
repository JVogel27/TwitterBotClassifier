import csv
from get_api import get_api
from get_tweet_ratios import get_data
from classifier import Classifier
from sklearn import datasets
from sklearn.model_selection import train_test_split
import numpy as np
from visualize import visualize_decision_regions
import keys as key_reader
import os
import sys

key = ['UqqhoQSyTE0nhgMV1CpgdIeLU', \
		'8kRZxE2DPJnNBmfiIKxJg8FWYHf4eYmwwZ2Sx0tMcegRT71XTG', \
		'837307303120551937-pUbSOzM3bISJI0J9zsPSQ4MesU5w7YH', \
		'3ohOMAmGkYsPKcq1zDTwNmGnUzPnQwqnV0m9ujy71Ta1p']



def get_training_data():
	X = []
	y = []
	with open('..//human_x.txt', 'r') as f:
		reader = csv.reader(f)
		for row in reader:
			X.append(row)
			y.append(0)
	with open('..//bot_x.txt', 'r') as f:
		reader = csv.reader(f)
		for row in reader:
			X.append(row)
			y.append(1)
	#print("training input data: " + str(X))
	#print()
	#print("training output data: " + str(y))
	#print()
	return np.asarray(X), np.asarray(y)



def lookup(userID):
	api = get_api(key[0], key[1], key[2], key[3])

	X = get_data(userID, api)
	#print()
	#print("user input:" + str(X))
	#print()
	return np.asarray(X)

def main():
	twitter_user_name = sys.argv[1].lstrip().rstrip()

	# read the learned classifier from the file system, or create it if it does not exist
	file_name = './learned_classifier.p'
	rfc = Classifier()
	if os.path.isfile(file_name):
		rfc.import_from_file(file_name)
	else:
	# learn the classifier
	# extract our features and class label from the raw data
		X, y = get_training_data()

		# split data into training and test data
		X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, train_size=0.66, random_state=42)
		rfc.learn(X_train, y_train, 22)
		rfc.export(file_name)   # save the classifier to disk

		# predict
		predicted_class_labels = rfc.predict(X_test)

		# calculate the accuracy of the classifier
		accuracy = rfc.get_classifier_accuracy(predicted_class_labels, y_test)
		print(accuracy)

	# run user input through classifier
	print("mining twitter data...")
	input_data = lookup(twitter_user_name)
	print("done!")
	print("predicting...\n")
	result = rfc.predict(input_data)
	if result[0] == 1:
		print("your account is a bot")
	else:
		print("your account is a human")


	# plot the decision boundaries
	# xlabel = iris.feature_names[first_feature]
	# ylabel = iris.feature_names[second_feature]
	# X_combined = np.vstack((X_train, X_test))
	# y_combined = np.hstack((y_train, y_test))
	# test_start = X_train.shape[0]   # use these values to highlight the test data on the graph
	# test_end = X_combined.shape[0]

	# visualize_decision_regions(X_combined, y_combined, xlabel, ylabel, rfc, test_idx=range(test_start, test_end))

if __name__ == '__main__':
	main()
