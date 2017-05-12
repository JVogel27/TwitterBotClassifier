from mlxtend.plotting import plot_decision_regions
from matplotlib.colors import ListedColormap
import matplotlib.pyplot as plt
import numpy as np
from math import floor
from classifier import Classifier


# def plot_decision_regions(X, y, classifier, test_idx=None, resolution=0.02):
# 	"""
# 	utility function to visualize the decision boundaries between two features
# 	:param X: 2D array of the input data to graph
# 	:param y: 1D vector of the class labels
# 	:param classifier: the trained classifier to use
# 	:param test_idx: range of indices that contain test data points
# 	:param resolution: hyper parameter
# 	:return: N/A
# 	"""
# 	print("SHAPE X: ", X.shape)
# 	# setup marker generator and color map
# 	markers = ('s', 'x', 'o', '^', 'v')
# 	colors = ('red', 'blue', 'lightgreen', 'gray', 'cyan')
# 	cmap = ListedColormap(colors[:len(np.unique(y))])
# 	# plot the decision surface
# 	x1_min, x1_max = X[:, 0].min() - 1, X[:, 0].max() + 1
# 	x2_min, x2_max = X[:, 1].min() - 1, X[:, 1].max() + 1
# 	delta_max = min((x1_max - x1_min), (x2_max - x2_min))
# 	resolution = delta_max/100
# 	grid1 = np.arange(x1_min, x1_max, resolution)
# 	grid2 = np.arange(x2_min, x2_max, resolution)
# 	print("SHAPE grid1: ", grid1.shape )
# 	print("SHAPE grid2: ", grid2.shape )
# 	xx1, xx2 = np.meshgrid(grid1, grid2)
# 	print("SHAPE xx1: ", xx1.shape)
# 	print("SHAPE xx2: ", xx2.shape)
# 	#Z = classifier.predict(np.array([xx1.ravel(), xx2.ravel()]).T)
# 	Z = classifier.predict(X)
# 	print("SHAPE Z: ", Z.shape)
# 	#Z = Z.reshape(1, -1)
# 	Z = Z.reshape(xx1.shape)
# 	print("NEW SHAPE: ", Z.shape)
# 	print("done")
# 	plt.contourf(xx1, xx2, Z, alpha=0.4, cmap=cmap)
# 	plt.xlim(xx1.min(), xx1.max())
# 	plt.ylim(xx2.min(), xx2.max())
# 	print("done!")

# 	# plot all samples
# 	print("plotting all samples")
# 	for idx, cl in enumerate(np.unique(y)):
# 		plt.scatter(x=X[y == cl, 0], y=X[y == cl, 1],
# 		alpha=0.8, c=cmap(idx),
# 		marker=markers[idx], label=cl)
# 	print("done")

# 	# highlight test samples
# 	print("highlighting test samples")
# 	if test_idx:
# 		X_test, y_test = X[test_idx, :], y[test_idx]
# 		plt.scatter(X_test[:, 0], X_test[:, 1], c='',
# 			alpha=1.0, linewidth=1, marker='o',
# 			s=55, label='test set')
# 	print("done")


def visualize_decision_regions(X_train, X_test, y_train, y_test):
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

	labels = [
		"Age of Account",								# 0		
		"Ratio of Followers to Friends",				# 1
		"Ratio of Favourites to age",	 				# 2
		"Ratio of Statuses to age",						# 3
		"Ratio of Followers to Followers and Friends",	# 4
		"Ratio of URLs",								# 5
		"Frequency of Monday Posts",					# 6
		"Frequency of Tuesday Posts",					# 7
		"Frequency of Wednesday Posts",					# 8 
		"Frequency of Thursday Posts",					# 9
		"Frequency of Friday Posts",					# 10
		"Frequency of Saturday Posts",					# 11
		"Frequency of Sunday Posts",					# 12
		"Average Number of Tweets per day",				# 13
		"Ratio of Hashtags",							# 14
		"Ratio of User Mentions",						# 15
		"Ratio of Malicious urls"						# 16
	]

	graphs = [
		#(0, 1),
		# (0, 2),
		# (0, 3),
		# (0, 4),
		# (0, 5),
		# (0, 13),
		# (0, 14),
		# (0, 15),
		# (0, 16),
		# (1, 2),
		# (1, 3),
		# (1, 4),
		# (1, 5),
		# (1, 13),
		# (1, 14),
		# (1, 15),
		# (1, 16),
		# (2, 3),
		(2, 4),
		(2, 5),
		#(2, 13),
		(2, 14),
		(2, 15),
		(2, 16),
		(3, 4),
		(3, 5),
		#(3, 13),
		(3, 14), #...
		(3, 15),
		(3, 16),
		(4, 5),
		#(4, 13),
		(4, 14),
		(4, 15),
		(4, 16),
		#(5, 13),
		(5, 14),
		(5, 15),
		(5, 16),
		(13, 14),
		(13, 15),
		(13, 16),
		(14, 15),
		(14, 16),
		(15, 16)
	]

	X_combined = np.vstack((X_train, X_test))
	y_combined = np.hstack((y_train, y_test))

	# convert to numpy arrays
	X_train = np.array(X_train)
	X_combined = np.array(X_combined).astype(np.float)
	y_combined = np.array(y_combined).reshape(1, -1)

	test_start = X_train.shape[0]   # use these values to highlight the test data on the graph
	test_end = X_combined.shape[0]

	for (i, j) in graphs:
		print(i, j)
		XX_train = np.array(X_train).astype(np.float)[:, [i, j]]
		XX_test = np.array(X_test).astype(np.float)[:, [i, j]]
		x1_min = XX_test[:, 0].min() - 1
		x1_max = XX_test[:, 1].max() + 1
		x2_min = XX_test[:, 0].min() - 1
		x2_max = XX_test[:, 1].max() + 1

		delta_max = max(abs(x1_max - x1_min), abs(x2_max - x2_min))
		resolution = (floor(delta_max)/100)

		print(delta_max, resolution)

		classifier = Classifier()
		print("learning...")
		classifier.learn(XX_train, y_train, 22)
		print("predicting...")
		predicted_classes = classifier.predict(XX_test)
		print("plotting...")
		plot_decision_regions(XX_test, np.array(y_test).astype(np.integer), clf=classifier)
		print("done!")
		plt.xlabel(labels[i])
		plt.ylabel(labels[j])
		#plt.legend(loc='upper left')
		filename = "./figs/figure_" + str(i) + "_" + str(j)
		plt.savefig(filename)
		plt.clf()






