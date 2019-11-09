# VEX V5 Python Project with Competition Template
import sys
import vex
from vex import *

#region config
brain        = vex.Brain()
leftmotor    = vex.Motor(vex.Ports.PORT11, vex.GearSetting.RATIO18_1, False)
left_intake  = vex.Motor(vex.Ports.PORT14, vex.GearSetting.RATIO18_1, False)
left_lift    = vex.Motor(vex.Ports.PORT15, vex.GearSetting.RATIO18_1, False)
rightmotor   = vex.Motor(vex.Ports.PORT17, vex.GearSetting.RATIO18_1, True)
right_lift   = vex.Motor(vex.Ports.PORT18, vex.GearSetting.RATIO18_1, True)
tray         = vex.Motor(vex.Ports.PORT19, vex.GearSetting.RATIO18_1, False)
right_intake = vex.Motor(vex.Ports.PORT20, vex.GearSetting.RATIO18_1, True)
dt           = vex.Drivetrain(leftmotor, rightmotor, 101.6, 28.9, vex.DistanceUnits.MM)
con          = vex.Controller(vex.ControllerType.PRIMARY)
#endregion config


# Creates a competition object that allows access to Competition methods.
competition = vex.Competition()

def pre_auton():
    # All activities that occur before competition start
    # Example: setting initial positions
    leftmotor.set_stopping(vex.BrakeType.COAST)
    rightmotor.set_stopping(vex.BrakeType.COAST)
    dt.set_velocity(100,vex.VelocityUnits.PCT)
    pass

def autonomous():
    # Place autonomous code here
    tray.rotate_for(vex.DirectionType.REV,5,vex.RotationUnits.REV,50,vex.VelocityUnits.PCT)
    tray.rotate_for(vex.DirectionType.FWD,5,vex.RotationUnits.REV,50,vex.VelocityUnits.PCT,False)
    dt.drive_for(vex.DirectionType.FWD,6,vex.DistanceUnits.IN)
    dt.turn_for(vex.TurnType.LEFT,90,vex.RotationUnits.DEG)
    dt.drive_for(vex.DirectionType.FWD,6,vex.DistanceUnits.IN)
    pass

def drivercontrol():
    # Place drive control code here, inside the loop
    while True:
        # This is the main loop for the driver control.
        # Each time through the loop you should update motor
        # movements based on input from the controller.
        leftmotor.spin(vex.DirectionType.FWD,(con.axis3.value()),vex.VelocityUnits.PCT)
        rightmotor.spin(vex.DirectionType.FWD,(con.axis2.value()),vex.VelocityUnits.PCT)
        if con.buttonR1.pressing():
            right_intake.spin(vex.DirectionType.FWD,100,vex.VelocityUnits.PCT)
            left_intake.spin(vex.DirectionType.FWD,100,vex.VelocityUnits.PCT)
        elif con.buttonR2.pressing():
            right_intake.spin(vex.DirectionType.FWD,-100,vex.VelocityUnits.PCT)
            left_intake.spin(vex.DirectionType.FWD,-100,vex.VelocityUnits.PCT)
        else :
            right_intake.stop(vex.BrakeType.BRAKE)
            left_intake.stop(vex.BrakeType.BRAKE)
        if con.buttonL1.pressing():
            left_lift.spin(vex.DirectionType.FWD,100,vex.VelocityUnits.PCT)
            right_lift.spin(vex.DirectionType.FWD,100,vex.VelocityUnits.PCT)
        elif con.buttonL2.pressing():
            left_lift.spin(vex.DirectionType.FWD,-100,vex.VelocityUnits.PCT)
            right_lift.spin(vex.DirectionType.FWD,-100,vex.VelocityUnits.PCT)
        else:
            left_lift.stop(vex.BrakeType.BRAKE)
            right_lift.stop(vex.BrakeType.BRAKE)
        if con.buttonA.pressing():
            tray.spin(vex.DirectionType.FWD,100,vex.VelocityUnits.PCT)
        elif con.buttonB.pressing():
            tray.spin(vex.DirectionType.FWD,-100,vex.VelocityUnits.PCT)
        else :
            tray.stop(vex.BrakeType.BRAKE)    
        pass
        

# Do not adjust the lines below

# Set up (but don't start) callbacks for autonomous and driver control periods.
competition.autonomous(autonomous)
competition.drivercontrol(drivercontrol)

# Run the pre-autonomous function.
pre_auton()

# Robot Mesh Studio runtime continues to run until all threads and
# competition callbacks are finished.



  
    
    
    
    



