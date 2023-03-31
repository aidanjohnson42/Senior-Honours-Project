import numpy as np
import matplotlib.pyplot as plt
    
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
    
angm01000_in = open('C:/Users/theev/Documents/Homework/SHP/data/angm/d07_e08/angm01000', 'r') #all e=0.8
angm01980_in = open('C:/Users/theev/Documents/Homework/SHP/data/angm/d07_e08/angm01980', 'r')
angm02200_in = open('C:/Users/theev/Documents/Homework/SHP/data/angm/d07_e08/angm02200', 'r')
angm02300_in = open('C:/Users/theev/Documents/Homework/SHP/data/angm/d07_e08/angm02300', 'r')
angm02800_in = open('C:/Users/theev/Documents/Homework/SHP/data/angm/d07_e08/angm02800', 'r')
angm03000_in = open('C:/Users/theev/Documents/Homework/SHP/data/angm/d07_e08/angm03000', 'r')
angm04000_in = open('C:/Users/theev/Documents/Homework/SHP/data/angm/d07_e08/angm04000', 'r')
angm04100_in = open('C:/Users/theev/Documents/Homework/SHP/data/angm/d07_e08/angm04100', 'r')
angm04200_in = open('C:/Users/theev/Documents/Homework/SHP/data/angm/d07_e08/angm04200', 'r')
angm04300_in = open('C:/Users/theev/Documents/Homework/SHP/data/angm/d07_e08/angm04300', 'r')
angm04400_in = open('C:/Users/theev/Documents/Homework/SHP/data/angm/d07_e08/angm04400', 'r')
angm04500_in = open('C:/Users/theev/Documents/Homework/SHP/data/angm/d07_e08/angm04500', 'r')
angm04600_in = open('C:/Users/theev/Documents/Homework/SHP/data/angm/d07_e08/angm04600', 'r')
angm04700_in = open('C:/Users/theev/Documents/Homework/SHP/data/angm/d07_e08/angm04700', 'r')
angm04800_in = open('C:/Users/theev/Documents/Homework/SHP/data/angm/d07_e08/angm04800', 'r')
angm04900_in = open('C:/Users/theev/Documents/Homework/SHP/data/angm/d07_e08/angm04900', 'r')
angm04940_in = open('C:/Users/theev/Documents/Homework/SHP/data/angm/d07_e08/angm04940', 'r')
angm05000_in = open('C:/Users/theev/Documents/Homework/SHP/data/angm/d07_e08/angm05000', 'r')
angm05100_in = open('C:/Users/theev/Documents/Homework/SHP/data/angm/d07_e08/angm05100', 'r')
angm06000_in = open('C:/Users/theev/Documents/Homework/SHP/data/angm/d07_e08/angm06000', 'r')
angm06900_in = open('C:/Users/theev/Documents/Homework/SHP/data/angm/d07_e08/angm06900', 'r')

angm02000_e04_in = open('C:/Users/theev/Documents/Homework/SHP/data/angm/d05_e04/angm02000')
angm04000_e04_in = open('C:/Users/theev/Documents/Homework/SHP/data/angm/d05_e04/angm04000')
angm06000_e04_in = open('C:/Users/theev/Documents/Homework/SHP/data/angm/d05_e04/angm06000')

angm02000_e06_in = open('C:/Users/theev/Documents/Homework/SHP/data/angm/d06_e06/angm02000')
angm04000_e06_in = open('C:/Users/theev/Documents/Homework/SHP/data/angm/d06_e06/angm04000')
angm06000_e06_in = open('C:/Users/theev/Documents/Homework/SHP/data/angm/d06_e06/angm06000')

