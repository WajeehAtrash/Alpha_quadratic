import  pointData
import numpy as np
from djitellopy import tello
from time import sleep
from movementCap import TelloDrone
import math




def moveToDoor(centerx,centery):
    _,arr=pointData.getAproxDist(centerx,centery)
    for i in range(len(arr)):
        TelloDrone.move_forward(arr[i])
        sleep(2)


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
    try:
        TelloDrone.connect()
        exit_help(land_deg, degree, centerx, centery, quarter)
    except:
        exit_help(land_deg, degree, centerx, centery, quarter)

#----------------------------------------------------------------------------
def exit_help(land_deg,degree,centerx,centery,quarter):
    print("Drone Battery:", TelloDrone.get_battery())
    # degree=degree-15
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

    # if (quarter == 1):
    #     if (land_deg < 0):
    #         TelloDrone.rotate_counter_clockwise(-degree - land_deg)
    #     else:
    #         TelloDrone.rotate_counter_clockwise(land_deg)
    #         TelloDrone.rotate_clockwise(-degree)
    #     moveToDoor(centerx, centery)
    # if (quarter == 2):
    #     if (land_deg < 0):
    #         TelloDrone.rotate_clockwise(180 - land_deg - degree)
    #     else:
    #         TelloDrone.rotate_clockwise(180 - degree - land_deg)
    #     moveToDoor(centerx, centery)
    # if (quarter == 3):
    #     if (land_deg < 0):
    #         TelloDrone.rotate_counter_clockwise(180 + land_deg + degree)
    #     else:
    #         TelloDrone.rotate_counter_clockwise(180 - land_deg - degree)
    #     moveToDoor(centerx, centery)
    # if (quarter == 4):
    #     if (land_deg < 0):
    #         TelloDrone.rotate_counter_clockwise(-land_deg)
    #         TelloDrone.rotate_clockwise(degree)
    #     else:
    #         TelloDrone.rotate_counter_clockwise(180 - land_deg - degree)
    #     moveToDoor(centerx, centery)







# if (quarter == 1):
 #        if (land_deg < 0):
 #            TelloDrone.rotate_clockwise(-degree - land_deg)
 #        else:
 #            TelloDrone.rotate_counter_clockwise(land_deg)
 #            TelloDrone.rotate_clockwise(-degree)
 #        moveToDoor(centerx, centery)
 #    if (quarter == 2):
 #        if (land_deg < 0):
 #            TelloDrone.rotate_clockwise(180 - land_deg - degree)
 #        else:
 #            TelloDrone.rotate_clockwise(180 - degree - land_deg)
 #        moveToDoor(centerx, centery)
 #    if (quarter == 3):
 #        if (land_deg < 0):
 #            TelloDrone.rotate_counter_clockwise(180 + land_deg + degree)
 #        else:
 #            TelloDrone.rotate_counter_clockwise(180 - land_deg - degree)
 #        moveToDoor(centerx, centery)
 #    if (quarter == 4):
 #        if (land_deg < 0):
 #            TelloDrone.rotate_counter_clockwise(-land_deg)
 #            TelloDrone.rotate_clockwise(degree)
 #        else:
 #            TelloDrone.rotate_counter_clockwise(180 - land_deg - degree)
 #        moveToDoor(centerx, centery)
 #
 #    TelloDrone.land()