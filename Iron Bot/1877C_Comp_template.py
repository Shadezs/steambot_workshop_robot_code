# VEX V5 Python Project with Competition Template
import sys
import vex
from vex import *

#region config
brain      = vex.Brain()
lroller    = vex.Motor(vex.Ports.PORT1, vex.GearSetting.RATIO18_1, False)
lfront     = vex.Motor(vex.Ports.PORT3, vex.GearSetting.RATIO18_1, False)
mag        = vex.Motor(vex.Ports.PORT4, vex.GearSetting.RATIO18_1, False)
lback      = vex.Motor(vex.Ports.PORT5, vex.GearSetting.RATIO18_1, False)
rback      = vex.Motor(vex.Ports.PORT6, vex.GearSetting.RATIO18_1, False)
rfront     = vex.Motor(vex.Ports.PORT7, vex.GearSetting.RATIO18_1, False)
rollerlift = vex.Motor(vex.Ports.PORT9, vex.GearSetting.RATIO18_1, False)
rroller    = vex.Motor(vex.Ports.PORT10, vex.GearSetting.RATIO18_1, False)
con        = vex.Controller(vex.ControllerType.PRIMARY)
#endregion config


# Creates a competition object that allows access to Competition methods.
competition = vex.Competition()

def pre_auton():
    # All activities that occur before competition start
    # Example: setting initial positions
    pass

def autonomous():
   #Blue
   Forward
   Right
   Back
   Forward
   Intake and forward
   Back
   Left
   Forward
   Score
  #Red
   Forward
   Left
   Back
   Forward
   Intake and forward
   Back
   Right
   Forward
   Score
   
   
 # Place autonomous code here
    pass

def drivercontrol():
    # Place drive control code here, inside the loop
    while True:
        lfront.spin(vex.DirectionType.FWD,(con.axis3.value()),vex.VelocityUnits.PCT)
        rfront.spin(vex.DirectionType.FWD, (con.axis2.value()), vex.VelocityUnits.PCT)
        lback.spin(vex.DirectionType.FWD, (con.axis3.value()), vex.VelocityUnits.PCT)
        rback.spin(vex.DirectionType.FWD, (con.axis2.value()), vex.VelocityUnits.PCT)
# 
        if con.buttonR1.pressing():
            rroller.spin(vex.DirectionType.FWD, 100, vex.VelocityUnits.PCT)
            lroller.spin(vex.DirectionType.FWD, 100, vex.VelocityUnits.PCT)
        elif con.buttonR2.pressing():
            rroller.spin(vex.DirectionType.FWD, -100, vex.VelocityUnits.PCT)
            lroller.spin(vex.DirectionType.FWD, -100, vex.VelocityUnits.PCT)
        else:
            rroller.stop(vex.BrakeType.BRAKE)
            lroller.stop(vex.BrakeType.BRAKE)
        if con.buttonL1.pressing():
            rollerlift.spin(vex.DirectionType.FWD, 100, vex.VelocityUnits.PCT)
        elif con.buttonL2.pressing():
            rollerlift.spin(vex.DirectionType.FWD, -100, vex.VelocityUnits.PCT)
        else:
            rollerlift.stop(vex.BrakeType.HOLD)
        if con.buttonX.pressing():
            mag.spin(vex.DirectionType.FWD, 100, vex.VelocityUnits.PCT)
        elif con.buttonB.pressing():
            mag.spin(vex.DirectionType.FWD, -100, vex.VelocityUnits.PCT)
        else:
            mag.stop(vex.BrakeType.BRAKE)

        pass

# Do not adjust the lines below

# Set up (but don't start) callbacks for autonomous and driver control periods.
competition.autonomous(autonomous)
competition.drivercontrol(drivercontrol)

# Run the pre-autonomous function.
pre_auton()

# Robot Mesh Studio runtime continues to run until all threads and
# competition callbacks are finished.



  
    
    
    
    


