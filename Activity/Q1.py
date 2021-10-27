import numpy as np
import matplotlib.pyplot as plt

from sklearn import datasets

iris = datasets.load_iris()

data = iris['data']
target = iris['target']
plt.scatter(data[:,2], data[:, 3], marker='.', c=target)

# Equation of boundary is ~ y = -5/12x + 1.25
discriminant = np.array([2, 1])
discriminant = discriminant / np.linalg.norm(discriminant)
projections = np.matmul(data[:, 2:], discriminant)

threshold = 2.5
ind = np.where(projections < threshold)

threshold_point = threshold * discriminant
boundary_direction = np.array([discriminant[1], -discriminant[0]])  # orthogonal
a = threshold_point + boundary_direction
b = threshold_point - boundary_direction
plt.plot([a[0], b[0]], [a[1], b[1]], 'k')

plt.scatter(data[ind, 2], data[ind, 3], marker='*')
plt.axis('equal')
plt.show()
