import numpy as np
from DrawCircle import circle_3D

def dubins_RSR(S,E,eS,eE,eN1,eN2,r1,r2):
    C1 = S + r1*(np.cross(eS,eN1))
    C2 = E + r2*(np.cross(eE,eN2))
    b = C2 - C1
    eb = b/np.linalg.norm(b)
    T1 = C1 + r1*np.cross(eN1,eb)
    T2 = C2 + r2*np.cross(eN2,eb)

    points = circle_3D(C1,eN1,r1,0,'R')
    Dir = (points - C1)/np.linalg.norm(points-C1)
    t = np.arccos(np.dot(S-C1,Dir)/(np.linalg.norm(S-C1)*np.linalg.norm(Dir)))
    points = circle_3D(C1,eN1,r1,t,'R')
    if all(np.fabs(points - S) < 0.1):
        ths1 = t
    else:
        ths1 = 2*np.pi - t

    t = np.arccos( np.dot(S-C1,T1-C1) / (np.linalg.norm(S-C1)*np.linalg.norm(T1-C1)) )
    points = circle_3D(C1,eN1,r1,(t+ths1),'R')
    if all(np.fabs(points - T1) < 0.1):
        ang_arc1 = t
    else:
        ang_arc1 = 2*np.pi-t

    points = circle_3D(C2,eN2,r2,0,'R')
    Dir = (points-C2)/np.linalg.norm(points-C2)
    t = np.arccos(np.dot(E-C2,Dir)/(np.linalg.norm(E-C2)*np.linalg.norm(Dir)))
    points = circle_3D(C2,eN2,r2,t,'R')
    if all(np.fabs(points - E) < 0.1):
        thf2 = t
    else:
        thf2 = 2*np.pi - t

    t = np.arccos( np.dot(E-C2,T2-C2)/(np.linalg.norm(E-C2)*np.linalg.norm(T2-C2)) )
    points = circle_3D(C2,eN2,r2,(t-thf2),'R')
    if all(np.fabs(points - T2) < 0.1):
        ang_arc2 = t
    else:
        ang_arc2 = 2*np.pi - t

    arc1 = ang_arc1*r1
    arc2 = ang_arc2*r2
    return arc1,arc2,T1,T2,ang_arc1,ang_arc2