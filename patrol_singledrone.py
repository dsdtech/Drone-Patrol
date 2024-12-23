from dronekit import connect, VehicleMode
import time

def auto_sweep_drone():

    vehicle_drone = connect('/dev/ttyUSB0', baud=57600, wait_ready=False)
    print("Basic pre-arm checks")
    while not vehicle_drone.is_armable:
        print(" Waiting for vehicle to initialize...")
        time.sleep(1)

    vehicle_drone.mode = VehicleMode("LOITER")
    vehicle_drone.armed = True
    while not vehicle_drone.armed:
        print(" Waiting for arming...")
        time.sleep(1)

    print("Arming motors")
    vehicle_drone.mode = VehicleMode("AUTO")

    while vehicle_drone.armed != False:
        time.sleep(1)
        print("Survillence in process")

    print("Survillence finished")

    vehicle_drone.close()
    print("Vehicle connection closed.")    

#------------Main-----------------------

# Connect to the vehicle
#print("Connecting to vehicle...")
#vehicle = connect('/dev/ttyUSB0', baud=57600, wait_ready=False)

try:
    print("Changing mode to Auto(Patrolling).")
    auto_sweep_drone()

except Exception as e:
    print(f"Error: {e}")

finally:
    vehicle.close()
    print("Vehicle connection closed.")