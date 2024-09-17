import numpy as np

a = np.array([1.14480774, 0.74504852, 0.36892075, 0.56873322])
print(a)
x, y, z, w = a
if x > w:
	print(f"{x}, {y}, {z}")
