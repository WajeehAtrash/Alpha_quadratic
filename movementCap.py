from djitellopy import tello
from time import sleep
#connecting to the drone
TelloDrone=tello.Tello()
TelloDrone.connect()
print("Drone Battery:",TelloDrone.get_battery())
#turning the drone camera on
TelloDrone.streamoff()
TelloDrone.streamon()
print("run ORB_SLAM2")
#turn on ORB_SLAM2 then press amy key in the console to let the drone takeoff
input()
#drone movment
TelloDrone.takeoff()
#(left_righ,for_back,up_down,Yaw)
TelloDrone.send_rc_control(0,0,50,0)#moving up
sleep(4)
# TelloDrone.send_rc_control(20,0,0,0)#moving rgiht
# sleep(2)
TelloDrone.rotate_clockwise(45)#rotating 30 degree counter clock wise
sleep(4)
TelloDrone.rotate_clockwise(45)#rotating 30 degree counter clock wiseTelloDrone.rotate_clockwise(60)#rotating 30 degree
sleep(4)
TelloDrone.rotate_clockwise(45)#rotating 30 degree
sleep(4)
TelloDrone.rotate_clockwise(45)#rotating 30 degree
sleep(4)
TelloDrone.rotate_clockwise(45)#rotating 30 degree
sleep(4)
TelloDrone.rotate_clockwise(45)#rotating 30 degree
sleep(4)
TelloDrone.land()

sleep(4)
TelloDrone.rotate_clockwise(45)#rotating 30 degree counter clock wise
sleep(4)
TelloDrone.rotate_clockwise(45)#rotating 30 degree counter clock wise
sleep(4)
TelloDrone.rotate_clockwise(45)#rotating 30 degree counter clock wise
sleep(4)
TelloDrone.rotate_clockwise(45)#rotating 30 degree counter clock wise
sleep(4)
TelloDrone.rotate_clockwise(45)#rotating 30 degree counter clock wise
sleep(4)
TelloDrone.rotate_clockwise(45)#rotating 30 degree counter clock wise
sleep(4)
TelloDrone.streamoff()
print("done")
