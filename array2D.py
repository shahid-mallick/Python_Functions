import numpy as np



def array_2D():
    rows= int(input("number of rows : "))
    col= int(input ("number of colomns : "))


    myMatrix = np.arange(1,rows*col+1).reshape(rows,col)

    print(myMatrix)


array_2D()