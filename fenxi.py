# -*- coding:UTF-8 -*-
import tushare as ts
import matplotlib.pyplot as plt
import numpy as np
stock = ts.get_h_data('399106', index=True)
#stock = ts.get_hist_data('399106')
stock.shape
#print stock.head()
'''
plt.plot(stock.index, stock.close, color='b', label='399106')
plt.xlabel('Date')
plt.ylabel('close price')
plt.title('Stock plot')
plt.legend()
plt.show()
'''
'''
fig = plt.figure()
ax1 = plt.subplot2grid((1, 1), (0, 0))
ax1.plot(stock.index, stock.close, label='399106')
for label in ax1.xaxis.get_ticklabels():
    label.set_rotation(45)    #转动x轴坐标45度
ax1.grid(True)
plt.xlabel('Date')
plt.ylabel('Close Price')
plt.title('Subplot')
plt.legend()
plt.show()
'''
'''
fig = plt.figure()
ax1 = plt.subplot2grid((1, 1), (0, 0))
ax1.fill_between(stock.index, 1850, stock.close, color='b')
ax1.plot(stock.index, stock.close, linewidth=1., color='k', label='399106')
ax1.grid(True, linestyle='--')
for label in ax1.xaxis.get_ticklabels():
    label.set_rotation(45)    #转动x轴坐标45度

ax1.set_yticks(np.arange(1850, 2200, 50))
ax1.xaxis.label.set_color('c')
ax1.yaxis.label.set_color('r')
plt.xlabel('Date')
plt.ylabel('Close Price')
plt.title('Subplot')
plt.legend()
plt.subplots_adjust(left=0.09, bottom=0.20, right=0.94, top=0.90, wspace=0.2, hspace=0)
plt.show()
'''

fig = plt.figure()
ax1 = plt.subplot2grid((1, 1), (0, 0))
date = stock.index
closeq = stock.close
mean_closeq = stock.close.mean()

ax1.fill_between(date, closeq, mean_closeq, where=(closeq >= mean_closeq), facecolor='g', alpha=.6)
ax1.fill_between(date, closeq, mean_closeq, where=(closeq < mean_closeq), facecolor='r', alpha=.6)

ax1.plot(stock.index, stock.close, linewidth=1., color='b', label='close price')
ax1.plot([], [], linewidth=5, label='low', color='r', alpha=0.5)
ax1.plot([], [], linewidth=5, label='high', color='g', alpha=0.5)

ax1.grid(True, linestyle='--')
for label in ax1.xaxis.get_ticklabels():
    label.set_rotation(45)

ax1.xaxis.label.set_color('c')
ax1.yaxis.label.set_color('r')
plt.xlabel('Date')
plt.ylabel('Close Price')
plt.title('Fillplot')
plt.legend()

plt.show()


