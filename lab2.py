



import numpy as np
import matplotlib.pyplot as plt


R = 1000       # 1k Ohm resistor
C = 0.000001   # 1uF Capacitor
V_initial = 5  # Starting at 5 volts
tau = R * C    # Time constant


time = np.linspace(0, 0.01, 500)



voltage = V_initial * np.exp(-time / tau)


plt.plot(time, voltage, color='red', label='Discharging')
plt.title("Capacitor Voltage vs Time (Discharging)")
plt.xlabel("Time in Seconds")
plt.ylabel("Voltage (V)")
plt.grid(True)
plt.legend()
plt.show()

