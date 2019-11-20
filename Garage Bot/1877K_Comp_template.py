# VEX V5 Python Project with Competition Template
import sys
import vex
from vex import *
def forward(x,y,z):
    if z==1:
        lback.rotate_to(x,vex.RotationUnits.REV,y,vex.VelocityUnits.PCT,True)
        lfront.rotate_to(x, vex.RotationUnits.REV,y,vex.VelocityUnits.PCT,True)
        rfront.rotate_to(x,vex.RotationUnits.REV,y, vex.VelocityUnits.PCT,True)
        rback.rotate_to(x,vex.RotationUnits.REV,y, vex.VelocityUnits.PCT,True)
    else:
        lback.rotate_to(x,vex.RotationUnits.REV,y,vex.VelocityUnits.PCT,False)
        lfront.rotate_to(x, vex.RotationUnits.REV,y,vex.VelocityUnits.PCT,False)
        rfront.rotate_to(x,vex.RotationUnits.REV,y, vex.VelocityUnits.PCT,False)
        rback.rotate_to(x,vex.RotationUnits.REV,y, vex.VelocityUnits.PCT,False)
    

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

def autonomous():
  def pre_auton():
    # All activities that occur before competition start
    # Example: setting initial positions
    rroller.set_timeout(1,vex.TimeUnits.SEC)
    mag.set_timeout(1,vex.TimeUnits.SEC)
    pass

def autonomous():
    #Blue  
    mag.rotate_to(1.4, vex.RotationUnits.REV, 100, vex.VelocityUnits.PCT)
    rollerlift.rotate_to(0.7, vex.RotationUnits.REV, 70, vex.VelocityUnits.PCT)#this need to finish before next command
    rollerlift.rotate_to(-0.0, vex.RotationUnits.REV, 70, vex.VelocityUnits.PCT)
    #mag.rotate_to(0.5,vex.RotationUnits.REV,100,vex.VelocityUnits.PCT)
   # mag.rotate_to(-1.4, vex.RotationUnits.REV, 100, vex.VelocityUnits.PCT)
   # rroller.rotate_for_time(vex.DirectionType.REV,3,vex.TimeUnits.SEC,100,vex.VelocityUnits.PCT,False)# not runing until the last commad finish.
    #lroller.rotate_for_time(vex.DirectionType.REV,3,vex.TimeUnits.SEC,100,vex.VelocityUnits.PCT)#same as the last one
    #roll(-10,100)
    rroller.rotate_to(-5,vex.RotationUnits.REV,25,vex.VelocityUnits.PCT,False)
    lroller.rotate_to(-5,vex.RotationUnits.REV,25,vex.VelocityUnits.PCT,False)
    rollerlift.rotate_to(0.9,vex.RotationUnits.REV,100,vex.VelocityUnits.PCT)
    rollerlift.rotate_to(-0.0,vex.RotationUnits.REV,100,vex.VelocityUnits.PCT)

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
            mag.spin(vex.DirectionType.FWD, 70, vex.VelocityUnits.PCT)
        elif con.buttonB.pressing():
            mag.spin(vex.DirectionType.FWD, -70, vex.VelocityUnits.PCT)
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



  
    
    
    
    



