import numpy as np
import matplotlib.pyplot as plt

R_val = 1000
C_val = 0.000001
V_0 = 5
tau_const = R_val * C_val

t_axis = np.linspace(0, 0.01, 500)
v_decay = V_0 * np.exp(-t_axis / tau_const)

plt.plot(t_axis, v_decay, color='blue', linestyle='--', label='Discharging')
plt.title("Capacitor Voltage Decay")
plt.xlabel("Time (s)")
plt.ylabel("Voltage (V)")
plt.grid(True)
plt.legend()
plt.show()

