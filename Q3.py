import pickle
import numpy as np
import matplotlib.pyplot as plt


def calc_feats(ecg: np.array) -> ():
    """:param ecg: Signal peak values"""
    # Calculate forward difference between samples
    diff_for = [i-j for i, j in zip(ecg[:-1], ecg[1:])]
    # Calculate backward differnce between samples
    diff_back = [-1 * diff_for[2]] + [-1*x for x in diff_for]
    diff_for.append(diff_for[0])
    return diff_for, diff_back


# Read pickle data file
with open('peak-data.pkl', 'rb') as file:
    data = pickle.load(file)
# Get filtered data
data['ecg'] = data['ecg'][data['indices']]
# Calculate features of interest
feat = calc_feats(data['ecg'])
# Plot, label, save
fig, ax = plt.subplots()
colours = ['r', 'b', 'g']
for i, cls in enumerate(set(data['labels'])):
    idx = np.where(data['labels'] == cls)[0]
    ax.scatter(np.array(feat[0])[idx], np.array(feat[1])[idx], c=colours[i], label=cls)
ax.legend()
ax.grid(True)
plt.xlabel('Forward Difference Between Samples')
plt.ylabel('Backward Difference Between Samples')
plt.show()
plt.savefig('peak_classification.png')
