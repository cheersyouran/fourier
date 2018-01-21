#encoding:utf-8
import numpy as np
from sklearn import preprocessing
import matplotlib.pyplot as plt

a = [9.16,9.16,9.17,9.13,9.15,9.15,9.14,9.15,9.16,9.14,9.15,9.17,9.18,9.22,9.22,
     9.27,9.26,9.33,9.26,9.31,9.3,9.3,9.31,9.33,9.41,9.4,9.45,9.46,9.39,9.56]

b = [7.86,7.63,7.73,7.35,6.97,7.16,7.38,7.77,7.83,7.8,7.85,8.22,8.33,8.79,9.67,10.64,
     11.19,12.31,12.02,11.9,12.55,12.57,12.14,13.35,14.69,16.16,16.13,15.77,15.8,17.38]

c = [9.08,9.1,9.3,9.96,10.07,10.,10.54,10.99,10.9,10.66,10.59,11.02,11.13,10.84,
     9.99,9.8,9.38,9.58,9.42,9.81,9.88,9.79,9.77,10.12,10.06,10.09,10.01,10.09,10.41,10.13]

#target-fft
a = [ 10.26,9.91,9.88,9.99,9.96,10.13,10.12,9.93,10.15,10.,10.22
,10.37,10.71,10.56,10.67,10.8,10.6,11.1,11.79,11.65,11.57
,11.75,11.7,11.32,11.38,11.6,11.64,11.7,12.25,12.4 ]

# target-all
b = [ 5.8, 5.72,5.76,5.3, 5.46,5.03,5.03,4.99,5.01,4.72,4.72,4.87
,4.76,4.61,4.66,4.62,4.16,4.08,3.88,4.05,3.96,4.06,4.07,4.12
,4.04,4.01,4.17,4.24,4.27,4.26]

# pattern
c = [ 11.33,11.4,11.53,10.94,11.12,10.76,10.81,10.71,10.77,10.46
,10.41,10.71,10.54,10.32,10.4,10.37,9.87,9.88,9.69,10., 9.8
,9.95,9.85,9.95,9.92,9.79,10.01,10.15,10.09,10.04]


a = preprocessing.scale(a)
b = preprocessing.scale(b)
c = preprocessing.scale(c)

a1 = np.fft.fft(a)/len(a)
b1 = np.fft.fft(b)/len(b)
c1 = np.fft.fft(c)/len(c)


print(np.rad2deg(np.angle(a1[1])))
print(np.rad2deg(np.angle(b1[1])))
print(np.rad2deg(np.angle(c1[1])))

def get_first_frequency(a, b):
     a_abs = np.abs(a[1])
     b_abs = np.abs(b[1])
     return np.abs(a_abs - b_abs)

a_b = get_first_frequency(a1, b1)
a_c = get_first_frequency(a1, c1)
b_c = get_first_frequency(b1, c1)

print('第0频域:')
print(np.abs(a1[1]))
print(np.abs(b1[1]))
print(np.abs(c1[1]))

print('第0频域之差:')
print('a和b', a_b)
print('a和c', a_c)
print('b和c', b_c)

plt.plot(a, 'r-', label=a, linewidth=1.5)
plt.plot(b, 'k-', label=b, linewidth=1.5)
plt.plot(c, 'g-', label=c, linewidth=1.5)

plt.xlabel('Time')
plt.ylabel('Net Asset Value')

plt.grid(True)
plt.xticks(fontsize=8)
plt.ioff()

plt.show()
plt.close()

