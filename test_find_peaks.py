import pytest
import pickle
import numpy as np

from Q2 import find_Tpeaks, find_better_Tpeaks
from Q3 import calc_feats


@pytest.fixture()
def ecg_data():
    """
    :return: Numpy array of ecg data in mV
    """
    with open('106m.pkl', 'rb') as file:
        data = np.array(pickle.load(file))/200
    return data


def test_find_Tpeaks(ecg_data):
    """
    Tests function to accurately find T peaks
    :param ecg_data: Numpy array of ecg data in mV
    """
    # Get number of data points needed to find first 5 seconds
    n_samples = 360*5
    peaks = find_Tpeaks(ecg_data[:n_samples])
    assert len(peaks) == 5  # Correct number of peaks identified
    assert isinstance(peaks, np.ndarray)  # Returns array for easy slicing
    # Returns indices as expected
    assert set(peaks) == {57,  448,  818, 1183, 1550}, \
            "Incorrect peak indices found"

def test_find_better_Tpeaks(ecg_data):
    """
    Tests function to accurately find T peaks in improved function
    :param ecg_data: Numpy array of ecg data in mV
    """
    # Get peaks between 20 and 25 seconds
    peaks = find_better_Tpeaks(ecg_data[20*360:25*360])
    assert len(peaks) == 6  # Correct number of peaks identified
    # Returns indices as expected
    assert set(peaks) == {1382, 230, 1077, 1658, 794, 507}, \
        "Incorrect peak indices found"


def test_calc_feats():
    """Tests feature calculation of prominent ecg data"""
    # Read class data
    with open('peak-data.pkl', 'rb') as file:
        ecg_data = pickle.load(file)
    ecg_data['ecg'] = ecg_data['ecg'][ecg_data['indices']]
    # Calculate forward and backward differences between signal data
    x, y = calc_feats(ecg_data['ecg'][:20])
    # Check that changes in mV are consistent regardless of reference direction
    for idx, value in enumerate(x[:19]):
        assert value == -y[idx+1], \
        f'Forward difference at index {idx} does not equal to \
        backward difference in adjacent index'