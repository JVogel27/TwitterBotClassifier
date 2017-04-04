from classifier import Classifier
from sklearn import datasets
from sklearn.model_selection import train_test_split
import numpy as np
from visualize import visualize_decision_regions


def main():
	# the data visualization graph only works for two features, so specify which ones to use
	first_feature = 2
	second_feature = 3

	# extract our features and class label from the raw data
	# TODO add our own data
	iris = datasets.load_iris()
	X = iris.data[:, [first_feature, second_feature]]
	y = iris.target

	# split data into training and test data
	X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, train_size=0.66, random_state=42)

	# create, train, then predict with our classifier
	rfc = Classifier()
	rfc.learn(X_train, y_train, 22)
	predicted_class_labels = rfc.predict(X_test)

	# calculate the accuracy of the classifier
	accuracy = rfc.get_classifier_accuracy(predicted_class_labels, y_test)
	print(accuracy)

	# plot the decision boundaries
	xlabel = iris.feature_names[first_feature]
	ylabel = iris.feature_names[second_feature]
	X_combined = np.vstack((X_train, X_test))
	y_combined = np.hstack((y_train, y_test))
	test_start = X_train.shape[0]   # use these values to highlight the test data on the graph
	test_end = X_combined.shape[0]
	visualize_decision_regions(X_combined, y_combined, xlabel, ylabel, rfc, test_idx=range(test_start, test_end))

if __name__ == '__main__':
	main()