
from math import sqrt, cos, sin, radians, atan

import cv2
import numpy as np
from matplotlib import pyplot as plt
import matplotlib.patches as mpatches

def inRectangle(rectPoint,xp,yp):
    tr=rectPoint[1]
    bl=rectPoint[3]
    #   ______________ tr
    #   |            |
    #   |    . (x,y) |
    #   |            |
    #bl --------------
    if (xp > bl[0] and xp < tr[0] and yp > bl[1] and yp < tr[1]):
        return True
    else:
        return False



def inRectangleUseSlope(rectPoint, xp, yp):
    # t => top
    # l => left
    # r =>right
    # d =>down
    tl=rectPoint[0]
    tr=rectPoint[1]
    dr=rectPoint[2]
    dl=rectPoint[3]

    # if there are two point with the same x => the rotation of the rectangle is 90
    # then check if the point in the rectangle in the simple way
    if(dl[0]-tl[0]==0):
        return inRectangle(rectPoint,xp,yp)


    #else we check if the point is in the rectangle by use the slope
    m1=float(dl[1]-tl[1])/float(dl[0]-tl[0])
    m2=float(dl[1]-dr[1])/float(dl[0]-dr[0])
    m3=float(tr[1]-tl[1])/float(tr[0]-tl[0])
    m4=float(tr[1]-dr[1])/float(tr[0]-dr[0])

    a1=float(dl[1]-yp)/float(dl[0]-xp)
    a2=float(tr[1]-yp)/float(tr[0]-xp)
    if(m2<=a1<=m1 and m3<=a2<=m4 ):
        return True
    return False
#---------------------------------------------------------------
#we return the new x,z
def deletePointsFromRectangle(firstOne,x1, z1):
    size=len(x1)
    x = []
    z = []
    Cos = sqrt(2)/2 #cos(45)
    Sin = sqrt(2)/2 #sin(45)
    print(Cos,Sin)
    secOne = [  [firstOne[0][0]*Cos + firstOne[0][1]*Sin, firstOne[0][0]*(-Sin) + firstOne[0][1]*Cos],
                [firstOne[1][0]*Cos + firstOne[1][1]*Sin, firstOne[1][0]*(-Sin) + firstOne[1][1]*Cos],
                [firstOne[2][0]*Cos + firstOne[2][1]*Sin, firstOne[2][0]*(-Sin) + firstOne[2][1]*Cos],
                [firstOne[3][0]*Cos + firstOne[3][1]*Sin, firstOne[3][0]*(-Sin) + firstOne[3][1]*Cos]]
    for i in range(size):
        # if (inRectangleUseSlope(secOne, x1[i], z1[i]) is False):
        if (inRectangleUseSlope(firstOne, x1[i], z1[i]) is False):
        # if (inRectangle(secOne, x1[i], z1[i]) is False):
            x.append(x1[i])
            z.append(z1[i])
    return x,z

def getRectangle(x1,z1):
    size = len(x1)
    x = []
    z = []
    midX = float(sum(x1)) / float(size)
    midZ = float(sum(z1)) / float(size)

    sumDic = 0
    for i in range(size):
        sumDic += sqrt((midX - x1[i]) ** 2 + (midZ - z1[i]) ** 2)

    sumDic = float(sumDic) / float(size)
    sumDic *= 2
    rectangle = [[midX - sumDic, midZ + sumDic],
                [midX + sumDic, midZ + sumDic],
                [midX + sumDic, midZ - sumDic],
                [midX - sumDic, midZ - sumDic]]
    return rectangle
#---------------------------------------------------------------------------------------------------------------------------
# rotataion matrix:
# cos   sin
# -sin  cos


#the files name that we work with
# x1,y,z1,a,b,c,d =np.loadtxt('/home/wajeeh/Downloads/pointData0.csv',unpack=True,delimiter=',')
# x1,y,z1=np.loadtxt('/home/wajeeh/pointDataImproved/pointData305.csv',unpack=True,delimiter=',')
# x1,y,z1 =np.loadtxt('/home/wajeeh/pointDataImproved/pointData205.csv',unpack=True,delimiter=',')
x1,y,z1=np.loadtxt('/home/wajeeh/pointData.csv',unpack=True,delimiter=',')

rectangle =getRectangle(x1,z1)

x,z=deletePointsFromRectangle(rectangle,x1, z1)
# x,z=deletePointsFromRectangle(x,z)

fig=plt.figure()
plt.plot(x,z,'o',color='black')
plt.title('chart')
plt.ylabel('Y axis')
plt.xlabel('X axis')
plt.show()
#---------------------------------------------------------------------------------------------------------------------------