angm01000_e08 = ang_ext(angm01000_in)
angm01980_e08 = ang_ext(angm01980_in)
angm02200_e08 = ang_ext(angm02200_in)
angm02300_e08 = ang_ext(angm02300_in)
angm02800_e08 = ang_ext(angm02800_in)
angm03000_e08 = ang_ext(angm03000_in)
angm04000_e08 = ang_ext(angm04000_in)
angm04100_e08 = ang_ext(angm04100_in)
angm04200_e08 = ang_ext(angm04200_in)
angm04300_e08 = ang_ext(angm04300_in)
angm04400_e08 = ang_ext(angm04400_in)
angm04500_e08 = ang_ext(angm04500_in)
angm04600_e08 = ang_ext(angm04600_in)
angm04700_e08 = ang_ext(angm04700_in)
angm04800_e08 = ang_ext(angm04800_in)
angm04900_e08 = ang_ext(angm04900_in)
angm04940_e08 = ang_ext(angm04940_in)
angm05000_e08 = ang_ext(angm05000_in)
angm05100_e08 = ang_ext(angm05100_in)
angm06000_e08 = ang_ext(angm06000_in)
angm06900_e08 = ang_ext(angm06900_in)

angm02000_e04 = ang_ext(angm02000_e04_in)
angm04000_e04 = ang_ext(angm04000_e04_in)
angm06000_e04 = ang_ext(angm06000_e04_in)

angm02000_e06 = ang_ext(angm02000_e06_in)
angm04000_e06 = ang_ext(angm04000_e06_in)
angm06000_e06 = ang_ext(angm06000_e06_in)


i = 6
ylab = "\u03B2, the tilt"


""" This one plots three separate figures
 fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize = (18,6))
#ax1.plot(angm01000[0,:,0], angm01000[0,:,i], label='1000')
ax3.plot(angm01980_e08[0,:,0], angm01980_e08[0,:,i], label='1980')
#ax1.plot(angm02800[0,:,0], angm02800[0,:,i], label='2800')
ax3.plot(angm04000_e08[0,:,0], angm04000_e08[0,:,i], label='4000')
#ax1.plot(angm05000[0,:,0], angm05000[0,:,i], label='5000')
#ax1.plot(angm04940[0,:,0], angm04940[0,:,i], label='4940')
ax3.plot(angm06000_e08[0,:,0], angm06000_e08[0,:,i], label='6000')
#ax1.plot(angm06900[0,:,0], angm06900[0,:,i], label='6900')

ax1.plot(angm02000_e04[0,:,0], angm02000_e04[0,:,i], label='2000')
ax1.plot(angm04000_e04[0,:,0], angm04000_e04[0,:,i], label='4000')
ax1.plot(angm06000_e04[0,:,0], angm06000_e04[0,:,i], label='6000')

ax2.plot(angm02000_e06[0,:,0], angm02000_e06[0,:,i], label='2000')
ax2.plot(angm04000_e06[0,:,0], angm04000_e06[0,:,i], label='4000')
ax2.plot(angm06000_e06[0,:,0], angm06000_e06[0,:,i], label='6000')

ax1.set_xlabel("Radius, au", fontsize = 16)
ax2.set_xlabel("Radius, au", fontsize = 16)
ax3.set_xlabel("Radius, au", fontsize = 16)

ax1.set_xlim(0, 50)
ax2.set_xlim(0, 50)
ax3.set_xlim(0, 50)

ax1.set_ylim(5, 6.3)
ax2.set_ylim(5, 6.3)
ax3.set_ylim(5, 6.3)

ax1.set_title("e = 0.4", fontsize = 16)
ax2.set_title("e = 0.6", fontsize = 16)
ax3.set_title("e = 0.8", fontsize = 16)
ax1.set_ylabel(ylab, fontsize = 16)
ax1.legend()
ax2.legend()
ax3.legend()
fig.suptitle("Plot of twist against radius for three eccentricities", fontsize = 20)

"""



#""" This plots just one figure
fig, ax1 = plt.subplots(figsize = (8,8))
ax1.plot(angm04000_e08[0,:,0], angm04000_e08[0,:,i], label='4000')
ax1.legend()
ax1.set_ylabel(ylab)
ax1.set_xlabel("Radius")
ax1.set_ylim(0.2,1.4)
ax1.set_xlim(1, 7)
#"""
