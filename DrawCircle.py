import numpy as np

def circle_3D(C,n,r,t,clocking):
    phi = np.arctan2(n[1],n[0])
    psi = np.arctan2( np.sqrt(np.power(n[0],2) + np.power(n[1],2)) ,n[2])
    if clocking == 'L':
        x = C[0] - r*( np.cos(t)*np.sin(phi) + np.sin(t)*np.cos(psi)*np.cos(phi) )
        y = C[1] + r*( np.cos(t)*np.cos(phi) - np.sin(t)*np.cos(psi)*np.sin(phi) )
        z = C[2] + r*( np.sin(t)*np.sin(psi) )
        points = np.array([x,y,z])
    elif clocking == 'R':
        x = C[0] - r*( np.cos(-t)*np.sin(phi) + np.sin(-t)*np.cos(psi)*np.cos(phi) )
        y = C[1] + r*( np.cos(-t)*np.cos(phi) - np.sin(-t)*np.cos(psi)*np.sin(phi) )
        z = C[2] + r*( np.sin(-t)*np.sin(psi) )
        points = np.array([x,y,z])
    return points