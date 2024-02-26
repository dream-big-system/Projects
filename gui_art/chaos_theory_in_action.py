import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from scipy.integrate import odeint  # Import odeint from scipy.integrate

# Constants
G = 9.8  # Acceleration due to gravity (m/s^2)
L1 = 1.0  # Length of pendulum 1 (m)
L2 = 1.0  # Length of pendulum 2 (m)
M1 = 1.0  # Mass of pendulum 1 (kg)
M2 = 1.0  # Mass of pendulum 2 (kg)

# Function to calculate the derivatives of theta1, theta2, omega1, and omega2
def derivs(state, t):
    dydx = np.zeros_like(state)
    dydx[0] = state[1]

    delta = state[2] - state[0]
    den1 = (M1 + M2) * L1 - M2 * L1 * np.cos(delta) * np.cos(delta)
    dydx[1] = ((M2 * L2 * state[3] * state[3] * np.sin(delta) * np.cos(delta)
                + M2 * G * np.sin(state[2]) * np.cos(delta)
                + M2 * L1 * state[1] * state[1] * np.sin(delta)
                - (M1 + M2) * G * np.sin(state[0]))
               / den1)

    dydx[2] = state[3]

    den2 = (L2 / L1) * den1
    dydx[3] = ((- M2 * L2 * state[3] * state[3] * np.sin(delta) * np.cos(delta)
                + (M1 + M2) * G * np.sin(state[0]) * np.cos(delta)
                - (M1 + M2) * L1 * state[1] * state[1] * np.sin(delta)
                - (M1 + M2) * G * np.sin(state[2]))
               / den2)

    return dydx

# Create a time array from 0..100 sampled at 0.05 second steps
dt = 0.05
t = np.arange(0, 100, dt)

# Initial conditions: theta1, dtheta1/dt, theta2, dtheta2/dt
theta1 = np.pi / 2
omega1 = 0
theta2 = np.pi / 2
omega2 = 0

# State vector
state = np.array([theta1, omega1, theta2, omega2])

# Integration using scipy's odeint
y = odeint(derivs, state, t)  # Use odeint from scipy.integrate

# Set up the figure and axis
fig = plt.figure()
ax = fig.add_subplot(111, autoscale_on=False, xlim=(-2, 2), ylim=(-2, 2))
ax.set_aspect('equal')
ax.grid()

line, = ax.plot([], [], 'o-', lw=2)
time_template = 'time = %.1fs'
time_text = ax.text(0.05, 0.9, '', transform=ax.transAxes)

# Initialize animation
def init():
    line.set_data([], [])
    time_text.set_text('')
    return line, time_text

# Update animation
def animate(i):
    thisx = [0, L1 * np.sin(y[i, 0]), L2 * np.sin(y[i, 2])]
    thisy = [0, -L1 * np.cos(y[i, 0]), -L2 * np.cos(y[i, 2])]

    line.set_data(thisx, thisy)
    time_text.set_text(time_template % (i*dt))
    return line, time_text

ani = animation.FuncAnimation(fig, animate, range(1, len(y)),
                              interval=dt * 1000, blit=True, init_func=init)

plt.show()
