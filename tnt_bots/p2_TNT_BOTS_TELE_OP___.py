"""__CONFIG__
{"version":20,"widgetInfos":[{"hwid":"1","name":"intake_motor","typeName":"motor","extraConfig":null,"bufferIndex":0},{"hwid":"2","name":"left_motor","typeName":"motor","extraConfig":null,"bufferIndex":1},{"hwid":"3","name":"right_motor","typeName":"motor_rp","extraConfig":null,"bufferIndex":2},{"hwid":"4","name":"trapdoor_motor","typeName":"motor","extraConfig":null,"bufferIndex":3},{"hwid":"5","name":"backlift","typeName":"motor_rp","extraConfig":null,"bufferIndex":4},{"hwid":"6","name":"Front_Lift","typeName":"motor_rp","extraConfig":null,"bufferIndex":5},{"hwid":"drivetrain","name":"dt","typeName":"drivetrain","extraConfig":{"leftMotorHwId":"2","rightMotorHwId":"3","wheelTravel":200,"trackWidth":225},"bufferIndex":6},{"hwid":"lcd","name":"lcd","typeName":"lcd","extraConfig":null,"bufferIndex":7},{"hwid":"sound","name":"sound","typeName":"sound","extraConfig":null,"bufferIndex":8},{"hwid":"btn_chk","name":"button_check","typeName":"face_button","extraConfig":null,"bufferIndex":9},{"hwid":"btn_up","name":"button_up","typeName":"face_button","extraConfig":null,"bufferIndex":10},{"hwid":"btn_down","name":"button_down","typeName":"face_button","extraConfig":null,"bufferIndex":11},{"hwid":"joystick","name":"Joystick","typeName":"joystick","extraConfig":null,"bufferIndex":12},{"hwid":"AxisA:y","name":"axisA:Y","typeName":"joystick_axis","extraConfig":null,"bufferIndex":13},{"hwid":"AxisB:x","name":"axisB:X","typeName":"joystick_axis","extraConfig":null,"bufferIndex":14},{"hwid":"AxisC:x","name":"axisC:X","typeName":"joystick_axis","extraConfig":null,"bufferIndex":15},{"hwid":"AxisD:y","name":"axisD:Y","typeName":"joystick_axis","extraConfig":null,"bufferIndex":16},{"hwid":"Eu","name":"eu","typeName":"joystick_button","extraConfig":null,"bufferIndex":17},{"hwid":"Ed","name":"ed","typeName":"joystick_button","extraConfig":null,"bufferIndex":18},{"hwid":"Fu","name":"fu","typeName":"joystick_button","extraConfig":null,"bufferIndex":19},{"hwid":"Fd","name":"fd","typeName":"joystick_button","extraConfig":null,"bufferIndex":20},{"hwid":"Lu","name":"lu","typeName":"joystick_button","extraConfig":null,"bufferIndex":21},{"hwid":"Ld","name":"ld","typeName":"joystick_button","extraConfig":null,"bufferIndex":22},{"hwid":"Ru","name":"ru","typeName":"joystick_button","extraConfig":null,"bufferIndex":23},{"hwid":"Rd","name":"rd","typeName":"joystick_button","extraConfig":null,"bufferIndex":24}]}"""
# VEX IQ Python-Project😁🧇
import sys
import vexiq

#region config🍧
intake_motor   = vexiq.Motor(1)
left_motor     = vexiq.Motor(2)
right_motor    = vexiq.Motor(3, True) # Reverse Polarity
trapdoor_motor = vexiq.Motor(4)
backlift       = vexiq.Motor(5, True) # Reverse Polarity
Front_Lift     = vexiq.Motor(6, True) # Reverse Polarity

import drivetrain
dt             = drivetrain.Drivetrain(left_motor, right_motor, 200, 225)
Joystick       = vexiq.Joystick()
#endregion config🍉🍧🍨🧁

Joystick.set_deadband(10)
while True:
    #The drive motor yay DERP!!!
    left_motor.run((Joystick.axisA()))
    right_motor.run((Joystick.axisD()))
    #The intake code yay derp!
    if Joystick.bLup():
        intake_motor.run(100)
    elif Joystick.bLdown():
        intake_motor.run(-100)
    else:
        intake_motor.off()
    #The backlift code yay derp!
    if Joystick.bRup():
        backlift.run(100)
    elif Joystick.bRdown():
        backlift.run(-100)
    else:
        backlift.brake()
    #The trapdoor code yay derp!
    if Joystick.bEup():
        trapdoor_motor.run_until(100,360)
    elif Joystick.bEdown():
        trapdoor_motor.run_until(-100,360)
    else:
        trapdoor_motor.off()
    if Joystick.bFup():
        Front_Lift.run(100)
    elif Joystick.bFdown():
        Front_Lift.run(-100)
    else:
        Front_Lift.brake()