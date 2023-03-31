import numpy as np
import matplotlib.pyplot as plt
import sys
import matplotlib.animation as animation
from matplotlib.animation import FuncAnimation
from matplotlib.animation import PillowWriter
from sklearn import preprocessing


def ang_ext(angm_in):
    data = np.genfromtxt(angm_in, skip_header = 2)
    
    radius = data[:,0]
    sigma = data[:,1] 
    hoverH = data[:,2] 
    lx = data[:,3]  
    ly = data[:,4]  
    lz = data[:,5] 
    tilt = data[:,6]  
    twist = data[:,7] 
    psi = data[:,8] #warp amplitude - v imp.
    HoverR = data[:,9] 
    ecc = data[:,10] 
    #alpha_sph = data[:,11] 
    #kappa = data[:,12] 
    #freq = data[:,13] 
    
    return np.dstack([radius, sigma, hoverH, lx, ly, lz, tilt, twist, psi, HoverR, ecc])
    
angm01000_e08 = ang_ext(open('C:/Users/theev/Documents/Homework/SHP/data/angm/d07_e08/angm01000', 'r')) #all e=0.8
angm01980_e08 = ang_ext(open('C:/Users/theev/Documents/Homework/SHP/data/angm/d07_e08/angm01980', 'r')) #very tedious but works well
angm02000_e08 = ang_ext(open('C:/Users/theev/Documents/Homework/SHP/data/angm/d07_e08/angm02000', 'r'))
angm02100_e08 = ang_ext(open('C:/Users/theev/Documents/Homework/SHP/data/angm/d07_e08/angm02100', 'r'))
angm02200_e08 = ang_ext(open('C:/Users/theev/Documents/Homework/SHP/data/angm/d07_e08/angm02200', 'r'))
angm02300_e08 = ang_ext(open('C:/Users/theev/Documents/Homework/SHP/data/angm/d07_e08/angm02300', 'r'))
angm02400_e08 = ang_ext(open('C:/Users/theev/Documents/Homework/SHP/data/angm/d07_e08/angm02400', 'r'))
angm02500_e08 = ang_ext(open('C:/Users/theev/Documents/Homework/SHP/data/angm/d07_e08/angm02500', 'r'))
angm02600_e08 = ang_ext(open('C:/Users/theev/Documents/Homework/SHP/data/angm/d07_e08/angm02600', 'r'))
angm02700_e08 = ang_ext(open('C:/Users/theev/Documents/Homework/SHP/data/angm/d07_e08/angm02700', 'r'))
angm02800_e08 = ang_ext(open('C:/Users/theev/Documents/Homework/SHP/data/angm/d07_e08/angm02800', 'r'))
angm02900_e08 = ang_ext(open('C:/Users/theev/Documents/Homework/SHP/data/angm/d07_e08/angm02900', 'r'))
angm03950_e08 = ang_ext(open('C:/Users/theev/Documents/Homework/SHP/data/angm/d07_e08/angm03950', 'r'))
angm04000_e08 = ang_ext(open('C:/Users/theev/Documents/Homework/SHP/data/angm/d07_e08/angm04000', 'r'))
angm04100_e08 = ang_ext(open('C:/Users/theev/Documents/Homework/SHP/data/angm/d07_e08/angm04100', 'r'))
angm04200_e08 = ang_ext(open('C:/Users/theev/Documents/Homework/SHP/data/angm/d07_e08/angm04200', 'r'))
angm04300_e08 = ang_ext(open('C:/Users/theev/Documents/Homework/SHP/data/angm/d07_e08/angm04300', 'r'))
angm04400_e08 = ang_ext(open('C:/Users/theev/Documents/Homework/SHP/data/angm/d07_e08/angm04400', 'r'))
angm04500_e08 = ang_ext(open('C:/Users/theev/Documents/Homework/SHP/data/angm/d07_e08/angm04500', 'r'))
angm04600_e08 = ang_ext(open('C:/Users/theev/Documents/Homework/SHP/data/angm/d07_e08/angm04600', 'r'))
angm04700_e08 = ang_ext(open('C:/Users/theev/Documents/Homework/SHP/data/angm/d07_e08/angm04700', 'r'))
angm04800_e08 = ang_ext(open('C:/Users/theev/Documents/Homework/SHP/data/angm/d07_e08/angm04800', 'r'))
angm04900_e08 = ang_ext(open('C:/Users/theev/Documents/Homework/SHP/data/angm/d07_e08/angm04900', 'r'))
angm04940_e08 = ang_ext(open('C:/Users/theev/Documents/Homework/SHP/data/angm/d07_e08/angm04940', 'r'))
angm05000_e08 = ang_ext(open('C:/Users/theev/Documents/Homework/SHP/data/angm/d07_e08/angm05000', 'r'))
angm05100_e08 = ang_ext(open('C:/Users/theev/Documents/Homework/SHP/data/angm/d07_e08/angm05100', 'r'))
angm05200_e08 = ang_ext(open('C:/Users/theev/Documents/Homework/SHP/data/angm/d07_e08/angm05200', 'r'))
angm05300_e08 = ang_ext(open('C:/Users/theev/Documents/Homework/SHP/data/angm/d07_e08/angm05300', 'r'))
angm05400_e08 = ang_ext(open('C:/Users/theev/Documents/Homework/SHP/data/angm/d07_e08/angm05400', 'r'))
angm05500_e08 = ang_ext(open('C:/Users/theev/Documents/Homework/SHP/data/angm/d07_e08/angm05500', 'r'))
angm05600_e08 = ang_ext(open('C:/Users/theev/Documents/Homework/SHP/data/angm/d07_e08/angm05600', 'r'))
angm05700_e08 = ang_ext(open('C:/Users/theev/Documents/Homework/SHP/data/angm/d07_e08/angm05700', 'r'))
angm05800_e08 = ang_ext(open('C:/Users/theev/Documents/Homework/SHP/data/angm/d07_e08/angm05800', 'r'))
angm05900_e08 = ang_ext(open('C:/Users/theev/Documents/Homework/SHP/data/angm/d07_e08/angm05900', 'r'))
angm06000_e08 = ang_ext(open('C:/Users/theev/Documents/Homework/SHP/data/angm/d07_e08/angm06000', 'r'))
angm06100_e08 = ang_ext(open('C:/Users/theev/Documents/Homework/SHP/data/angm/d07_e08/angm06100', 'r'))
angm06200_e08 = ang_ext(open('C:/Users/theev/Documents/Homework/SHP/data/angm/d07_e08/angm06200', 'r'))
angm06300_e08 = ang_ext(open('C:/Users/theev/Documents/Homework/SHP/data/angm/d07_e08/angm06300', 'r'))
angm06400_e08 = ang_ext(open('C:/Users/theev/Documents/Homework/SHP/data/angm/d07_e08/angm06400', 'r'))
angm06500_e08 = ang_ext(open('C:/Users/theev/Documents/Homework/SHP/data/angm/d07_e08/angm06500', 'r'))
angm06600_e08 = ang_ext(open('C:/Users/theev/Documents/Homework/SHP/data/angm/d07_e08/angm06600', 'r'))
angm06700_e08 = ang_ext(open('C:/Users/theev/Documents/Homework/SHP/data/angm/d07_e08/angm06700', 'r'))
angm06800_e08 = ang_ext(open('C:/Users/theev/Documents/Homework/SHP/data/angm/d07_e08/angm06800', 'r'))
angm06900_e08 = ang_ext(open('C:/Users/theev/Documents/Homework/SHP/data/angm/d07_e08/angm06900', 'r'))

