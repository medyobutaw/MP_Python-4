import numpy as np
import matplotlib.pyplot as plt
import math as math

h = float(input('Initial Height above the ground: '))
v = float(input('Magnitude of the Velocity: '))
a = float(input('Angle in degrees with respect to the x-axis: '))
x = float(input('x-component acceleration: '))
y = float(input('y-component acceleration (free fall = -9.8):' ))

if y >= 0:
    raise ValueError('The acceleration of the y-component must not be greater than or equal to zero.')
elif h < 0:
    raise ValueError('The Height must not be less than 0.')
 
def python4(h,v,a,x,y):
    A = math.radians(a)
    xval = math.cos(A)
    yval = math.sin(A)

    tmax = (math.sqrt(((v*yval)**2) - 2*y*h) - v*xval)/y

    if tmax <= 0:
    
        tmax = (-math.sqrt(((v*yval)**2) - 2*y*h) - v*xval)/y
    
    t = np.arange(0,tmax,0.01)

    X = (v*(xval)*t)+(1/2)*x*(t**2)
    Y = (h+ v*(yval)*t)+(1/2)*y*(t**2)

    plt.plot(X,Y)
    plt.grid()
    plt.xlabel('Distance')
    plt.ylabel('Height')
    plt.title('Projectile Trajectory')
    plt.show()
    
python4(h,v,a,x,y)