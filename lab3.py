


import random
import time


file = open("sensor_data.csv", "w")
file.write("Time(s), Temp(C), Humidity(%)\n")

print("Starting data log... please wait.")


for i in range(1, 11):
    timestamp = i * 0.5
    temp = random.uniform(20.0, 30.0)
    
    humidity = random.uniform(40.0, 60.0)
    
    
    file.write(f"{timestamp}, {temp:.2f}, {humidity:.2f}\n")
    
    print(f"Logged reading {i}: Temp={temp:.2f}C, Humidity={humidity:.2f}%")
    time.sleep(0.5) 

file.close()
print("All data saved to sensor_data.csv!")