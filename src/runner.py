from classifier import Classifier
from sklearn import datasets
from sklearn.model_selection import train_test_split
import numpy as np


def main():
	# iris = datasets.load_iris()
	# X = iris.data[:, [2, 3]]
	# y = iris.target
	# TODO add our own data
	X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42)
	rfc = Classifier()
	rfc.learn(X_train, y_train)
	predicted_class_labels = rfc.predict(X_test)
	accuracy = rfc.get_classifier_accuracy(predicted_class_labels, y_test)
	print(accuracy)

if __name__ == '__main__':
	main()
