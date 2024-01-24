import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad

def integrand(theta, r, R, lam):
    nu = 2 * lam * R * (r - R * np.cos(theta))
    denom = (R**2 + r**2 - 2 * R * r * np.cos(theta))**1.5
    return nu / denom

def electric_field(r, R, lam):
    integral, _ = quad(integrand, 0, np.pi, args=(r, R, lam))
    return integral / (4 * np.pi * 8.854e-12)

#dec variables
R = 1.0  
lam = 1.0  

# Eval E
r_values = np.linspace(0, 5, 1000)
electric_field_values = [electric_field(r, R, lam) for r in r_values]

plt.plot(r_values, electric_field_values)
plt.axvline(x=R, color='r', linestyle='--')
plt.xlabel('r')
plt.ylabel('E')
plt.title('Electric Field as a Function of r'+ "\n" + "R = "+ str(R)+"lam = "+str(lam) + "\n")
plt.grid(True)
plt.show()
