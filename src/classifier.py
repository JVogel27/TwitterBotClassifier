from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score


class Classifier():
	"""
	A wrapper class for some of the sci-kit functionality.
	"""
	def __init__(self):
		self.forest = None

	def learn(self, x_train, y_train):
		"""
		create and train the random forest classifier
		:param x_train: the input training data
		:param y_train: the input class labels
		:return: n/a
		"""
		self.forest = RandomForestClassifier(criterion='entropy', n_estimators=10, random_state=1, n_jobs=2)
		self.forest.fit(x_train, y_train)

	def predict(self, x):
		"""
		wrapper for the RandomForestClassifier predict method
		:param x: the input data for the classifier
		:return: array of class labels
		"""
		if self.forest:
			return self.forest.predict(x)
		else:
			return None

	@staticmethod
	def get_classifier_accuracy(y_true, y_prediction):
		"""
		get the overall accuracy of the learned model
		:param y_true: the ground truth (correct labels)
		:param y_prediction: the predicted labels as returned from the classifier
		:return: overall accuracy normalized as a decimal between 0.0 and 1.0
		"""
		return accuracy_score(y_true, y_prediction)


