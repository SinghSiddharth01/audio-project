from pprint import pprint as pp
import numpy as np
from scipy.io import wavfile
from scipy.fft import fft as FFT
from scipy import signal
import matplotlib.pyplot as plt
from matplotlib import cm # colour map
# from IPython.display import Audio

def read_wav_file(filename):
    sample_rate, samples = wavfile.read(filename)
    num_channels = samples.shape[1]
    return samples, sample_rate, num_channels


# https://publish.illinois.edu/augmentedlistening/tutorials/music-processing/tutorial-1-introduction-to-audio-processing-in-python/
def plot_AmpT(data, to_file=False, filename='test.png', xlabel='Time', ylabel='Amplitude'):
    plt.figure()
    plt.plot(data)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    if to_file:
        plt.savefig(filename)
    else:
        plt.show()

# Working Example of Spectogram with Filter
# https://stackoverflow.com/questions/56788798/python-spectrogram-in-3d-like-matlabs-spectrogram-function
# basic config
def filter_spectogram_example():
    fs = 11240.
    t = 10
    time = np.arange(fs*t) / fs
    frequency = 1000.
    mysignal = np.sin(2.0 * np.pi * frequency * time)

    nperseg = 2**14
    noverlap = 2**13
    f, t, Sxx = signal.spectrogram(mysignal, fs, nperseg=nperseg,noverlap=noverlap)

    myfilter = (f>800) & (f<1200)

    f = f[myfilter]
    Sxx = Sxx[myfilter, ...]

    fig = plt.figure()
    ax = fig.gca(projection='3d')

    ax.plot_surface(f[:, None], t[None, :], 10.0*np.log10(Sxx), cmap=cm.coolwarm)
    plt.show() 

# Attempt to Draw a spectrogram --- NOT WORKING!
# https://stackoverflow.com/questions/44787437/how-to-convert-a-wav-file-to-a-spectrogram-in-python3
# frequencies, times, spectrogram = signal.spectrogram(samples, sample_rate)
# plt.pcolormesh(times, frequencies, spectrogram)
# plt.imshow(spectrogram)
# plt.ylabel('Frequency [Hz]')
# plt.xlabel('Time [sec]')
# plt.show()

samples, sample_rate, num_channels = read_wav_file('test.wav')


b, a = signal.iirfilter(2, 500, btype='lowpass', analog=True, ftype='butter')
w, h = signal.freqs(b, a, 1000)
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
ax.semilogx(w / (2*np.pi), 20 * np.log10(np.maximum(abs(h), 1e-5)))
ax.set_title('Chebyshev Type II bandpass frequency response')
ax.set_xlabel('Frequency [Hz]')
ax.set_ylabel('Amplitude [dB]')
ax.axis((10, 1000, -100, 10))
ax.grid(which='both', axis='both')
plt.show()


# Left Channel
#plot_AmpT(samples[:,0])
# Right Channel
#plot_AmpT(samples[:,1])