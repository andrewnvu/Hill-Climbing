import random
import numpy as np

x = 10
y = 10

#creates a matrix nxn initialized to 0
#terrain = np.zeros([x,y], dtype = int, order = 'C')


#creates a matrix m x n initialized with random ints from 0 to 100
terrain = np.random.randint(0,100,size = (x,y))

#grabs max value op the array, when axis is 1 you go horizontally, 0 is verticall
#globalOptima = np.amax(terrain, axis=1)
globalOptima = np.amax(terrain)

#will get me the index or specific location of the value i want
globalIndex = np.unravel_index(terrain.argmax(),terrain.shape)

print(terrain)
print(globalOptima)
print(globalIndex)
