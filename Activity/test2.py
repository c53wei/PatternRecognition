import numpy as np


def find_qrs(ecg):
    y2 = np.zeros(len(ecg))
    indices = []

    for i in range(5, len(ecg)):
        y2, qrs = is_peak(ecg, i, y2)

        if qrs and (len(indices) == 0 or i > indices[-1] + 50):
            indices.append(i)

    return indices


def is_peak(ecg: np.array, i: int, y2: np.array) -> ():
    """Assesses if given index in ecg signal is a peak
    :param ecg: Array of ecg data
    :param i: Index of interest
    :param y2: Array of previously computed data to be filled in"""
    y0 = abs(ecg[i] - ecg[i-2])
    y1 = abs(ecg[i] - 2*ecg[i-2] + ecg[i-4])
    y2[i] = 1.3*y0 + 1.1*y1
    y3 = sum(y2[max(0,i-9):i+1])

    return y2, y3>5

def zero_crossings(signal):
    crossings = np.logical_and(signal[:-1] <= 0, signal[1:] > 0)
    return np.array(np.where(crossings)) + 1
