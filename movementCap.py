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
TelloDrone.send_rc_control(0,0,30,0)#moving up
for i in range(19):
    TelloDrone.rotate_clockwise(20)
    sleep(3)
TelloDrone.streamoff()
print("done")
