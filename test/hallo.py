#!/usr/bin/python
# -*- coding: utf-8 -*-

# Import DroneKit-Python
from dronekit import connect, VehicleMode

# Connect to the Vehicle.
print("Connecting")
vehicle = connect('/dev/ttyS0', wait_ready=True,baud=57600)

# Get some vehicle attributes (state)
print "Get some vehicle attribute values:"
print " GPS: %s" % vehicle.gps_0
print " Battery: %s" % vehicle.battery
print " Last Heartbeat: %s" % vehicle.last_heartbeat
print " Is Armable?: %s" % vehicle.is_armable
print " System status: %s" % vehicle.system_status.state
print " Mode: %s" % vehicle.mode.name    # settable

# Close vehicle object before exiting script
vehicle.close()

# Shut down simulator
print("Completed")
