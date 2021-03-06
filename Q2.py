import pickle
import numpy as np
import matplotlib.pyplot as plt

from scipy import signal

# Part d function
def find_Tpeaks(data: np.array):
    return signal.find_peaks(data, height=[5.5, 6], threshold=0, distance=35)[0]

# Part e function
def find_better_Tpeaks(data: np.array) -> list:
    """
    Returns the indices of T peaks in an ECG signal
    :type data: np.array
    :param data: Values of ECG signal
    :return: List of indices where T peaks occur
    """
    # Extract all indices of peaks with a minimum prominence of 0.25
    # This extracts P, R, & T peak indices
    all_peaks = signal.find_peaks(data, height=0, prominence=0.25)[0]
    # Find indices of R peaks only as they serve as an easy landmark
    R_peaks = signal.find_peaks(data, height=6)[0]
    # Find indices of all_peaks that contain an R peak
    R_peak_in_all_indices = np.nonzero(np.in1d(all_peaks,R_peaks))[0]
    # T peaks occur one 'pulse' after an R or 2 pulses before
    # Use this information to find unique values of T peak indices
    t_peaks = [all_peaks[R+1] for R in R_peak_in_all_indices]
    t_peaks.extend([all_peaks[R-2] for R in R_peak_in_all_indices if R-2 >= 0])
    t_peaks = list(set(t_peaks))
    # Return T peak indices of interest
    return t_peaks


# Question Two: Python Problem Solving
# a) Load the file 106m.pkl from Learn, using pickle. This file contains an ECG signal.
with open('106m.pkl', 'rb') as file:
    data = np.array(pickle.load(file))/200
# b) Plot the first five seconds of the ECG signal in mV vs. time in seconds and label the axes.
#    Note that the sampling rate is 360 samples/s. Dividing the signal by 200 will give the signal
#    in mV. You should put the data in a numpy ndarray to conveniently divide these values.
n_samples = 360*5
time = np.linspace(0, n_samples/360, n_samples)
ecg5 = data[:n_samples]
plt.plot(time, ecg5)
plt.xlabel('Time (s)')
plt.ylabel('Signal Value (mV)')

# c) Using scipy.signal.find_peaks(), plot blue x’s at the peaks of the P, R, and T waves in the
# signal (and nowhere else).
peaks = signal.find_peaks(ecg5, height=0, prominence=0.25)[0]
plt.plot(time[peaks], ecg5[peaks], color = 'b', marker='x', linestyle='None')

# d) Write a function that returns the peaks of T waves only. Your function can call find_peaks().
#     Plot the signal again with red x’s at the peaks of the T waves.
T_peaks = find_Tpeaks(ecg5)
plt.plot(time[T_peaks], ecg5[T_peaks], color = 'r', marker='x', linestyle='None')
plt.savefig('5s.png')
plt.close()

# e) Plot the signal from 20-25s, run your code from (d) on this part of the signal, and plot red
# x’s at the returned indices. The signal at this point is different enough that the function you
# designed for the earlier part of the signal probably will not work well. Write a more robust
# function. Submit the code for this function, along with new plots to show that it works for
# both the 0-5s and 20-25s signals.
time = np.linspace(20, 20 + n_samples/360, n_samples)
ecg20 = data[20*360:25*360]
plt.plot(time, ecg20)
plt.xlabel('Time (s)')
plt.ylabel('Signal Value (mV)')

tpeak_indices = find_better_Tpeaks(ecg20)
plt.plot(time[tpeak_indices], ecg20[tpeak_indices], color = 'r', marker='x', linestyle='None')

plt.savefig('20s.png')
plt.close()