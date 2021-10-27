import numpy as np

from sklearn import datasets
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import confusion_matrix

bc = datasets.load_breast_cancer()
data = bc['data']
target = bc['target']
test_ind = np.random.randint(0, len(target), round(len(target)/5))
train_ind = np.setdiff1d(range(len(target)), target)

classifier = KNeighborsClassifier(n_neighbors=5)
classifier.fit(data[train_ind, :], target[train_ind])

predicted = classifier.predict(data[test_ind, :])
cm = confusion_matrix(target[test_ind], predicted)