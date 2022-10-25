import json 
#to create the graph
import matplotlib.pyplot as plt
import numpy as np


x= open('dataset1.json')
dataset1=json.load(x)

year=[]
temp=[]

data=dataset1['data']
for key in data:
    year.append(int(key))
    temp.append(float(data[key]))

plt.plot(year,temp)
plt.xlabel('Year')
plt.yticks(np.arange(0, 1, step=0.2))
plt.xticks(np.arange(1880,2016 , step=20))
plt.ylabel('Temperature (Celcius)')
plt.title('Temperature versus Year')


plt.show()


#linegraph