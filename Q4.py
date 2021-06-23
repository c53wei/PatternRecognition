import pickle
import numpy as np
import matplotlib.pyplot as plt

from Q3 import calc_feats

# Read pickle data file
with open('peak-data.pkl', 'rb') as file:
    data = pickle.load(file)
# Get filtered data
data['ecg'] = data['ecg'][data['indices']]
# Calculate features of interest
x, y = calc_feats(data['ecg'])

# Get indices of all class 1s
pred_label_1_idx = np.where(y > -x)
# Formatting labels
pred_labels = np.array(['Not Class 1'] * len(y))
pred_labels[pred_label_1_idx] = 'Class 1'
# Plot, label, save
fig, ax = plt.subplots()
colours = ['r', 'b', 'g']
for i, cls in enumerate(set(pred_labels)):
    idx = np.where(pred_labels == cls)[0]
    ax.scatter(x[idx], y[idx], c=colours[i], label=cls)
ax.legend()
ax.grid(True)
# Boundary line is y = -x
# (2, -2) and (-2, 2) are on this line
plt.plot([2, -2], [-2, 2], c='black')
plt.title('Predicted Labels')
plt.xlabel('Forward Difference Between Samples')
plt.ylabel('Backward Difference Between Samples')
plt.savefig('manual_classifier.png')
plt.show()
plt.close()


