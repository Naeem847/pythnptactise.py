# Road Safety Traffic Light Simulation

import time  # To add delays between light changes

# List of traffic lights in order
traffic_lights = ["red", "yellow", "green"]

# Loop to simulate traffic lights changing continuously
while True:
    for light in traffic_lights:
        if light == "red":
            print("Red light - You must stop 🚦")
        elif light == "yellow":        
            print("Yellow light - Prepare to stop ⚠️")
        else:  # green
            print("Green light - You can go 🟢")
            
        time.sleep(3)  # Wait for 3 seconds before changing light