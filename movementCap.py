from djitellopy import tello
from time import sleep
import os
import threading

TelloDrone = tello.Tello()
TelloDrone.connect()

# function to run orb_slam in a different thread automatically
def run_slam():
    os.chdir('/home/wajeeh/ORB_SLAM2')
    OrbSlamCom = './Examples/Monocular/mono_tum Vocabulary/ORBvoc.txt Examples/Monocular/TUM1.yaml'
    os.system(OrbSlamCom)


def fly_cap():
    # connecting to the drone
    print("Drone Battery:", TelloDrone.get_battery())
    print("yaw degree", TelloDrone.get_yaw())
    # turning the drone camera on
    TelloDrone.streamoff()
    TelloDrone.streamon()
    print("run ORB_SLAM2")
    # turn on ORB_SLAM2 then press amy key in the console to let the drone takeoff
    run_Orbslam = threading.Thread(target=run_slam)
    run_Orbslam.start()
    # drone movment
    TelloDrone.send_rc_control(0, 0, 0, 0)
    sleep(1)
    TelloDrone.takeoff()
    # TelloDrone.move_up(80)
    sleep(3)
    for i in range(19):
        TelloDrone.rotate_clockwise(20)
        sleep(3)
        TelloDrone.move_up(20)
        sleep(3)
        TelloDrone.move_down(20)
        sleep(5)
    TelloDrone.land()
    TelloDrone.streamoff()
    print("done")
    print("Drone Battery:", TelloDrone.get_battery())
    landing_yaw_degree = TelloDrone.get_yaw()
    # landing_yaw_degree=-33
    run_Orbslam.join()
    return landing_yaw_degree