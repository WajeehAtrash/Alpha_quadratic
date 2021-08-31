# used to see the cloud point  plot
from matplotlib import pyplot as plt
def show_Plot(xPoints,zPoints,title='chart'): # shows a plot for the givin points
    fig = plt.figure()
    plt.plot(xPoints, zPoints, 'o', color='black')
    plt.title(title)
    plt.ylabel('Y axis')
    plt.xlabel('X axis')
    plt.show()




def show_plot_Special(xPoints,zPoints,specialPoints,title='chart'):# showing a chart with a red points that we give in special points
    fig = plt.figure()
    plt.plot(xPoints, zPoints, 'o', color='black')
    for i in range (len(specialPoints)):
        plt.plot(specialPoints[i][0], specialPoints[i][1], 'o', color='red')
    plt.title(title)
    plt.ylabel('Y axis')
    plt.xlabel('X axis')
    plt.show()