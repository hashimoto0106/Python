import numpy as np
import csv

dat = np.loadtxt('test.csv', delimiter=',', skiprows=1, dtype=float)

np.savetxt('save.csv', dat, fmt='%.lf,%.8f,%d', header='time,vel,alt', comments='')

with open('out.csv', 'w', newline='', encoding='utf-8') as f:
    f.write('time,vel,height')
    writer = csv.writer(f)
    writer.writerows(dat)
