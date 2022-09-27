#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.media.ev3dev import SoundFile, ImageFile
from pybricks.robotics import DriveBase


# Initializing up the pieces that will be used

ev3 = EV3Brick()

motor1 = Motor(port = Port.A, positive_direction = Direction.CLOCKWISE)
motor2 = Motor(port = Port.B, positive_direction = Direction.CLOCKWISE)

us_sensor = UltrasonicSensor(port = Port.S2)
touch_sensor = TouchSensor(port = Port.S1)


"""
------- Objective 1: Move robot until it moves 1.2 meters -------
"""

# Wait until center button press to move
pressed = 0 

while(pressed == 0):
    if(Button.CENTER in EV3Brick.buttons.pressed()): 
      pressed = 1

pressed = 0 

distance = us_sensor.distance()

if (distance > 2550):
    motor1.run(180)
    motor2.run(180)
    wait(1000)
else:
    motor1.run(180)
    motor2.run(180)
    while(distance - us_sensor.distance() < 1200):
        filler = 0


motor1.run_time(0,0,then=Stop.BRAKE, wait = False)
motor2.run_time(0,0,then=Stop.BRAKE, wait = True)

ev3.speaker.play_file("boing.wav")


"""
------- Objective 2: Move robot until it is 50cm from the wall -------
"""

# Wait until center button press to move
while(pressed == 0):
    if(Button.CENTER in EV3Brick.buttons.pressed()): 
      pressed = 1

pressed = 0 

motor2.run(180)
motor1.run(180)

# Robots moves until 50cm from wall
while(us_sensor.distance() > 500):
    filler=0

motor2.run_time(0,0,then=Stop.BRAKE, wait = False)
motor1.run_time(0,0,then=Stop.BRAKE, wait = True)

ev3.speaker.play_file("boing.wav")


"""
------- Objective 3: Move robot until it touches the wall and then move back 50cm -------
"""

# Wait until center button press to move
while(pressed == 0):
    if(Button.CENTER in EV3Brick.buttons.pressed()): 
      pressed = 1

pressed = 0 

motor2.run(180)
motor1.run(180)

# Robot moves until it is touching the wall
while((not touch_sensor.pressed()) and (us_sensor.distance() < 1000)):
    filler = 0

motor2.run_time(0,0,then=Stop.BRAKE, wait = False)
motor1.run_time(0,0,then=Stop.BRAKE, wait = True)

ev3.speaker.play_file("boing.wav")

# Wait until center button press to move
while(pressed == 0):
    if(Button.CENTER in EV3Brick.buttons.pressed()): 
      pressed = 1

pressed = 0 

motor1.run(-180)
motor2.run(-180)

wait(300)

# Robot moves backwards until it is 50cm from wall
while (us_sensor.distance() < 500):
    filler = 0

motor1.run_time(0,0,then=Stop.BRAKE, wait = False)
motor2.run_time(0,0,then=Stop.BRAKE, wait = True)

ev3.speaker.play_file("Hotline Bling.wav")