from djitellopy import tello
from time import sleep
import  cv2
import os
import threading
def run_slam():
    os.chdir('/home/wajeeh/ORB_SLAM2')
    OrbSlamCom = './Examples/Monocular/mono_tum Vocabulary/ORBvoc.txt Examples/Monocular/TUM1.yaml'
    os.system(OrbSlamCom)
#connecting to the drone
TelloDrone=tello.Tello()
TelloDrone.connect()
print("Drone Battery:",TelloDrone.get_battery())
#turning the drone camera on
TelloDrone.streamoff()
TelloDrone.streamon()
print("run ORB_SLAM2")
#turn on ORB_SLAM2 then press amy key in the console to let the drone takeoff
run_Orbslam=threading.Thread(target=run_slam)
run_Orbslam.start()
#drone movment
TelloDrone.send_rc_control(0,0,0,0)
TelloDrone.takeoff()
TelloDrone.move_up(80)
# sleep(5)ove_up(80)
# TelloDrone.move_back(20)
# sleep(5)
# TelloDrone.move_forward(20)
sleep(5)
for i in range(18):
    # img=TelloDrone.get_frame_read().frame
    # img=cv2.resize((img,(640,480)))
    # cv2.imshow("drone view",img)
    # cv2.waitKey(1)
    TelloDrone.rotate_clockwise(20)
    sleep(5)
TelloDrone.land()
TelloDrone.streamoff()
print("done")
run_Orbslam.join()






