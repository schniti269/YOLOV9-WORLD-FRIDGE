

def lehmer_prng(seed, a=51,m=61):


    return (a * seed) % m

n=61

arr = [1]
for i in range(1, n):
    arr.append(lehmer_prng(arr[i-1]))   

coords=[]
for i in range(0,n-1,1):
    coords.append([arr[i],arr[i+1]])

#plot 2d
import matplotlib.pyplot as plt
import numpy as np

x = [i[0] for i in coords]
y = [i[1] for i in coords]

plt.scatter(x, y)
plt.show()




    