i = 8 #change this value to the corresponding parameter and it will be plotted on the y-axis

disc_names = [angm01000_e08,angm01980_e08,angm02000_e08,angm02100_e08,angm02200_e08,angm02300_e08,angm02400_e08,\
              angm02500_e08,angm02600_e08,angm02700_e08,angm02800_e08,angm02900_e08,angm03950_e08,angm04000_e08,\
              angm04100_e08,angm04200_e08,angm04300_e08,angm04400_e08,angm04500_e08,angm04600_e08,angm04700_e08,\
              angm04800_e08,angm04900_e08,angm04940_e08,angm05000_e08,angm05100_e08,angm05200_e08,angm05300_e08,\
              angm05400_e08,angm05500_e08,angm05600_e08,angm05700_e08,angm05800_e08,angm05900_e08,angm06000_e08,\
              angm06100_e08,angm06200_e08,angm06300_e08,angm06400_e08,angm06500_e08,angm06600_e08,angm06700_e08,\
              angm06800_e08,angm06900_e08]
    
disc_labels = ['1000','1980','2000','2100','2200','2300','2400','2500','2600','2700','2800','2900','3950','4000',\
               '4100','4200','4300','4400','4500','4600','4700','4800','4900','4940','5000','5100','5200','5300',\
               '5400','5500','5600','5700','5800','5900','6000','6100','6200','6300','6400','6500','6600','6700',\
               '6800','6900']

fig, ax1 = plt.subplots(figsize = (8,8))

def animate(f):
    ax1.clear()
    ax1.set_xlim(0, 30)
    ax1.set_ylim(0, 7)
    ax1.set_xlabel("Radius, au", fontsize = 16)
    ax1.set_ylabel("Warp amplitude", fontsize = 16)
    ax1.plot( (disc_names[f])[0,:,0], ((disc_names[f])[0,:,i]), label=disc_labels[f], color='m')
    ax1.legend()

ani = FuncAnimation(fig, animate, frames=len(disc_names), interval=150, repeat=True)
ani.save("output_animation.gif", dpi=300, writer=PillowWriter(fps=1))