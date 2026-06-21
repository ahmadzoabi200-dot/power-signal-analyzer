import matplotlib.pyplot as plt
from src.signals import make_signal
from src.spectrum import compute_fft
from src.thd import thd_from_spectrum
from src.filters import design_lowpass, apply_filter

def main():
    fs, f1, T = 5000, 50, 1.0
    harmonics = [(3, 0.15), (5, 0.07)]
    t, x = make_signal(fs, T, f1, harmonics, noise_sigma=0.01)

    freqs, mag = compute_fft(x, fs)
    thd_before = thd_from_spectrum(freqs, mag, f1)
    print(f"THD before filtering: {thd_before*100:.2f}%")

    # AFTER:
    from scipy.signal import sosfiltfilt
    sos = design_lowpass(120, 6, fs)  # lower fc, higher order
    y = sosfiltfilt(sos, x)  # zero-phase filtering
    freqs2, mag2 = compute_fft(y, fs)
    thd_after = thd_from_spectrum(freqs2, mag2, f1)
    print(f"THD after filtering: {thd_after*100:.2f}%")

    plt.figure(figsize=(10, 5))
    plt.subplot(2, 1, 1)
    plt.plot(t, x, label='Original')
    plt.plot(t, y, label='Filtered', alpha=0.8)
    plt.legend()
    plt.title("Time Domain")

    plt.subplot(2, 1, 2)
    plt.semilogy(freqs, mag, label='Original')
    plt.semilogy(freqs2, mag2, label='Filtered')
    plt.legend()
    plt.title("Frequency Spectrum")
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()
