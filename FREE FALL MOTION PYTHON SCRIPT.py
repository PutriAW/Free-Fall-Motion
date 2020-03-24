#free fall motion 
#by Putri Apriyanti Windya (1301174169)
# Mar Ayu Fotina (1301174013)
# Hema Ditania (1301174219)

import numpy as np
import matplotlib.pyplot as plt

#Initialization
v = 0 #initial velocity
y = 10#initial height
t = 0 #initial time
dt = 0.01 #time differences
g =  -9.8 #accelaration
yy = 10
t_list =[t] # list of time
t_list_an = [t]
v_list =[v] # list of velocity
y_list =[y] # list of height
v_list_analytical = [v] # velocity list of analitycal solution
y_list_analytical = [y] # height list of analytical solution

#process
while y >= 0 :
    v += g * dt
    y += v * dt
    t += dt
    va = g * t
    ya = yy + 0.5 * g * t ** 2
    t_an = np.sqrt((2 * ya - yy / g))
    if (y < 0):
        break
    t_list.append(t)
    t_list_an.append(t_an)
    v_list.append(v)
    y_list.append(y)
    v_list_analytical.append(va)
    y_list_analytical.append(ya)
t_an = np.sqrt((2*yy)/-g)
print(t_an)

#comparation between Analytical and Numerical
# t_analytical = np.sqrt((2 * y_list_analytical[-1]) - yy / g)
print("High of Numerical vs Analytical" )
print(y_list[-1], " VS " ,y_list_analytical[-1]) 
print()

print("Time of Numerical vs Analytical" )
# print(t_list[-1])
# print(t_list[-1], " VS " ,t_analytical) 
print(t_list[-1], " VS " ,t_an) 
# print(t_analytical)
print(t_list_an)
# print(y_list_analytical)
print()
# print(t_list[-1] - t_list_an[-1])
print((t_list_an[-1]/t_list[-1])*100)

#plot diagram
plt.plot(t_list,y_list, color="red", label="Numerical")
plt.plot(t_list, y_list_analytical, color="blue", label="Analytical")
plt.xlabel('waktu')
plt.ylabel('ketinggian')
plt.legend()
plt.show()




