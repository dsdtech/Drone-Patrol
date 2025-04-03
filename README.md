# Drone Auto-Sweep/Patrol Script

This Python script uses the DroneKit library to automate a drone's patrol or surveillance flight. It connects to the drone, arms it, switches to AUTO mode to execute a pre-programmed mission, and then closes the connection.

## Purpose

This script is designed to automate drone flights for surveillance, patrols, or other missions that require following a pre-defined path. It simplifies the process of arming the drone, switching to AUTO mode, and ensuring a safe connection closure.

## Prerequisites

* **DroneKit:** You must have the DroneKit library installed. Install it using pip:
    ```bash
    pip install dronekit
    ```
* **Drone Setup:** Your drone must be properly configured and connected to your computer via a telemetry radio or other compatible connection method.
* **Pre-programmed Mission:** The drone should have a pre-programmed mission (waypoints) uploaded that it can execute in AUTO mode.
* **Serial Connection:** The script assumes a serial connection over `/dev/ttyUSB0` at 57600 baud. You may need to adjust this depending on your setup.

## How to Use

1.  **Install Prerequisites:** Ensure you have DroneKit installed and your drone is configured.

2.  **Save the Script:** Save the provided Python script as a `.py` file (e.g., `drone_patrol.py`).

3.  **Modify the Connection (if needed):**
    * If your drone connects via a different serial port or baud rate, modify the `connect()` function in the `auto_sweep_drone()` function. For example:
        ```python
        vehicle_drone = connect('/dev/ttyS0', baud=115200, wait_ready=False)
        ```
        Or to connect via a TCP connection:
        ```python
        vehicle_drone = connect('tcp:127.0.0.1:5760', wait_ready=False)
        ```

4.  **Run the Script:**
    * Open a terminal or command prompt.
    * Navigate to the directory where you saved the script.
    * Execute the script:
        ```bash
        python drone_patrol.py
        ```

## Script Explanation

```python
from dronekit import connect, VehicleMode
import time

def auto_sweep_drone():
    # Connect to the drone
    vehicle_drone = connect('/dev/ttyUSB0', baud=57600, wait_ready=False)

    # Pre-arm checks
    print("Basic pre-arm checks")
    while not vehicle_drone.is_armable:
        print(" Waiting for vehicle to initialize...")
        time.sleep(1)

    # Arm the drone
    vehicle_drone.mode = VehicleMode("LOITER")
    vehicle_drone.armed = True
    while not vehicle_drone.armed:
        print(" Waiting for arming...")
        time.sleep(1)

    # Switch to AUTO mode and execute the mission
    print("Arming motors")
    vehicle_drone.mode = VehicleMode("AUTO")

    # Monitor the mission
    while vehicle_drone.armed:
        time.sleep(1)
        print("Surveillance in process")

    print("Surveillance finished")

    # Close the connection
    vehicle_drone.close()
    print("Vehicle connection closed.")

# Main execution
try:
    print("Changing mode to Auto(Patrolling).")
    auto_sweep_drone()

except Exception as e:
    print(f"Error: {e}")

finally:
    try:
        vehicle_drone.close()
        print("Vehicle connection closed.")
    except NameError:
        print("vehicle_drone was never defined, or already closed.")

connect(): Establishes a connection to the drone.
is_armable: Checks if the drone is ready to be armed.
VehicleMode("LOITER"): Sets the drone to LOITER mode for arming.
armed = True: Arms the drone's motors.
VehicleMode("AUTO"): Sets the drone to AUTO mode for mission execution.
try...except...finally: Handles potential errors and ensures the connection is closed.

**Notes:**
Ensure your drone's safety features are properly configured.
Always perform test flights in a safe and open area.
Adjust the connection parameters and mission as needed for your specific drone and mission.
Dronekit code is designed for use with drones running Ardupilot or PX4 flight controller software.
