import numpy as np

def vertex(dict_vertex):
    # Punti da File
    p1 = np.array(dict_vertex[1])
    p2 = np.array(dict_vertex[2])
    p3 = np.array(dict_vertex[3])
    p4 = np.array(dict_vertex[4])
    return p1, p2, p3, p4

def points_vectors(p1, p2, p3, p4, O):
    v1 = p1 - O
    v2 = p2 - O
    v3 = p3 - O
    v4 = p4 - O
    return v1, v2, v3, v4

def center(v1, v3):
    ## CENTER GATE DEFINITION
    v13 = v3 - v1
    vC = v1 + (0.5 * np.linalg.norm(v13, 2) * (v13 / np.linalg.norm(v13, 2)))
    return vC

def normal(vC, v1, v2, v4):
    vC2 = v2 - vC
    vC1 = v1 - vC 
    v21 = v1 - v2
    v14 = v4 - v1
    vC5 = vC2 + ( 0.5*np.linalg.norm(v21,2) * (v21 / np.linalg.norm(v21,2) ) )
    vC6 = vC1 + ( 0.5*np.linalg.norm(v14,2) * (v14 / np.linalg.norm(v14,2) ) )
    vN  =  np.cross(vC5,vC6)/np.linalg.norm(np.cross(vC5,vC6)) + vC
    return vN

def input_dubins(O,vC,vN):
    ## STARTING DIRECTION ENDING DIRECTION DEFINITION
    S = O
    E = vC
    eS = np.array([1,0,0])
    eE = vN-vC
    ## NORMAL PLANES' VECTORS WHERE ARE DESCRIBED CIRCUMFERENCES
    eN1 = np.cross(eS,(S-E)/np.linalg.norm(S-E))/np.linalg.norm(np.cross(eS,(S-E)/np.linalg.norm(S-E)))
    if(eN1[2]<0):
        eN1 = -eN1
    
    eN2 = np.cross((E-S)/np.linalg.norm(E-S),eE)/np.linalg.norm(np.cross((E-S)/np.linalg.norm(E-S),eE))
    if(eN2[2]<0):
        eN2 = -eN2
    
    return S, eS, eN1, E, eE, eN2