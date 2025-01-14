import numpy as np
import ctypes
import matplotlib.pyplot as plt

# lib stores the shared object file of the c code
lib = ctypes.CDLL('./6.5.14.so')

#the function 'gradientascent' is accessed via lib.gradientascent
#the restype(type of output) by the function gradientascent.
lib.gradientascent.restype = ctypes.POINTER(ctypes.c_double)


result = lib.gradientascent() # storing the pointer returned by the function 'gradientascent' in result

#initializing  lists to store x coordinates and y coordinates of the generated points respectively.
xcoords = np.linspace(13,17,400)
ycoords = xcoords*((60-xcoords)**3)
#storing x ang y coords of maxima.       
xmax = result[0]
ymax = result[1]

print("x value at maxima = ",xmax)
print("y value at maxima = ",ymax)

#plotting theoretical curve
plt.plot(xcoords, ycoords,color='r',linewidth =2,label="functional curve")
#plot the maxima
plt.scatter(xmax,ymax,color='k',label='maxima')


#labelling the two perpendicular axes
plt.xlim(13,17)
plt.ylim(1349699,1367500)
plt.xlabel('X')
plt.ylabel('Y')
plt.legend()
# To get a grid
plt.grid(True)
plt.show()




