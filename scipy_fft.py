import numpy as np
from scipy.fftpack import fft, ifft
import matplotlib.pyplot as plt

x = np.linspace(0, 1, 1400)
y = 1 * np.sin(180 * 2 * np.pi * x) + 2 * np.sin(390 * 2 * np.pi * x) + 3 * np.sin(600 * 2 * np.pi * x)

yy = fft(y)
yreal = yy.real
yimag = yy.imag

# yf = abs(fft(y))                # 取绝对值
# yf1 = abs(fft(y))/len(x)        # 归一化处理
# yf2 = yf1[range(int(len(x)/2))]  # 由于对称性，只取一半区间

yf = fft(y)
yf1 = fft(y)/len(x)
yf2 = yf1[range(int(len(x)/2))]

xf = np.arange(len(y))
xf1 = xf
xf2 = xf[range(int(len(x)/2))]

plt.subplot(221)
plt.plot(x[0:50], y[0:50])
plt.title('Original wave')

plt.subplot(222)
plt.plot(xf, yf, 'r')
plt.title('FFT of Mixed wave(two sides frequency range)', fontsize=7, color='#7A378B')

plt.subplot(223)
plt.plot(xf1, yf1, 'g')
plt.title('FFT of Mixed wave(normalization)', fontsize=9, color='r')

plt.subplot(224)
plt.plot(xf2, yf2, 'b')
plt.title('FFT of Mixed wave)', fontsize=10, color='#F08080')

plt.show()