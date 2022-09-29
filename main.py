#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.media.ev3dev import SoundFile, ImageFile


# Initializing up the pieces that will be used

ev3 = EV3Brick()

rightMotor = Motor(port = Port.C, positive_direction = Direction.CLOCKWISE)
leftMotor = Motor(port = Port.A, positive_direction = Direction.CLOCKWISE)

us_sensor = UltrasonicSensor(port = Port.S2)
touch_sensor = TouchSensor(port = Port.S4)


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

rightMotor.run(100)
leftMotor.run(100)
ev3.speaker.beep()

avg_speed_per_round = 0
area_traveled = 0 
target_distance  = 634350

for i in range(1000000):
    
    avg = (leftMotor.speed() + rightMotor.speed())/2
    diff = abs(leftMotor.speed() - rightMotor.speed())
    area_traveled = area_traveled + avg
   
    if( not(target_distance - 100 < area_traveled < target_distance+50)):
   
        if(diff > 15):
         diff = diff/2
       
         if(diff/2 > 20):
            diff = 20

        if(leftMotor.speed()< rightMotor.speed()):
         rightMotor.run(avg - diff)
         leftMotor.run(avg + diff+3.75)

        elif (leftMotor.speed()> rightMotor.speed()):
          rightMotor.run(avg + diff)
          leftMotor.run(avg - diff)

        elif(i%2==0):
            rightMotor.run(100)
            leftMotor.run(100)
        else:
            leftMotor.run(100)
            rightMotor.run(100)
    else:
        rightMotor.run_time(0,0,then=Stop.BRAKE, wait = False)
        leftMotor.run_time(0,0,then=Stop.BRAKE, wait = True)
        rightMotor.run_time(0,0,then=Stop.BRAKE, wait = False)
        leftMotor.run_time(0,0,then=Stop.BRAKE, wait = True)

        ev3.speaker.beep()
        ev3.speaker.play_file("boing.wav")
        break
   

"""
------- Objective 2: Move robot until it is 50cm from the wall -------
"""

# Wait until center button press to move
while(pressed == 0):
    if(Button.CENTER in EV3Brick.buttons.pressed()): 
      pressed = 1

pressed = 0 

leftMotor.run(100)
rightMotor.run(100)

# Robots moves until 50cm from wall
while(us_sensor.distance() > 500):
    avg = (leftMotor.speed() + rightMotor.speed())/2
    diff = abs(leftMotor.speed() - rightMotor.speed())
    area_traveled = area_traveled + avg   
   
    if(diff > 15):
        diff = diff/2
       
    if(diff/2 > 20):
        diff = 20

    if(leftMotor.speed()< rightMotor.speed()):
        rightMotor.run(avg - diff-0.25)
        leftMotor.run(avg + diff+3.75)

    elif (leftMotor.speed()> rightMotor.speed()):
        rightMotor.run(avg + diff)
        leftMotor.run(avg - diff)

    elif(i%2==0):
        rightMotor.run(100)
        leftMotor.run(100)
    else:
        leftMotor.run(100)
        rightMotor.run(100)

leftMotor.run_time(0,0,then=Stop.BRAKE, wait = False)
rightMotor.run_time(0,0,then=Stop.BRAKE, wait = True)
leftMotor.run_time(0,0,then=Stop.BRAKE, wait = False)
rightMotor.run_time(0,0,then=Stop.BRAKE, wait = True)

ev3.speaker.play_file("boing.wav")


"""
------- Objective 3: Move robot until it touches the wall and then move back 50cm -------
"""

# Wait until center button press to move
while(pressed == 0):
    if(Button.CENTER in EV3Brick.buttons.pressed()): 
      pressed = 1

pressed = 0 

rightMotor.run(100)
leftMotor.run(100)

# Robot moves until it is touching the wall
while((not touch_sensor.pressed()) and (us_sensor.distance() < 1000)):
    avg = (leftMotor.speed() + rightMotor.speed())/2
    diff = abs(leftMotor.speed() - rightMotor.speed())
    area_traveled = area_traveled + avg
   
   
    if(diff > 15):
        diff = diff/2
       
    if(diff/2 > 20):
        diff = 20

    if(leftMotor.speed()< rightMotor.speed()):
        rightMotor.run(avg - diff-0.25)
        leftMotor.run(avg + diff+3.75)

    elif (leftMotor.speed()> rightMotor.speed()):
        rightMotor.run(avg + diff)
        leftMotor.run(avg - diff)

    elif(i%2==0):
        rightMotor.run(100)
        leftMotor.run(100)
    else:
        leftMotor.run(100)
        rightMotor.run(100)

leftMotor.run_time(0,0,then=Stop.BRAKE, wait = False)
rightMotor.run_time(0,0,then=Stop.BRAKE, wait = True)

ev3.speaker.play_file("boing.wav")

rightMotor.run(-100)
leftMotor.run(-100)

wait(1000)

# Robot moves backwards until it is 50cm from wall
while (us_sensor.distance() < 500):
    filler = 0

rightMotor.run_time(0,0,then=Stop.BRAKE, wait = False)
leftMotor.run_time(0,0,then=Stop.BRAKE, wait = True)

#ev3.speaker.play_file("Hotline Bling.wav")
ev3.speaker.beep()