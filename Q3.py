import pickle
import matplotlib.pyplot as plt

def features(ecg):
    diff_for = [i-j for i, j in zip(ecg[:-1], ecg[1:])]

    diff_back = [-1 * diff_for[2]] + [-1*x for x in diff_for]
    diff_for.append(diff_for[0])
    return diff_for, diff_back

with open('peak-data.pkl', 'rb') as file:
    data = pickle.load(file)

data['ecg'] = data['ecg'][data['indices']]
feat = features(data['ecg'])
plt.scatter(feat[0], feat[1], c=data['labels'])

# plt.savefig('true.png')
