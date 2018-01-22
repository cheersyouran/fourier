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

# target-fft
a = [5.76, 5.62, 5.8, 5.23, 5.35, 5.01, 5.13, 5.01, 5.13, 4.86, 4.91, 5.07, 5.04, 4.87, 4.92,
     4.99, 4.51, 4.43, 4.27, 4.39, 4.29, 4.42, 4.42, 4.53, 4.46, 4.43, 4.59, 4.64, 4.65, 4.63]

# target-all
b = [5.8, 5.72, 5.76, 5.3, 5.46, 5.03, 5.03, 4.99, 5.01, 4.72, 4.72, 4.87, 4.76, 4.61, 4.66,
     4.62, 4.16, 4.08, 3.88, 4.05, 3.96, 4.06, 4.07, 4.12, 4.04, 4.01, 4.17, 4.24, 4.27, 4.26]

# pattern
c = [11.33, 11.4, 11.53, 10.94, 11.12, 10.76, 10.81, 10.71, 10.77, 10.46, 10.41, 10.71, 10.54, 10.32,
     10.4, 10.37, 9.87, 9.88, 9.69, 10., 9.8, 9.95, 9.85, 9.95, 9.92, 9.79, 10.01, 10.15, 10.09, 10.04]


a = preprocessing.scale(a)
b = preprocessing.scale(b)
c = preprocessing.scale(c)

a1 = np.fft.fft(a)/len(a)
b1 = np.fft.fft(b)/len(b)
c1 = np.fft.fft(c)/len(c)


print('第1频域相位差:')
print('a:', np.rad2deg(np.angle(a1[1])))
print('b:', np.rad2deg(np.angle(b1[1])))
print('c:', np.rad2deg(np.angle(c1[1])))

print('第1频域振幅:')
print('a:', np.abs(a1[1]))
print('b:', np.abs(b1[1]))
print('c:', np.abs(c1[1]))

print('第2频域相位差:')
print('a:', np.rad2deg(np.angle(a1[1])))
print('b:', np.rad2deg(np.angle(b1[1])))
print('c:', np.rad2deg(np.angle(c1[1])))

print('第2频域振幅:')
print('a:', np.abs(a1[2]))
print('b:', np.abs(b1[2]))
print('c:', np.abs(c1[2]))


def measure_method(a, b):
     fft_abs_1 = np.abs(a[1]) - np.abs(b[1])
     fft_abs_2 = np.abs(a[2]) - np.abs(b[2])

     a_deg = np.rad2deg(np.angle(a[1]))
     b_deg = np.rad2deg(np.angle(b[1]))
     deg_abs_1 = np.abs(a_deg - b_deg)

     a_deg = np.rad2deg(np.angle(a[2]))
     b_deg = np.rad2deg(np.angle(b[2]))
     deg_abs_2 = np.abs(a_deg - b_deg)


     return np.abs(fft_abs_1 - deg_abs_1) + np.abs(fft_abs_2 + deg_abs_2)

print('特征方法：')
print('a和b', measure_method(a1, b1))
print('a和c', measure_method(a1, c1))
print('b和c', measure_method(b1, c1))

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

