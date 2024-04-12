import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt

# Define the system of differential equations
def eq_system(t, y):
    x, y = y
    dxdt = y + x**2*y
    dydt = -x + 2*x*y
    return [dxdt, dydt]

# Define parameters
#alpha = 0.1
#beta = 0.02
#gamma = 0.3
#delta = 0.01

# Define initial conditions
x0 = 0.5  
y0 = 1 
initial_conditions = [x0, y0]

# Define time span
t_span = (0, 0.6)
t_eval = np.linspace(0, 0.6, 1000)

# Solve the differential equations
sol = solve_ivp(eq_system, t_span, initial_conditions, t_eval=t_eval)

# Plot the solution
plt.plot(sol.t, sol.y[0], label='x')
plt.plot(sol.t, sol.y[1], label='y')
plt.xlabel('Time')
plt.ylabel('X or Y')
plt.title('System of Equations')
plt.legend()
plt.grid(True)
plt.savefig('x_y_plot.png')
plt.close()  #Close the plot to prevent displaying it interactively
