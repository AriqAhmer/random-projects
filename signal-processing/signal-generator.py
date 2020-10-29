import matplotlib.pyplot as plt
import numpy as np
from math import exp, sin
import random
import csv

#setting random seed for reproduceable results
random.seed(123456789)

#creating x values
t = np.arange(1, 101, 0.1)
#creating y values
y = [exp(0.05*(i + sin(5*i) + random.randint(0,2))) for i in t]

"""
#rounding values for exporting
t_exp = [round(i, 1) for i in t]
y_exp = [round(i, 3) for i in y]

#writing data to csv file
rows = zip(t_exp, y_exp)
with open("signal-data.csv", "w", newline='') as f:
    write = csv.writer(f)
    write.writerow(['time-t', 'signal-y'])
    write.writerows(rows)
"""

#after normal exponential regression
A = 1.057826806
B = 0.0502770095
y2 = [A*exp(B*i) for i in t]

#plotting the data to the graph
plt.xlabel('Time - t')
plt.ylabel('Input signal - y')
plt.title('Generated signal')

plt.ylim(0, 100)
plt.xlim(0, 100)

plt.plot(t, y, label='actual signal')
plt.plot(t, y2, label='regression line')

plt.legend()

plt.show()