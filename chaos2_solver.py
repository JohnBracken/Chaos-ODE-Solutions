import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt

# Define the system of differential equations
def rossler(t, y, a, b, c):
    x, y, z = y
    dxdt = -y - z
    dydt = x + a*y
    dzdt = b + z*(x - c)
    return [dxdt, dydt, dzdt]

# Define parameters
a = 0.2
b = 0.2
c = 5.7
args = (a,b,c,)

# Define initial conditions
x0 = 1  
y0 = 1 
z0 = 1
initial_conditions = [x0, y0, z0]

# Define time span
t_span = (0, 500)
t_eval = np.linspace(0, 500, 10000)

# Solve the differential equations
sol = solve_ivp(rossler, t_span, initial_conditions, args=args, t_eval=t_eval)

# Plot the solution
plt.plot(sol.y[0], sol.y[1], label='Rossler plot')
#plt.plot(sol.t, sol.y[1], label='y')
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Rossler System')
plt.legend()
plt.grid(True)
plt.savefig('Rossler_plot.png')
plt.close()  #Close the plot to prevent displaying it interactively
