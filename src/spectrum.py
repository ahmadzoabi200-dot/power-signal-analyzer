import numpy as np
import scipy.signal as signal

def compute_fft(x, fs, window='hann'):
    N = len(x)
    w = signal.get_window(window, N)
    X = np.fft.rfft(x * w)
    freqs = np.fft.rfftfreq(N, 1/fs)
    mag_rms = np.abs(X) / (np.sqrt(2) * (N/2))
    return freqs, mag_rms
