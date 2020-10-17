import matplotlib.pyplot as mat
import numpy as num

x= num.arange(-360,360,180)
y= num.sin(x)
z=num.cos(x)


mat.plot(x,y,x,z)
mat.xlabel("x value from -360 to 360")
mat.ylabel("sin(x) and cos(x)")
mat.title("sin Vs cosine curves")
mat.legend(['sin(x)','cos(x)'])
mat.show()