print("--- MY OHMS LAW APP ---")

v_input = float(input("Enter the voltage (V): "))
r_input = float(input("Enter the resistance (R): "))

if r_input == 0:
    print("Error: Resistance cannot be zero.")
else:
    current = v_input / r_input
    power_val = v_input * current
    
    print("Current is:", current, "A")
    print("Power is:", power_val, "W")

print("Calculation Finished.")