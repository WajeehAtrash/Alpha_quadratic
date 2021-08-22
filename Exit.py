import  pointData
import numpy as np
from djitellopy import tello
from time import sleep
import math

def moveToDoor(centerx,centery):
    _,arr=pointData.getAproxDist(centerx,centery)
    for i in range(len(arr)):
        TelloDrone.move_forward(arr[i])
        sleep(2)

x1,y,z1=np.loadtxt('/home/wajeeh/pointData.csv',unpack=True,delimiter=',')
rectangle =pointData.getRectangle(x1,z1)
size=len(x1)
midX = float(sum(x1)) / float(size)
midZ = float(sum(z1)) / float(size)
x,z=pointData.deletePointsFromRectangle(rectangle,x1, z1)
# x,z=deletePointsFromRectangle(x,z)

quarter,centerx,centery = pointData.getQuarterOfDoor(x, z, midX, midZ)

degree = pointData.getDegreeRotationV2(centerx,centery,midX,midZ)
print(degree,'degreeee + quarter ',quarter)
TelloDrone=tello.Tello()
TelloDrone.connect()
print("Drone Battery:",TelloDrone.get_battery())
# degree=degree-15
# TelloDrone.get_yaw()
TelloDrone.send_rc_control(0,0,0,0)
print('YAW degree:',TelloDrone.get_yaw())
TelloDrone.takeoff()
TelloDrone.move_up(80)
if(quarter==1):
    if(TelloDrone.get_yaw()<0):
        TelloDrone.rotate_counter_clockwise(degree - TelloDrone.get_yaw())
        print(degree - TelloDrone.get_yaw())
    else:
        TelloDrone.rotate_counter_clockwise(abs(degree - TelloDrone.get_yaw()))
        print(abs(degree - TelloDrone.get_yaw()))
    moveToDoor(centerx,centery)
if(quarter==2):
    if (TelloDrone.get_yaw() < 0):
        TelloDrone.rotate_clockwise(abs(180-degree - TelloDrone.get_yaw()))
    else:
        TelloDrone.rotate_clockwise(180-degree - TelloDrone.get_yaw())
    moveToDoor(centerx,centery)
if(quarter==3):
    if (TelloDrone.get_yaw() < 0):
        TelloDrone.rotate_counter_clockwise(abs(degree-TelloDrone.get_yaw()))
    else:
        TelloDrone.rotate_counter_clockwise(TelloDrone.get_yaw()+90+degree)
    moveToDoor(centerx,centery)
if(quarter==4):
    if (TelloDrone.get_yaw() < 0):
        TelloDrone.rotate_counter_clockwise(abs(degree-TelloDrone.get_yaw()))
    else:
        TelloDrone.rotate_counter_clockwise(TelloDrone.get_yaw()+degree)
    moveToDoor(centerx,centery)

TelloDrone.land()