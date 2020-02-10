import numpy as np 

def my_fun(mat1,mat2):
    try:
        return mat1 * mat2
    except ValueError:
        print("Matrixs not here")
        return None

my_martix = np.identity(4)
my_2_martix = np.identity(4)

print(my_fun(my_martix,my_2_martix))