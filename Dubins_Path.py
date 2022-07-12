from RSL_Path import dubins_RSL
from LSR_Path import dubins_LSR
from RSR_Path import dubins_RSR
from LSL_Path import dubins_LSL
import numpy as np
from geometry import *

def main():
    ## ORIGIN
    O  = np.array([ 0, 0, 0])

    ## GATE'S VERTEX
    for i in range(4):
        if i == 0:
            p1 = np.array([22,15,+1])
            p2 = np.array([22,15,-1])
            p3 = np.array([26,15,-1])
            p4 = np.array([26,15,+1])
        elif i == 1:
            p1 = np.array([22,-15,+1])
            p2 = np.array([22,-15,-1])
            p3 = np.array([26,-15,-1])
            p4 = np.array([26,-15,+1])
        elif i == 2:
            p1 = np.array([22,-15,+5])
            p2 = np.array([22,-15,+4])
            p3 = np.array([26,-15,+4])
            p4 = np.array([26,-15,+5])
        elif i == 3:
            p1 = np.array([22,-15,-4])
            p2 = np.array([22,-15,-5])
            p3 = np.array([26,-15,-5])
            p4 = np.array([26,-15,-4])
        '''
        p1, p2, p3, p4 = vertex(dict_vertex)
        '''

        v1, v2, v3, v4 = points_vectors(p1, p2, p3, p4, O)

        # CENTER
        vC = center(v1, v3)

        ## GATE'S NORMAL
        vN  =  normal(vC, v1, v2, v4)

        ## INPUT POINTS
        [S, eS, eN1, E, eE, eN2] = input_dubins(O,vC,vN)
        r1 = 4
        r2 = 4

        ## OPTIMAL PATH
        counter = np.matrix((np.arange(44).reshape((4,11))), dtype=np.float32)
        for j in range(4):
            if j == 0:
                [arc1,arc2,T1,T2,ang1,ang2] = dubins_RSL(S,E,eS,eE,eN1,eN2,r1,r2)
                counter[j,0] = arc1
                counter[j,1] = arc2
                counter[j,[2,3,4]] = T1
                counter[j,[5,6,7]] = T2
                counter[j,8] = ang1
                counter[j,9] = ang2
                counter[j,10] = arc1 + arc2 + np.linalg.norm(T2-T1)
            elif j == 1:
                [arc1,arc2,T1,T2,ang1,ang2] = dubins_LSR(S,E,eS,eE,eN1,eN2,r1,r2)
                counter[j,0] = arc1
                counter[j,1] = arc2
                counter[j,[2,3,4]] = T1
                counter[j,[5,6,7]] = T2
                counter[j,8] = ang1
                counter[j,9] = ang2
                counter[j,10] = arc1 + arc2 + np.linalg.norm(T2-T1)
            elif j == 2:
                [arc1,arc2,T1,T2,ang1,ang2] = dubins_RSR(S,E,eS,eE,eN1,eN2,r1,r2)
                counter[j,0] = arc1
                counter[j,1] = arc2
                counter[j,[2,3,4]] = T1
                counter[j,[5,6,7]] = T2
                counter[j,8] = ang1
                counter[j,9] = ang2
                counter[j,10] = arc1 + arc2 + np.linalg.norm(T2-T1)
            elif j == 3:
                [arc1,arc2,T1,T2,ang1,ang2] = dubins_LSL(S,E,eS,eE,eN1,eN2,r1,r2)
                counter[j,0] = arc1
                counter[j,1] = arc2
                counter[j,[2,3,4]] = T1
                counter[j,[5,6,7]] = T2
                counter[j,8] = ang1
                counter[j,9] = ang2
                counter[j,10] = arc1 + arc2 + np.linalg.norm(T2-T1)
        ## VALUTAZIONE CASO MIGLIORE
        ind = np.argmin(counter[:,10],axis=0)
        val = counter[ind,10]
        MAXVEL = 20
        print('GATE NUMBER ',i)
        if ind == 0:
            print('Percorso breve: RSL')
            print('Lunghezza percorso: ',np.round(val,3) )
            print('Waypoint: ',S,np.round(counter[ind,[2,3,4]],3),np.round(counter[ind,[5,6,7]],3),E )
            print('velocità angolare arco iniziale attorno asse N1: ', np.round(MAXVEL/r1,3) )
            print('durata arco iniziale: ', np.round(counter[ind,0]/MAXVEL,3) )
            print('velocità lineare', np.round(MAXVEL,3) )
            print('durata tratto lineare', np.round(np.linalg.norm((counter[ind,[2,3,4]] - counter[ind,[5,6,7]]))/MAXVEL,3))
            print('velocità angolare arco finale attorno asse N2: ', np.round(MAXVEL/r2,3) )
            print('durata arco finale: ', np.round(counter[ind,1]/MAXVEL,3) )
        elif ind == 1:
            print('Percorso breve: LSR')
            print('Lunghezza percorso: ',np.round(val,3) )
            print('Waypoint: ',S,np.round(counter[ind,[2,3,4]],3),np.round(counter[ind,[5,6,7]],3),E )
            print('velocità angolare arco iniziale attorno asse N1: ', np.round(MAXVEL/r1,3) )
            print('durata arco iniziale: ', np.round(counter[ind,0]/MAXVEL,3) )
            print('velocità lineare', np.round(MAXVEL,3) )
            print('durata tratto lineare', np.round(np.linalg.norm((counter[ind,[2,3,4]] - counter[ind,[5,6,7]]))/MAXVEL,3))
            print('velocità angolare arco finale attorno asse N2: ', np.round(MAXVEL/r2,3) )
            print('durata arco finale: ', np.round(counter[ind,1]/MAXVEL,3) )
        elif ind == 2:
            print('Percorso breve: RSR')
            print('Lunghezza percorso: ',np.round(val,3) )
            print('Waypoint: ',S,np.round(counter[ind,[2,3,4]],3),np.round(counter[ind,[5,6,7]],3),E )
            print('velocità angolare arco iniziale attorno asse N1: ', np.round(MAXVEL/r1,3) )
            print('durata arco iniziale: ', np.round(counter[ind,0]/MAXVEL,3) )
            print('velocità lineare', np.round(MAXVEL,3) )
            print('durata tratto lineare', np.round(np.linalg.norm((counter[ind,[2,3,4]] - counter[ind,[5,6,7]]))/MAXVEL,3))
            print('velocità angolare arco finale attorno asse N2: ', np.round(MAXVEL/r2,3) )
            print('durata arco finale: ', np.round(counter[ind,1]/MAXVEL,3) )
        elif ind == 3:
            print('Percorso breve: LSL')
            print('Lunghezza percorso: ',np.round(val,3) )
            print('Waypoint: ',S,np.round(counter[ind,[2,3,4]],3),np.round(counter[ind,[5,6,7]],3),E )
            print('velocità angolare arco iniziale attorno asse N1: ', np.round(MAXVEL/r1,3) )
            print('durata arco iniziale: ', np.round(counter[ind,0]/MAXVEL,3) )
            print('velocità lineare', np.round(MAXVEL,3) )
            print('durata tratto lineare', np.round(np.linalg.norm((counter[ind,[2,3,4]] - counter[ind,[5,6,7]]))/MAXVEL,3))
            print('velocità angolare arco finale attorno asse N2: ', np.round(MAXVEL/r2,3) )
            print('durata arco finale: ', np.round(counter[ind,1]/MAXVEL,3) )
        print('----------------------------------------')
if __name__ == "__main__":
    main()