import numpy as np

# Problem 1
a1 = np.array([1, 2, 3])
b1 = np.array([4, 5, 6])
print(f"P1. Sum: {a1+b1} \nDifference:{a1-b1}\n")

# Problem 2
a2 = np.array([[1, 2], [3, 4]])
b2 = np.array([[5, 6], [7, 8]])
print(f"P2. Sum: {a2+b2}\nDifference:{a2-b2}\n")

# Problem 3
a3 = a1
b3 = b1
print(f"P3. Dot product: {np.dot(a3,b3)}")

# Problem 4
a4 = np.array([[1, 2, 3], [4, 5, 6]])
b4 = np.array([[7, 8, 9, 10], [11, 12, 13, 14], [15, 16, 17, 18]])
print(f"P4. Product: {np.dot(a4,b4)}")

# Problem 5
a5 = np.array([1, 1, 2])
print(f"P5. Product: {np.linalg.norm(a5)}")

# Problem 6
a6 = np.array([[1, 2], [3, 4]])
print(f"P6. Transposed Matrix: {a6.T}")
