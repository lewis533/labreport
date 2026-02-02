import random
import time

output_file = open("my_lab_results.csv", "w")
output_file.write("Time(s), Temp(C), Humidity(%)\n")

print("Starting data log... please wait.")

for count in range(1, 11):
    sec = count * 0.5
    t_reading = random.uniform(21.0, 29.0)
    h_reading = random.uniform(45.0, 55.0)
    
    output_file.write(f"{sec}, {t_reading:.2f}, {h_reading:.2f}\n")
    
    print(f"Reading {count} saved: Temp={t_reading:.2f}C, Humidity={h_reading:.2f}%")
    time.sleep(0.5)

output_file.close()
print("Success: Data saved to my_lab_results.csv")