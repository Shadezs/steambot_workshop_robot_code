"""__CONFIG__
{"version":20,"widgetInfos":[{"hwid":"7","name":"left_motor","typeName":"motor","extraConfig":{"gearSetting":1,"reverse":false},"bufferIndex":0},{"hwid":"8","name":"rigth_motor","typeName":"motor","extraConfig":{"gearSetting":1,"reverse":false},"bufferIndex":1},{"hwid":"triport_adi","name":"triport_22","typeName":"triport","extraConfig":null,"bufferIndex":2},{"hwid":"adi_22_2","name":"blue1","typeName":"limit","extraConfig":null,"bufferIndex":3},{"hwid":"adi_22_3","name":"red1","typeName":"limit","extraConfig":null,"bufferIndex":4},{"hwid":"adi_22_4","name":"blue2","typeName":"limit","extraConfig":null,"bufferIndex":5},{"hwid":"adi_22_5","name":"red2","typeName":"limit","extraConfig":null,"bufferIndex":6},{"hwid":"drivetrain","name":"dt","typeName":"drivetrain","extraConfig":null,"bufferIndex":7},{"hwid":"controller","name":"con","typeName":"controller_one","extraConfig":null,"bufferIndex":8},{"hwid":"Axis1","name":"axis1","typeName":"controller_axis","extraConfig":null,"bufferIndex":9},{"hwid":"Axis2","name":"axis2","typeName":"controller_axis","extraConfig":null,"bufferIndex":10},{"hwid":"Axis3","name":"axis3","typeName":"controller_axis","extraConfig":null,"bufferIndex":11},{"hwid":"Axis4","name":"axis4","typeName":"controller_axis","extraConfig":null,"bufferIndex":12},{"hwid":"ButtonL1","name":"buttonL1","typeName":"controller_button","extraConfig":null,"bufferIndex":13},{"hwid":"ButtonL2","name":"buttonL2","typeName":"controller_button","extraConfig":null,"bufferIndex":14},{"hwid":"ButtonR1","name":"buttonR1","typeName":"controller_button","extraConfig":null,"bufferIndex":15},{"hwid":"ButtonR2","name":"buttonR2","typeName":"controller_button","extraConfig":null,"bufferIndex":16},{"hwid":"ButtonUp","name":"buttonUp","typeName":"controller_button","extraConfig":null,"bufferIndex":17},{"hwid":"ButtonDown","name":"buttonDown","typeName":"controller_button","extraConfig":null,"bufferIndex":18},{"hwid":"ButtonLeft","name":"buttonLeft","typeName":"controller_button","extraConfig":null,"bufferIndex":19},{"hwid":"ButtonRight","name":"buttonRight","typeName":"controller_button","extraConfig":null,"bufferIndex":20},{"hwid":"ButtonX","name":"buttonX","typeName":"controller_button","extraConfig":null,"bufferIndex":21},{"hwid":"ButtonB","name":"buttonB","typeName":"controller_button","extraConfig":null,"bufferIndex":22},{"hwid":"ButtonY","name":"buttonY","typeName":"controller_button","extraConfig":null,"bufferIndex":23},{"hwid":"ButtonA","name":"buttonA","typeName":"controller_button","extraConfig":null,"bufferIndex":24}]}"""
# VEX V5 Python Project
import sys
import vex
from vex import *

#region config
brain       = vex.Brain()
left_motor  = vex.Motor(vex.Ports.PORT7, vex.GearSetting.RATIO18_1, False)
rigth_motor = vex.Motor(vex.Ports.PORT8, vex.GearSetting.RATIO18_1, False)
blue1       = vex.Limit(brain.three_wire_port.b)
red1        = vex.Limit(brain.three_wire_port.c)
blue2       = vex.Limit(brain.three_wire_port.d)
red2        = vex.Limit(brain.three_wire_port.e)
con         = vex.Controller(vex.ControllerType.PRIMARY)
#endregion config
while True:
    
    if (blue1.value()==1):
        vex.BrainLcd.set_cursor(1,1)
        vex.BrainLcd.print_(" the jumper works")
        vex.BrainLcd.render()
