import math

ra_dec_0 = [0.0138, 0.0375]
ra_dec_1 = [0.0308, 0.0607]
ra_dec_2 = [-0.0142, -0.0389]
ra_dec_3 = [-0.0203, -0.0560]

r_mag_0 = (ra_dec_0[0]**2 + ra_dec_0[1]**2)**(0.5)
r_mag_rads_0 = r_mag_0 * 4.8481e-6
R_0 = ( r_mag_rads_0 * 140 ) * 206265 #radius in au
print("Radius 1 calculated as ", R_0, " au")

r_mag_1 = (ra_dec_1[0]**2 + ra_dec_1[1]**2)**(0.5)
r_mag_rads_1 = r_mag_1 * 4.8481e-6
R_1 = ( r_mag_rads_1 * 140 ) * 206265 #radius in au
print("Radius 2 calculated as ", R_1, " au")

r_mag_2 = (ra_dec_2[0]**2 + ra_dec_2[1]**2)**(0.5)
r_mag_rads_2 = r_mag_2 * 4.8481e-6
R_2 = ( r_mag_rads_2 * 140 ) * 206265 #radius in au
print("Radius 3 calculated as ", R_2, " au")

r_mag_3 = (ra_dec_3[0]**2 + ra_dec_3[1]**2)**(0.5)
r_mag_rads_3 = r_mag_3 * 4.8481e-6
R_3 = ( r_mag_rads_3 * 140 ) * 206265 #radius in au
print("Radius 4 calculated as ", R_3, " au")


#imshow obtain:
im_x_coord = (ra_dec_0[0] / 0.355)*150.5
im_y_coord = (ra_dec_0[1] / 0.350)*150.5
im_coords_0 = [(150.5 - im_x_coord), (150.5 - im_y_coord)]
print(im_coords_0)

im_x_coord = (ra_dec_1[0] / 0.355)*150.5
im_y_coord = (ra_dec_1[1] / 0.350)*150.5
im_coords_1 = [(150.5 - im_x_coord), (150.5 - im_y_coord)]
print(im_coords_1)

im_x_coord = (ra_dec_2[0] / 0.355)*150.5
im_y_coord = (ra_dec_2[1] / 0.350)*150.5
im_coords_2 = [(150.5 - im_x_coord), (150.5 - im_y_coord)]
print(im_coords_2)

im_x_coord = (ra_dec_3[0] / 0.355)*150.5
im_y_coord = (ra_dec_3[1] / 0.350)*150.5
im_coords_3 = [(150.5 - im_x_coord), (150.5 - im_y_coord)]
print(im_coords_3)


theta = 1 #radians

h_0 = 0.1654 # au
h_1 = 1.65230
h_2 = 0.58920
h_3 = 2.41907

omega_0 = 2 * math.atan( ((math.tan(theta))**2)/((h_0 / R_0)**2) - 1 )
omega_1 = 2 * math.atan( ((math.tan(theta))**2)/((h_1 / R_1)**2) - 1 )
omega_2 = 2 * math.atan( ((math.tan(theta))**2)/((h_2 / R_2)**2) - 1 )
omega_3 = 2 * math.atan( ((math.tan(theta))**2)/((h_3 / R_3)**2) - 1 )

print("Omega 1 ", math.degrees(omega_0))
print("Omega 2 ", math.degrees(omega_1))
print("Omega 3 ", math.degrees(omega_2))
print("Omega 4 ", math.degrees(omega_3))