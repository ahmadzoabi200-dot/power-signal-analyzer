import numpy as np

def make_signal(fs=5000, T=1.0, f1=50, harmonics=None, noise_sigma=0.0, dc=0.0):
    """
    Generate a waveform with a fundamental, harmonics, noise, and DC offset.
    """
    t = np.arange(0, T, 1/fs)
    x = np.sin(2 * np.pi * f1 * t)
    if harmonics:
        for n, a in harmonics:
            x += a * np.sin(2 * np.pi * f1 * n * t)
    if noise_sigma > 0:
        x += np.random.normal(0, noise_sigma, len(t))
    x += dc
    return t, x
