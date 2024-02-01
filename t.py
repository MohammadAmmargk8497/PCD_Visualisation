import numpy as np

# Create a 1D array
array1d = np.array([1, 2, 3, 4, 5])

# Use np.vstack to reshape it into a 2D array with a single column
array2d = np.vstack(array1d)

print("Original 1D array:")
print(array1d)

print("\nReshaped 2D array:")
print(array2d)