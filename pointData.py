from math import sqrt, cos, sin, radians, atan, pi
import numpy as np
from matplotlib import pyplot as plt



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
    x=[]
    z=[]
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

#---------------------------------------------------------------------------------------------------------------------------

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
def getQuarterOfDoor(x, y, xCenter, yCenter):
    size=len(x)
    dencity1=0
    dencity2=0
    dencity3=0
    dencity4=0

    # we use the sum to know the center of the dencity points in each qwart
    sum1x=0
    sum2x=0
    sum3x=0
    sum4x=0

    sum1y = 0
    sum2y = 0
    sum3y = 0
    sum4y = 0

    for i in range(size):
        if(x[i]<=xCenter and y[i]>=yCenter):
            sum1x +=x[i]
            sum1y +=y[i]
            dencity1 +=1
        elif( x[i]>=xCenter and y[i]>=yCenter):
            sum2x += x[i]
            sum2y += y[i]
            dencity2 +=1
        elif( x[i]>=xCenter and y[i]<=yCenter):
            sum3x += x[i]
            sum3y += y[i]
            dencity3+=1
        elif (x[i] <= xCenter and y[i] <= yCenter):
            sum4x += x[i]
            sum4y += y[i]
            # print(x[i],y[i])
            dencity4+=1
    maxDencity = max(dencity4,dencity3,dencity2,dencity1)
    print (dencity4,dencity3,dencity2,dencity1)
    print('-------------------------',xCenter,yCenter)
    if(maxDencity==dencity1):
        return 1,float(sum1x/dencity1),float(sum1y/dencity1)
    if(maxDencity==dencity2):
        return 2,float(sum2x/dencity2),float(sum2y/dencity2)
    if(maxDencity==dencity3):
        return 3,float(sum3x/dencity3),float(sum3y/dencity3)
    if(maxDencity==dencity4):
        return 4,float(sum4x/dencity4),float(sum4y/dencity4)

#---------------------------------------------------------------------------------------------------------------------------

def getDegreeRotation(xDirection,yDirection,xCenter,yCenter):

    lenA = sqrt( (xCenter-xDirection)**2 + (yCenter-yDirection)**2)
    lenB = abs(yDirection-yCenter)

    arctang = atan((float)(lenB)/(float)(lenA))
    # degree = radians(arctang)
    degree = (arctang)*180/pi
    return (int)(degree)



#---------------------------------------------------------------------------------------------------------------------------
# rotataion matrix:
# cos   sin
# -sin  cos


#the files name that we work with
# x1,y,z1,a,b,c,d =np.loadtxt('/home/wajeeh/Downloads/pointData0.csv',unpack=True,delimiter=',')
x1,y,z1=np.loadtxt('/home/wajeeh/pointData.csv',unpack=True,delimiter=',')
# x1,y,z1 =np.loadtxt('/home/wajeeh/pointDataImproved/pointData205.csv',unpack=True,delimiter=',')
# x1,y,z1=np.loadtxt('/home/wajeeh/pointData.csv',unpack=True,delimiter=',')


rectangle =getRectangle(x1,z1)
size=len(x1)
midX = float(sum(x1)) / float(size)
midZ = float(sum(z1)) / float(size)
x,z=deletePointsFromRectangle(rectangle,x1, z1)
# x,z=deletePointsFromRectangle(x,z)

quarter,centerx,centery = getQuarterOfDoor(x, z, midX, midZ)

degree = getDegreeRotation(centerx,centery,midX,midZ)
print(degree,'degreeee + quarter ',quarter)
# quarter 1 => rotate left by degree
# quarter 2 => rotate right by degree
# quatret 3 => rotate right by 180 - degree
# quatret 4 => rotate left by 180 - degree
fig=plt.figure()
plt.plot(x,z,'o',color='black')
plt.plot(midX,midZ,'o',color='red')
plt.plot(centerx,centery,'o',color='red')
plt.title('chart')
plt.ylabel('Y axis')
plt.xlabel('X axis')
plt.show()
#---------------------------------------------------------------------------------------------------------------------------

