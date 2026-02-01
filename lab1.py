# Lab 1 - Ohm's Law Calculator


print("--- Ohm's Law Calculator ---")


volts = float(input("Enter the voltage: "))
ohms = float(input("Enter the resistance: "))


if ohms == 0:
    print("Wait, resistance can't be zero. Try again.")
else:
    
    amps = volts / ohms
    
    watts = volts * amps
    
    print("Current is:", amps, "A")
    print("Power is:", watts, "W")

print("Done.")