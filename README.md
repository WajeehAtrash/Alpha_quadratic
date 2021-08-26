# Alpha_quadratic
  Alpha_quadratic Team
  
  RTLAB with prof. Dan Feldman

  Team members :
  
    Saji Assi
    Wajeeh Atrash
    Farouq Kraeem
    
  Overview of the project:
      
      We are working with dji tello drone.
      In our project we created a code that is capable to fly the drone and scan the room it is in, and returns a point cloud that we use
      to detect the door and to navigat from his position to the door and out of the room.
      
   How it works:
     
     Our project is divided into number of classes,
     our main class is Run wich contains coomand for the drone to:
     I) Fly the drone and scan the room (movementCap class)
     " The point cloud is saved and procced through pointData class"
     II) detect the door and exit (Exit class)
     
     Between step I and II the drone will land and wait for command to fly again (the command "fly" is given by the programmer after the ORB_SLAM is shut down).
     
     ** So all you need to do is go to Run class and run the project**
     
   Video for the program:
   
      The link : 
        
        https://campushaifaac-my.sharepoint.com/:v:/g/personal/watras02_campus_haifa_ac_il/EU_9dBQI1BpNm5sZGyZj0_EBtfhb6wfv_9SvoKnbmakDag?e=9xrH5i
