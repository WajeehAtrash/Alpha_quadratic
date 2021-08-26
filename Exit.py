import  pointData
import numpy as np
from djitellopy import tello
from time import sleep
from movementCap import TelloDrone
import math



# moving the drone by the approximated value that we calculated
def moveToDoor(centerx,centery):
    _,arr=pointData.getAproxDist(centerx,centery)
    for i in range(len(arr)):
        TelloDrone.move_forward(arr[i])
        sleep(2)

#------------------------------------------------------------------------------------------------------
#this function gets  the needed data from the csv file and and do the calculations using the pointData script functions
def exit_door(land_deg):
    x1, y, z1 = np.loadtxt('/home/wajeeh/pointData.csv', unpack=True, delimiter=',')
    rectangle = pointData.getRectangle(x1, z1)
    size = len(x1)
    midX = float(sum(x1)) / float(size)
    midZ = float(sum(z1)) / float(size)
    x, z = pointData.deletePointsFromRectangle(rectangle, x1, z1)
    # x,z=deletePointsFromRectangle(x,z)

    quarter, centerx, centery = pointData.getQuarterOfDoor(x, z, midX, midZ)

    degree = pointData.getDegreeRotation(centerx, centery, midX, midZ)
    print(degree, 'degreeee + quarter ', quarter)
    try:# trying to connect to the drone ( if we lost connection)
        TelloDrone.connect()
        exit_help(land_deg, degree, centerx, centery, quarter)
    except:
        exit_help(land_deg, degree, centerx, centery, quarter)

#----------------------------------------------------------------------------
#help function to make the  drone face the door
def exit_help(land_deg,degree,centerx,centery,quarter):
    print("Drone Battery:", TelloDrone.get_battery())
    # degree=degree-15/home/wajeeh
    # TelloDrone.get_yaw()
    TelloDrone.send_rc_control(0, 0, 0, 0)
    print('YAW degree:', land_deg)
    TelloDrone.takeoff()
    TelloDrone.move_up(80)
    degree=degree+land_deg-18
    if(quarter==1):
        TelloDrone.rotate_counter_clockwise(degree)
        moveToDoor(centerx,centery)
    elif(quarter==2):
        TelloDrone.rotate_clockwise(degree)
        moveToDoor(centerx, centery)
    elif(quarter==3):
        TelloDrone.rotate_clockwise(180-degree)
        moveToDoor(centerx, centery)
    else:
        TelloDrone.rotate_counter_clockwise(180-degree)
        moveToDoor(centerx, centery)