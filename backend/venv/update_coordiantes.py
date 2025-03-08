import time
import random

# Starting coordinates (example: Bangalore)
latitude = 12.9716  
longitude = 77.5946  

# File where coordinates are stored
file_path = "coordinates.txt"

while True:
    # Simulate small movement
    latitude += random.uniform(-0.0005, 0.0005)
    longitude += random.uniform(-0.0005, 0.0005)

    # Write the new coordinates to the file
    with open(file_path, "w") as file:
        file.write(f"{latitude},{longitude}")

    print(f"Updated coordinates: {latitude}, {longitude}")

    time.sleep(1)  # Update every 1 second
