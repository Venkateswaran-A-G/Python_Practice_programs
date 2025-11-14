#Flatten a nested list 
import numpy as np
nested = [[1, 2], [3, 4, 5], [6]]
flat = np.array([item for sublist in nested for item in sublist])
print(flat)  
