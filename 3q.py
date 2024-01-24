import numpy as np
import matplotlib.pyplot as plt

k = 9e9  
# Def pos and q of charges
positions = np.array([[-0.5, 0], [0.5, 0], [0, np.sqrt(3)/2]])
charges = np.array([1, 1, 1])
# make grid
x = np.linspace(-1, 1, 10000)
y = np.linspace(-1, 1, 10000)
X, Y = np.meshgrid(x, y)
# Calc E on each point in grid
Ex = np.zeros_like(X)
Ey = np.zeros_like(Y)
for i in range(len(charges)):
    r = np.sqrt((X - positions[i, 0])**2 + (Y - positions[i, 1])**2)
    Ex += k*charges[i] * (X - positions[i, 0]) / r**3 # Ex = kq/r^2sin(theta)= kq(x-x0)/r^3
    Ey += k*charges[i] * (Y - positions[i, 1]) / r**3 # Ey = kq/r^2cos(theta)= kq(y-y0)/r^3
# Calc net E
E= np.sqrt(Ex**2 + Ey**2)
#log scale or power scale ? eh
E_lognorm = np.log(E)
# E_pnorm = E**2 
# Plot the electric field norm
plt.contourf(X, Y, E_lognorm, cmap='hsv')

# Plot the electric field streamlines
plt.streamplot(X, Y, Ex, Ey, color='k', linewidth=1, density=2)

plt.colorbar(label='Log of Electric Field Norm (log(V/m))')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Electric Field Norm with Streamlines')
plt.show()