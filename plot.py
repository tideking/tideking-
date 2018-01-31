# coding = utf-8
import matplotlib.pyplot as plt
import numpy as np
'''

x = [1, 2, 3]
y1 = [5, 7, 4]
y2 = [10, 14, 12]

plt.plot(x, y1, label='Line1')
plt.plot(x, y2, label='Line2')
plt.xlabel('X axis')
plt.ylabel('Y axis')
plt.title('Line')
plt.legend()
plt.show()
'''
'''

x1 = [1, 3, 5, 7, 9]
x2 = [2, 4, 6, 8, 10]
y1 = [3, 5, 7, 8, 10]
y2 = [4, 6, 9, 10, 15]

plt.bar(x1, y1, label='simple1', color='b')
plt.bar(x2, y2, label='simple2', color='r')

plt.xlabel('bar number')
plt.ylabel('bar count')
plt.title('Bar Plot')

plt.legend()
plt.show()
'''
'''

po = [22, 55, 62, 45, 21, 22, 34, 42, 42, 4, 99, 102, 110, 120, 121, 122, 130, 111,
                   115, 112, 80, 75, 65, 54, 44, 43, 42, 48]
bins = list(range(0, 140, 10))
plt.hist(po, bins=bins, histtype='bar', color='b', rwidth=.8)

plt.xlabel('x')
plt.ylabel('y')
plt.title('Histogram Plot')

plt.show()
'''
'''
plt.scatter(np.arange(10), np.random.randn(10), color='r')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Scatter Plot')

plt.show()
'''

slice = [7, 2, 2, 13]
act = ['sleeping', 'eating', 'working', 'playing']
colors = 'cmrb'

plt.pie(slice, labels=act, colors=colors, startangle=90, explode=(0, .1, 0, 0), shadow=True, autopct='%1.1f%%')
plt.title('Pie Plot')
plt.show()

