import numpy as np

def booth_function (x):

    x1 , x2 = x
    return (x1 + 2 * x2 - 7) **2 + (2 * x1 + x2 - 5) **2

# Example usage
x = np.array ([1.0 , 3.0])
result = booth_function (x)
print("Booth function result:", result)