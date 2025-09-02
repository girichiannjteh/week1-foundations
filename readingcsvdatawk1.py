import numpy as np
import matplotlib.pyplot as plt
import csv

data = np.genfromtxt('testcsvdata.csv',
                     delimiter=',',
                     names= True)

years = data['year']

masses = data['mass']
#csv data is now stored
plt.xlabel('Years')
plt.ylabel('Masse in Kg')
plt.yticks(np.arange(0, max(masses)+1000, 1000),
           [f"{x} kg" for x in np.arange(0, max(masses)+1000, 1000)])
plt.xticks(np.arange(min(years), max(years)+1,2.0))
plt.plot(years,masses, c = 'red', marker = '.', 
         markersize = 5)
for x, y in zip(years, masses):
    plt.text(x, y, str(y), fontsize=8, ha='right', va='bottom')
plt.show()