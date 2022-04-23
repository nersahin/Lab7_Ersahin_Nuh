import numpy as np
from scipy import fftpack, signal
from matplotlib import pyplot as plt
import pandas as pd
from scipy.io import wavfile
import sys, os, os.path

time_step=1/44100
noise_amplitude=0.25
noise_amplitude2=0.5


#plotting signal 1
frequency_1=322 #1Hz
Tperiod_1 = 1/frequency_1
time_vec = np.arange(0, 1, time_step)
signal1 = 1000*(np.sin(2 * np.pi / Tperiod_1 * time_vec))
plt.figure(figsize=(20,10))
plt.title('322Hz Signal', fontsize=35)
plt.ylabel('Amplitude', fontsize=25)
plt.xlabel('Time (s)', fontsize=25)
plt.xticks(fontsize=20)
plt.yticks(fontsize=20)
plt.xlim(0,.01)
plt.plot(time_vec, signal1)

#plotting Signal 2
frequency_2=555 #1Hz
Tperiod_2 = 1/frequency_2
time_vec = np.arange(0, 1, time_step)
signal2 = noise_amplitude*1000*(np.sin(2 * np.pi / Tperiod_2 * time_vec))
plt.figure(figsize=(20,10))
plt.title('555Hz Signal', fontsize=35)
plt.ylabel('Amplitude', fontsize=25)
plt.xlabel('Time (s)', fontsize=25)
plt.xticks(fontsize=20)
plt.yticks(fontsize=20)
plt.xlim(0,.01)
plt.plot(time_vec, signal2)

#Plotting signal 3
frequency_3=663 #1Hz
Tperiod_3 = 1/frequency_3
time_vec = np.arange(0, 1, time_step)
signal3 = noise_amplitude2*1000*(np.sin(2 * np.pi / Tperiod_3 * time_vec))
plt.figure(figsize=(20,10))
plt.title('663Hz Signal', fontsize=35)
plt.ylabel('Amplitude', fontsize=25)
plt.xlabel('Time (s)', fontsize=25)
plt.xticks(fontsize=20)
plt.yticks(fontsize=20)
plt.xlim(0,.01)
plt.plot(time_vec, signal3)

#Combining the 3 signals on one plot
sig = signal1 + signal2 + signal3
plt.figure(figsize=(60,30))
plt.title('Combined Signals (322Hz, 555Hz, 663Hz)', fontsize=80)
plt.ylabel('Amplitude', fontsize=60)
plt.xlabel('Time (s)', fontsize=60)
plt.xticks(fontsize=55)
plt.yticks(fontsize=55)
plt.xlim(0,1)
plt.plot(time_vec, sig)

#Turns the combnined signials into a wav file
wavfile.write('Combined.wav', 44100, sig.astype(np.int16))

sig_fft = fftpack.fft(sig)
power = np.abs(sig_fft)**2
sample_freq = fftpack.fftfreq(sig.size, d=time_step)
plt.figure(figsize=(60, 30))
plt.title('Signal in Frequency Domain', fontsize=80)
plt.ylabel('Power', fontsize=60)
plt.xlabel('Frequency (Hz)', fontsize=60)
plt.xticks(fontsize=55)
plt.yticks(fontsize=55)
plt.xlim(-1000,1000)
plt.plot(sample_freq, power)


#Finding the peak frequency
pos_mask = np.where(sample_freq > 0)
freqs = sample_freq[pos_mask]
peak_freq = freqs[power[pos_mask].argmax()]


# filter out high frequencies
high_freq_fft = sig_fft.copy()
high_freq_fft[np.abs(sample_freq) > peak_freq] = 0
filtered_sig = fftpack.ifft(high_freq_fft)

#turns the filtered signal into a wav file
wavfile.write('Filtered.wav', 44100, filtered_sig.astype(np.int16))


#FFT of the graph
plt.figure(figsize=(60,30))
plt.title('Original and Filtered Time Domain Signals', fontsize=80)
plt.plot(time_vec, sig, label='Original signal')
plt.plot(time_vec, filtered_sig, linewidth=5, label='Filtered signal')
plt.xlabel('Time (s)', fontsize=60)
plt.ylabel('Amplitude', fontsize=60)
plt.xticks(fontsize=55)
plt.yticks(fontsize=55)
plt.xlim(0,.01)
plt.legend(loc='best')
sig_fft1 = fftpack.fft(filtered_sig)
power = np.abs(sig_fft1)**2
sample_freq = fftpack.fftfreq(filtered_sig.size, d=time_step)

#FFT of the filtered graph
plt.figure(figsize=(60, 30))
plt.title('Filtered Signal in Frequency Domain', fontsize=80)
plt.ylabel('Power', fontsize=60)
plt.xlabel('Frequency (Hz)', fontsize=60)
plt.xticks(fontsize=55)
plt.yticks(fontsize=55)
plt.xlim(-1500,1500)
plt.plot(sample_freq, power)

