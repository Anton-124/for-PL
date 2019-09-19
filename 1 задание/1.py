import numpy as np
a = open('1.txt')
read = a.read().split() 
values = [int(i) for i in read]
print('%.2f'%np.percentile(values, 90), '90 персентиль')
print('%.2f'%np.median(values), 'median')
print('%.2f'%np.mean(values), 'average')
print('%.2f'%np.max(values), 'max')
print('%.2f'%np.min(values), 'min')
input('Press any key to exit')

