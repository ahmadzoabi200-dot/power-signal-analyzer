import numpy as np

def thd_from_spectrum(freqs, mag_rms, f1, max_harm=25):
    fund_bin = np.argmin(np.abs(freqs - f1))
    V1 = mag_rms[fund_bin]
    harmonics = []
    for n in range(2, max_harm + 1):
        idx = np.argmin(np.abs(freqs - n * f1))
        harmonics.append(mag_rms[idx])
    Vh = np.sqrt(np.sum(np.square(harmonics)))
    return Vh / V1
