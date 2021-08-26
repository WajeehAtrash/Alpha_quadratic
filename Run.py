import movementCap
import Exit
land_deg=movementCap.fly_cap()
print('wait for orb_slam and the drone then enter fly....')
x=input()
while x!='fly':
    print('wait')
    x=input()
print(land_deg)
Exit.exit_door(land_deg)