from matplotlib.colors import ListedColormap
import matplotlib.pyplot as plt
import numpy as np


def plot_decision_regions(X, y, classifier, test_idx=None, resolution=0.02):
	"""
	utility function to visualize the decision boundaries between two features
	:param X: 2D array of the input data to graph
	:param y: 1D vector of the class labels
	:param classifier: the trained classifier to use
	:param test_idx: range of indices that contain test data points
	:param resolution: hyper parameter
	:return: N/A
	"""
	# setup marker generator and color map
	markers = ('s', 'x', 'o', '^', 'v')
	colors = ('red', 'blue', 'lightgreen', 'gray', 'cyan')
	cmap = ListedColormap(colors[:len(np.unique(y))])

	# plot the decision surface
	x1_min, x1_max = X[:, 0].min() - 1, X[:, 0].max() + 1
	x2_min, x2_max = X[:, 1].min() - 1, X[:, 1].max() + 1
	xx1, xx2 = np.meshgrid(np.arange(x1_min, x1_max, resolution),
	np.arange(x2_min, x2_max, resolution))
	Z = classifier.predict(np.array([xx1.ravel(), xx2.ravel()]).T)
	Z = Z.reshape(xx1.shape)
	plt.contourf(xx1, xx2, Z, alpha=0.4, cmap=cmap)
	plt.xlim(xx1.min(), xx1.max())
	plt.ylim(xx2.min(), xx2.max())

	# plot all samples
	for idx, cl in enumerate(np.unique(y)):
		plt.scatter(x=X[y == cl, 0], y=X[y == cl, 1],
		alpha=0.8, c=cmap(idx),
		marker=markers[idx], label=cl)

	# highlight test samples
	if test_idx:
		X_test, y_test = X[test_idx, :], y[test_idx]
		plt.scatter(X_test[:, 0], X_test[:, 1], c='',
			alpha=1.0, linewidth=1, marker='o',
			s=55, label='test set')


def visualize_decision_regions(X, y, xlabel, ylabel, classifier_obj, test_idx=None):
	"""
	wrapper function for the plot_decision_regions function. Performs the graph configuration
	:param X: 2D array of the input data to graph
	:param y: 1D vector of the class labels
	:param xlabel:
	:param ylabel:
	:param classifier_obj: the trained classifier to use
	:param test_idx: range of indices that contain test data points
	:return: N/A
	"""
	plot_decision_regions(X, y, classifier_obj, test_idx)
	plt.xlabel(xlabel)
	plt.ylabel(ylabel)
	plt.legend(loc='upper left')
	plt.show()