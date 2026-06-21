import scipy.signal as signal

def design_notch(f0, Q, fs):
    b, a = signal.iirnotch(f0, Q, fs)
    return signal.tf2sos(b, a)

def design_lowpass(fc, order, fs):
    return signal.butter(order, fc, btype='low', fs=fs, output='sos')

def apply_filter(sos, x):
    return signal.sosfilt(sos, x)
