import numpy as np
import pylab as pl

def fft_combine(freqs, n, loops=1):
    length = len(freqs) * loops
    data = np.zeros(length)
    index = loops * np.arange(0, length, 1.0) / length * (2 * np.pi)
    for k, p in enumerate(freqs[:n]):
        if k != 0: p *= 2 # 除去直流成分之外，其余的系数都*2
        data += np.real(p) * np.cos(k*index)
        data -= np.imag(p) * np.sin(k*index)
    return index, data

def triangle_wave(size):
    x = np.arange(0, 1, 1.0/size)
    y = np.where(x<0.5, x, 0)
    y = np.where(x>=0.5, 1-x, y)
    return x, y

fft_size = 250

x, y = triangle_wave(fft_size)
fy = np.fft.fft(y) / fft_size

pl.figure()
pl.plot(np.clip(20 * np.log10(np.abs(fy[:20])), -120, 120), "o")
pl.xlabel("frequency bin")
pl.ylabel("power(dB)")
pl.title("FFT result of triangle wave")

pl.figure()
pl.plot(y, label="original triangle", linewidth=2)
for i in [0,1,3,5,7,9]:
    index, data = fft_combine(fy, i+1, 2)  # 计算两个周期的合成波形
    pl.plot(data, label = "N=%s" % i)
pl.legend()
pl.title("partial Fourier series of triangle wave")
pl.show()