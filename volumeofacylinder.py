# Name: Richard Truong rxt5171@psu.edu
# CMPSC 121 HW 1 2.0
# Date: 1/29/2018
# Title: VolumeofACylinder
# Description: User enters radius and height, program multiples Pi by radius squared by height, prints volume in cubic meters

Pi = 3.14

radius_sphere= float(input('Enter the Radius of the sphere:')) # user inputs float value for radius of the sphere
height_cylinder= float(input('Enter Height of the cylinder:')) # user inputs float value for height of the cylinder

volume_cylinder= Pi * radius_sphere * radius_sphere * height_cylinder # Pi*r^2*h = volume of a cylinder

print ('The volume of the cyclinder is = %.2f' % volume_cylinder, 'cubic meters')

##Enter the Radius of the sphere:2
##Enter Height of the cylinder:2
##The volume of the cyclinder is = 25.12 cubic meters

##Enter the Radius of the sphere:3
##Enter Height of the cylinder:6
##The volume of the cyclinder is = 169.56 cubic meters

##Enter the Radius of the sphere:5
##Enter Height of the cylinder:9
##The volume of the cyclinder is = 706.50 cubic meters
