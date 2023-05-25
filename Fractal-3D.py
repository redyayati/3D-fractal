from vpython import *
import numpy as np 


scene.width = 1050
scene.height = 900
scene.background = color.color = vector(0, 0, 0)

def tree(start , end , t ,theta) : 
    l = mag(end-start)
    ang_vec = norm(end-start)
    cylinder(pos=start, length = l , radius = t, axis = ang_vec)
    if l > 8 : 
        if t > .2 : t -= .2
        l *= .8
        ang_vec_left = ang_vec.rotate(theta)
        ang_vec_left.mag = l
        ang_vec_left += end 
        ang_vec_right = ang_vec.rotate(-theta)
        ang_vec_right.mag = l
        ang_vec_right += end 
        tree(end,ang_vec_left, t , theta)
        tree(end,ang_vec_right, t , theta)


def tree3D(start , end , t ,theta , phi , col) : 
    l = mag(end-start)
    ang_vec = norm(end-start)
    cylinder(pos=start, length = l , radius = t, axis = ang_vec , color = col)
    if l > 8 : 
        if t > .2 : t -= .2
        l *= .8
        ang_vec_left = ang_vec.rotate(phi , axis = vector(0,0,1))
        ang_vec_left = ang_vec_left.rotate(-theta , axis = vector(0,1,0))
        ang_vec_left.mag = l
        ang_vec_left += end 

        ang_vec_right = ang_vec.rotate(-phi , axis = vector(0,0,1))
        ang_vec_right = ang_vec_right.rotate(theta , axis = vector(0,1,0))
        ang_vec_right.mag = l
        ang_vec_right += end 
        
        ang_vec_mid = ang_vec.rotate(theta , axis = vector(0,1,0))
        ang_vec_mid = ang_vec_mid.rotate(phi , axis = vector(1,0,0))
        ang_vec_mid.mag = l
        ang_vec_mid += end 
        
        tree3D(end,ang_vec_left, t , theta, phi , color.red)
        tree3D(end,ang_vec_right, t , theta , phi , color.yellow)
        tree3D(end,ang_vec_mid, t , theta , phi , color.green)

start = vector(0,-40,0)
end = vector(0,-10,0)
# tree(start,end,1,np.pi/4)

phi = np.pi/4
theta = np.pi/6
dtheta = 2*np.pi/3

# base = cylinder(pos = vector (0,0,0), length = 10, axis = vector(0,1,0))
# b1 = cylinder(pos=vector(0,10,0), length = 10 , axis = vector(np.cos(phi)*np.cos(theta),np.sin(phi),np.cos(phi)*np.sin(theta)), color = color.red)
# b2 = cylinder(pos=vector(0,10,0), length = 10 , axis = vector(np.cos(phi)*np.cos(theta+dtheta),np.sin(phi),np.cos(phi)*np.sin(theta+dtheta)), color = color.green)
# b3 = cylinder(pos=vector(0,10,0), length = 10 , axis = vector(np.cos(phi)*np.cos(theta+2*dtheta),np.sin(phi),np.cos(phi)*np.sin(theta+2*dtheta)), color= color.yellow)

tree3D(start , end ,1, theta , phi , color.red)


while True : 
    pass
    # rate(500)
    
    # changed1 = b1.axis.rotate(.01 , axis=vector(1,0,0))
    # b1.axis = vector(changed1)
    # b1.length = 10

    # changed2 = b2.axis.rotate(.01)
    # b2.axis = vector(changed2)
    # b2.length = 10

    # changed3 = b3.axis.rotate(.01)
    # b3.axis = vector(changed3)
    # b3.length = 10


    