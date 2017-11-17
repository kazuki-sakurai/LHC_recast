import sys

from math import *
from probavector import vector
from matrixclass import matrix


def Armenteros(p1,p2):
    p = p1 + p2
    pu = vunit(p)
    pl1 = vdot(p1,pu)
    pl2 = vdot(p2,pu)
    ap_alpha = (pl1-pl2)/(pl1+pl2)
    ap_pt = psqrt(vmod(p1)**2 - pl1**2)
    return ap_alpha, ap_pt

def ratio001(a,b):
    return abs(a -b)*(1./abs(a+b))

def IM2(p1,p2,m1,m2):
    """returns the Invariant Mass of two tracks with p1 and p2, for masses m1 m2"""
    t1=-1*vdot(p1,p2)
    pm1=vmod(p1)
    pm2=vmod(p2)
    t2=sqrt((m1*m1+pm1*pm1)*(m2*m2+pm2*pm2))
    masa2=m1*m1+m2*m2+2*(t1+t2)
    return masa2
def tIM2(p1,p2):
    """returns the invariant mass of the two tracks, suposing massless particles
    """
    ptot=vtmod(p1+p2)
    k=vtmod(p1)+vtmod(p2)
    tim2=k*k-ptot*ptot

    return tim2

def psqrt(thing):
    if thing < 0: return thing
    return sqrt(thing)

def closest_point(ori1,dir1,ori2,dir2):
    """ returns the closest point between these two tracks:
            one contains point 'ori1' and has vector 'dir1'
            one contains point 'ori2' and has vector 'dir2'

    """

    tol = 1.e-13;

    udir1 = vunit(dir1)
    udir2 = vunit(dir2)
  
    t1b = ori1;
    t2b = ori2;
    t1e = ori1 + udir1;
    t2e = ori2 + udir2;
  
    v0 = ori1 - ori2;
    v1 = udir1;
    v2 = udir2;
  
    d02 = vdot(v0,v2);
    d21 = vdot(v2,v1);
    d01 = vdot(v0,v1);
    d22 = vdot(v2,v2);
    d11 = vdot(v1,v1);
    
    denom = d11 * d22 - d21 * d21; 
    if (abs(denom) < tol): return None
    numer = d02 * d21 - d01 * d22;
    
    mu1 = numer / denom;
    mu2 = (d02 + d21 * mu1) / d22;
    
    close1 = t1b + mu1 * v1;  
    close2 = t2b + mu2 * v2;

    vertex = (close1 + close2)*0.5

    return vertex,close1,close2


def dpr(point,o,v):
    """dpr(point, point on track, track vector)
    Returns the distance between the 'point' and the straight line which passes
    over point 'o' and has vector director 'v'
    """
    d=point-o
    m=vcross(d,v)
    if vdot(m,m)==0: return 0
    m=vcross(m,v)
    

    sol =abs(vdot(m,d))/sqrt(vdot(m,m))
                                 
    return sol

def vdot(v1,v2):
    """ scalar product between 2 vectors
    """
    return v1[0]*v2[0]+v1[1]*v2[1]+v1[2]*v2[2]

def vcross(v1,v2):
    """ cross products between 2 3D vectors
    """
    v30 =   v1[1]*v2[2]-v1[2]*v2[1]
    v31 =   v1[2]*v2[0]-v1[0]*v2[2]
    v32 =   v1[0]*v2[1]-v1[1]*v2[0]

    v3 = vector(v30,v31,v32)

   ##  print " cross ",v1,v2," = ",v3
    return v3;

def vmod(v1):
    """ returns the modulo of the vector
    """
    mag = sqrt(vdot(v1,v1))
    return mag

def vtmod(v1):
    """ return the transverse module of the vector
    """
    mag = sqrt(v1[0]*v1[0]+v1[1]*v1[1])
    return mag

def vunit(v):
    """  makes unitary this vector
    """
    udir = v
    mod = vmod(v)
    if (mod != 0.): udir = v/vmod(v)
    return udir


def ACO(p1,p2):
    """the angle between p1 and p2
    """
    den=1.*vmod(p1)*vmod(p2)
#    if not(vmod(p1)): return pi/2
    if not(den): return 0.5*pi
    
    num=1.*vmod(vcross(p1,p2))
    seno = num/den
    coseno = vdot(p1,p2)/den
    ase = abs(seno)
    if ase>1: alpha = 0.5*pi
    else: alpha = asin(ase)
    
    if not coseno and seno < 0 : return 3*pi*0.5
    if not coseno: return 0.5*pi
    return int(coseno < 0)*pi + alpha*coseno/abs(coseno)
    #else: return alpha
    

def andreis_vars(p1,p2, rSV):
    p = rSV
    u1 = vunit(p)
    u2 = vunit(vcross(p1,p))
    u3 = vcross(u1,u2)

    p1w = vdot(p1,u2)
    p1q = vdot(p1,u3)
    p2w = vdot(p2,u2)
    p2q = vdot(p2,u3)

    p1_ = vector(p1w,p1q,0)
    p2_ = vector(p2w,p2q,0)

    pmiss = p1_ + p2_
    

    p1_ = vmod(p1_)
    p2_ = vmod(p2_)
    pmiss = vmod(pmiss)
    
    n = pmiss/( pmiss+p1_+p2_)
    m = p1_/(pmiss+p1_+p2_)

    return n, m
    

def mprod(matrix1,matrix2):

    out = []

    for i in range(matrix1.rows):
        row =[]
        fila = matrix1[i]
        for j in range(matrix2.columns):
            N = 0
            for k in range(matrix2.rows):
                N += fila[k]*matrix2[k][j]

            row.append(N)
        out.append(row)
    return matrix(out)

class Cono:
    def __init__(self,o1,p1,o2,p2,sinAngle,PV,IP = 0.1):
        hhh = closest_point(o1,p1,o2,p2)
        self.absSV = hhh[0]
        self.PV = PV
        self.SV = hhh[0] - PV
        self.alpha = sinAngle
        self.ipThres = IP
        self.o1 = o1
        self.o2 =o2
        self.p1 = vunit(p1)
        self.p2 = vunit(p2)
    def acceptTrack(self,x, p):
        ip = dpr(self.absSV,x,p)
        if ip > self.ipThres: return False
        ang = ACO(self.SV,p)
        if ang > self.alpha: return False
        xxx1 = x - self.o1
        xxx1 = vmod(xxx1)
        vvv1 = vunit(p) - self.p1
        vvv1 = vmod(vvv1)
        xxx2 = x - self.o2
        xxx2 = vmod(xxx2)
        vvv2 = vunit(p) - self.p2
        vvv2 = vmod(vvv2)

        d = min(xxx1 +vvv1, xxx2,vvv2)
        if d == 0 : return "MT"
        if d < 1.e-12: return "sMT"
        return True

def tpointing(v,vdi):
    u = vunit(vdi)
    vL = vdot(u,v)
    vm = vmod(v)
    return sqrt(vm*vm - vL*vL)


def gamma(beta):
    return 1./sqrt(1-beta**2)

def Ecm(lv1, lv2):
    ## 0 = E
    lv1 = [lv1.e(),lv1.x(),lv1.y(),lv1.z()]
    lv2 = [lv2.e(),lv2.x(),lv2.y(),lv2.z()]
    iE = 1./lv2[0]
    beta = vector(lv2[1]*iE,lv2[2]*iE,lv2[3]*iE)
    bt = vmod(beta)
    gm = gamma(bt)
    p = vector(lv1[1],lv1[2],lv1[3])
    v1 = vunit(beta)
    v2 = vector(beta[1], -beta[0], 0)
    v3 = vcross(v1,v2)
    v3 = vunit(v3)

    p1 = vdot(v1,p)
    p2 = vdot(v2,p)
    p3 = vdot(v3,p)

    gb = gm*bt
    p1b = -gb*lv1[0] + gm*p1
    p2b = p2
    p3b = p3
    eb = gm*lv1[0] - gb*p1

    return eb

def P_VV_angles(l1,l2,l3,l4):
    e1,p1 = l1[0], l1[1]
    e2,p2 = l2[0], l2[1]
    e3,p3 = l3[0], l3[1]
    e4,p4 = l4[0], l4[1]
                      
    pV1 = p1+p2
    pV2 = p3+p4
    eV1 = e1 + e2
    eV3 = e3 + e4
    iE = 1./eV1
    beta = iE*pV1
    bt = vmod(beta)
    g = gamma(bt)
    v1 = vunit(pV1)
    v2 = vector(beta[1], -beta[0], 0)
    v2 = vunit(v2)
    v3 = vcross(v1,v2)
    v3 = vunit(v3)
    gb = g*bt
    def project(l):
        e,p = l[0], l[1]
        p1 = vdot(v1,p)
        p2 = vdot(v2,p)
        p3 = vdot(v3,p)
       
        p1b = -gb*e + g*p1
        p2b = p2
        p3b = p3
        eb = g*e - gb*p1
        
        return [eb, vector(p1b,p2b,p3b)]
    l1 = project(l1)
    l2 = project(l2)
    l3 = project(l3)
    l4 = project(l4)
    
    p1,p2,p3,p4 = l1[1],l2[1],l3[1],l4[1]
    pV1 = p1 + p2
    pV2 = p3 + p4
    Th2 = ACO(p3,pV2)
    Th1 = ACO(p1,-pV2)
    PI1 = vcross(p1,pV2)
    PI2 = -1*vcross(p3,p4)
    Phi = ACO(PI1,PI2)

    if vdot(PI2,p1) < 0: Phi = -1*Phi
    
    return Th1, Th2, Phi
   

    
def ponderate(lx,lsx): ## TO CHECK
    if len(lx) != len(lsx):
        print "ERROR in 'ponderate', diferent lens"
        return lx[0], lsx[0]
    lwi = len(lx)*[0.]
    
    w = 0
    #w_inv = 1./w
    m = 0
    s = 0
    for i in range(len(lx)):
        sinv = 1./lsx[i]
        wi = sinv*sinv
        m+= lx[i]*wi
        w += wi
    winv = 1./w
    m = m*winv
    s = sqrt(winv)
    return m, s


def angleToflight(l1, l2):
    e1,p1 = l1[0], l1[1]
    e2,p2 = l2[0], l2[1]

    Bp = p1 + p2
    BE = e1 + e2

    iE = 1./BE
    beta = iE*Bp
    bt = vmod(beta)
    g = gamma(bt)
    v1 = vunit(Bp)
    v2 = vector(beta[1], -beta[0], 0)
    v2 = vunit(v2)
    v3 = vcross(v1,v2)
    v3 = vunit(v3)
    gb = g*bt

    px = vdot(v1,p1)
    py = vdot(v2,p1)
    pz = vdot(v3,p1)
    
    p1b = -gb*e1 + g*px
    p2b = py
    p3b = pz
    eb = g*e1 - gb*px
    
    p1p = vector(p1b,p2b,p3b)
    
    return ACO(vector(1,0,0),p1p)
        
def KSstat(data1,data2, st = None):
    steps = 0
    start = min(min(data1),min(data2))
    end = max(max(data1),max(data2))
    if not st: 
        steps = len(data1) + len(data2)
        
        st = (end - start)*1./100
    data1.sort()
    data2.sort()
    def cm(a,data):
        out = 0
        for y in data:
            if y >= a: break
            out += 1
        return out*1./len(data)
    D = 0.
    if not steps: steps = int((end-start)*1./st)
    for i in range(steps):
        x = start + st*i
        f1 = cm(x,data1)
        f2 = cm(x,data2)
        #if abs(f1-f2)>0.1 : print x, abs(f1-f2), f1, f2
        D = max(abs(f1-f2),D)
    n1 = len(data1)
    n2 = len(data2)
    return sqrt(n1*n2*1./(n1+n2))*D
        
def nonIndepErrors(a,N, sa = 0, sb = 0):
    Ni = 1./N
    b = N-a
    x = a*Ni
    if not (sa or sb):
        #print "Gaussian...."
        return x, Ni*Ni*sqrt(a*b*N)
    if not sb: sb = sqrt(b)
    if not sa: sa = sqrt(a)
    else:
        b = N-a
        return x, Ni*Ni* sqrt(b*b*sa*sa+a*a*sb*sb)


def poissonErrors(n):
    if n > 19:
        print "using gaussian, as n >=20"
        return sqrt(n), sqrt(n)
    
    some_poisson_p = {1: 2.3,
                      0: 1.8,
                      2: 2.6,
                      3: 2.9,
                      4: 3.1,
                      5: 3.4,
                      6: 3.6,
                      7: 3.8,
                      8: 3.9,
                      9: 13.1-9,
                      10:14.2-10,
                      11: 15.4-11,
                      12: 16.5-12,
                      13:4.7,
                      14:18.8-14,
                      15:19.9-15,
                      16:5.1,
                      17:5.2,
                      18:5.3,
                      19:5.4
                      }  #### 16%
    
    some_poisson_n = {1: 0.8,
                      0:0.,
                      2: 1.3,
                      3:1.6,
                      4: 1.9,
                      5: 2.2,
                      6: 2.4,
                      7: 2.6,
                      8: 2.8,
                      9:9-6.07,
                      10:10-6.91,
                      11:11-7.75,
                      12:12-8.6,
                      13:3.5,
                      14:14-10.32,
                      15:15-11.19,
                      16:3.9,
                      17:4.1,
                      18:4.2,
                      19:4.3
                      }  ##### 16%
    
    if n not in some_poisson_p.keys():
        print n , " not in list"
        return "wrong"
    return some_poisson_p[n], some_poisson_n[n]


def poissonErrors95(n):
    if n > 19:
        print "using gaussian, as n >=20"
        return 1.96*sqrt(n), 1.96*sqrt(n)
    
    some_poisson_p = {1: 5.57-1,
                      0: 3.69,
                      2: 7.22-2,
                      3: 8.77-3,
                      4: 10.24-4,
                      5: 11.67-5,
                      6: 13.1-6,
                      7: 14.4-7,
                      8: 15.8-8,
                      13:22.2-13,
                      16:10,
                      17:27.2-17,
                      18:10.45,
                      19:10.7
                      }  #### 16%
    
    some_poisson_n = {1: 1-0.253,
                      0:0.,
                      2: 2-0.24,
                      3:3-.6187,
                      4: 4-1.09,
                      5: 5-1.62,
                      6: 6-2.2,
                      7: 7-2.81,
                      8: 8-3.45,
                      13:13-6.92,
                      16:16-9.15,
                      17:17-9.9,
                      18:18-10.7,
                      19:19-11.4
                      }  ##### 16%
    
    if n not in some_poisson_p.keys():
        print n , " not in list"
        return "wrong"
    return some_poisson_p[n], some_poisson_n[n]

def poissonErrors50(n):
    if n > 19:
        print "using gaussian, as n >=20"
        return 0.6745*sqrt(n), 0.6745*sqrt(n)
    
    some_poisson_p = {1: 2.69-1,
                      0: 1.386,
                      2: 3.92-2,
                      3: 5.11-3,
                      4: 4.27-4,
                      5: 7.42-5,
                      6: 8.56-6,
                      7: 9.68-7,
                      8: 10.8-8,
                      13:16.3-13,
                      16:19.6-16,
                      17:20.7-17,
                      18:21.7-18,
                      19:22.8-19
                      }  #### 16%
    
    some_poisson_n = {1: 1-0.2877,
                      0:0.,
                      2: 2-0.9613,
                      3:3-1.73,
                      4: 4-2.53,
                      5: 5-3.37,
                      6: 6-4.22,
                      7: 7-5.08,
                      8: 8-5.96,
                      13:13-10.4,
                      16:16-13.2,
                      17:17-14.1,
                      18:18-15,
                      19:19-15.9
                      }  ##### 16%
    
    if n not in some_poisson_p.keys():
        print n , " not in list"
        return "wrong"
    return some_poisson_p[n], some_poisson_n[n]


def fuckingErrors(n):
    if n > 19:
        print "using gaussian, as n >=20"
        return sqrt(n), sqrt(n)
    
    some_poisson_p = {1: 1.58,
                      2: 1.91 ,
                      3: 2.20,
                      4: 2.47,
                      5: 2.67,
                      6: 2.90,
                      7: 3.06,
                      8: 3.29,
                      10:3.36,
                      13:4.01,
                      15: 4.38,
                      16:4.40,
                      17:4.43,
                      18:4.63,
                      19:4.67
                      }  #### 16%
    
    some_poisson_n = {1: 1.14,
                      2: 1.4,
                      3: 1.59,
                      4: 1.82,
                      5: 1.99,
                      6: 2.19,
                      7: 2.39,
                      8: 2.57,
                      10:3.02,
                      13: 3.30,
                      15: 3.48,
                      16: 3.66,
                      17: 3.78,
                      18: 3.89,
                      19: 4.05
                      }  ##### 16%
    
    if n not in some_poisson_p.keys():
        print n , " not in list"
        return "wrong"
    return some_poisson_p[n], some_poisson_n[n]



def fuckingErrorsB(n):
    if n > 19:
        print "using gaussian, as n >=20"
        return sqrt(n), sqrt(n)
    
    some_poisson_p = {1: 1.2985505262165684, 2: 1.6745245491587737, 3: 1.9372930591879378, 4: 2.1972999828792221, 5: 2.4268662075839673, 6: 2.6172957195407842, 7: 2.8223052707294807, 8: 3.0140541128641742, 9: 3.1446901383203345, 10: 3.326508638050349, 11: 3.4592536076426357, 12: 3.611599233464847, 13: 3.7546642717788687, 14: 3.8739574660165252, 15: 4.0342309666466134, 16: 4.1485487938204262, 17: 4.2611823567902114, 18: 4.3842090833588339, 19: 4.5037770770053722}
    some_poisson_n = {1: 1.0450122825008918, 2: 1.4221304040623721, 3: 1.6672436567392452, 4: 1.9117706083399071, 5: 2.1436130271824965, 6: 2.3334463475863885, 7: 2.531188610888691, 8: 2.7220285995078228, 9: 2.8689822007709722, 10: 3.0404491932724227, 11: 3.1770837928040834, 12: 3.3305711719978888, 13: 3.4724209677833073, 14: 3.6040794677557528, 15: 3.7602649864067814, 16: 3.8717803185396491, 17: 3.9872593004360795, 18: 4.1204046537674799, 19: 4.2215175215639533}
    
    if n not in some_poisson_p.keys():
        print n , " not in list"
        return "wrong"
    return some_poisson_p[n], some_poisson_n[n]


## def weightedAverage(lx,lsx):
##     w = len(lsx)*[0.]
##     for i in range(len(lsx)):# in lsx:
##         s = lsx[i]
##         w[i] = 1./(s*s)
    
##     W = sum(w)
##     for i in range(len(lsx)):
##         w[i] = w[i]/W
##     x,sx = 0, 0
##     for i in range(len(lx)):
##         x+=w[i]*lx[i]
##         sx+= (w[i]**2) *( lsx[i]**2)
##     sx = sqrt(sx)
##     return x, sx
    
    
    
def median(x):
    N = len(x)
    x.sort()
    mi = int(round(0.5*N))
    if N%2: m = x[mi-1]
    else:
        #print mi
        m = (x[mi]+x[mi-1])*0.5
    s1i = int(round(0.16*N))
    s2i = int(round(0.84*N))

    return m, x[s1i-1], x[s2i-1]


def buggy_angle(l1, l2):
    e1,p1 = l1[0], l1[1]
    e2,p2 = l2[0], l2[1]

    Bp = p1 + p2
    BE = e1 + e2

    iE = 1./BE
    beta = iE*Bp
    bt = vmod(beta)
    g = gamma(bt)
    v1 = vunit(Bp)
    v2 = vector(beta[1], -beta[0], 0)
    v2 = vunit(v2)
    v3 = vcross(v1,v2)
    v3 = vunit(v3)
    gb = g*bt

    px = vdot(v1,p1)
    py = vdot(v2,p1)
    pz = vdot(v3,p1)
    
    p1b = -gb*e1 + g*px
    p2b = py
    p3b = pz
    eb = g*e1 - gb*px
    
    p1p = vector(p1b,p2b,p3b)
    
    return ACO(Bp,p1p)


    
def JpsiKst_Angles(kaon,pion, mu1, mu2):
    """
    paula
    """
    P11p = kaon[1]
    P12p = pion[1]
    P21p = mu1[1]
    P22p = mu2[1]
    from ROOT import TLorentzVector, TVector3
    def NProductV(alpha, Vect):
        Vect1 = [Vect.x(),Vect.y(),Vect.z()]    
        for i in range(0,3):
            Vect1[i] = alpha*Vect[i]
        return TVector3(Vect1[0],Vect1[1],Vect1[2])
    
    p1 = TLorentzVector(P11p[0],P11p[1],P11p[2],kaon[0])
    p2 = TLorentzVector(P12p[0],P12p[1],P12p[2],pion[0])
    p3 = TLorentzVector(P21p[0],P21p[1],P21p[2],mu1[0])
    p4 = TLorentzVector(P22p[0],P22p[1],P22p[2],mu2[0])
    p1Psi = TLorentzVector(p1)
    
    p12 = TLorentzVector(p1+p2)
    p34 = TLorentzVector(p3+p4)
    BK0S = TLorentzVector(p1+p2+p3+p4)
    BPsi = TLorentzVector(p1+p2+p3+p4)

    p1.Boost(NProductV(-1./(p12.E()),p12.Vect()))
    BK0S.Boost(NProductV(-1./(p12.E()),p12.Vect()))

    ThK = (p1.Vect()).Angle(-BK0S.Vect())

    p1Psi.Boost(NProductV(-1./(p34.E()),p34.Vect()))
    BPsi.Boost(NProductV(-1./(p34.E()),p34.Vect()))


    xtr = BPsi.Vect().Unit()
    ytr = (p1Psi.Vect().Unit()- NProductV((p1Psi.Vect().Unit()).Dot(xtr),xtr)).Unit()
    ztr = xtr.Cross(ytr)

    p3.Boost(NProductV(-1./(p34.E()),p34.Vect()))
    Thtr = ztr.Angle(p3.Vect())
    Phitr = xtr.Angle(p3.Vect()-NProductV(ztr.Dot(p3.Vect()),ztr))
    if (ytr.Angle(p3.Vect()-NProductV(ztr.Dot(p3.Vect()),ztr))>pi/2.): Phitr = -Phitr

    return ThK, Thtr, Phitr
#==========================================================================================================================

def HelicityAngles(Kplus_P, Kminus_P, muplus_P, muminus_P ):
    """ Vasilis
    """
    from ROOT import TMath
    # Calculation based on the ANA-2012-067-v3

    # Bs, KK, mm momenta 4 vectors
    KK_P   = Kplus_P + Kminus_P;
    mm_P   = muplus_P + muminus_P;
    KKmm_P = KK_P + mm_P;

    # Unit vector along mumu direction in the KK mass r.f.
    muplus_P.Boost( - KK_P.BoostVector() );
    muminus_P.Boost( - KK_P.BoostVector() );
    e_KK = - (muplus_P + muminus_P).Vect().Unit();

    # Boost the muons back to lab frame
    muplus_P.Boost( KK_P.BoostVector() );
    muminus_P.Boost( KK_P.BoostVector() );

    # Unit vector along KK direction in the mm mass r.f.
    Kplus_P.Boost( - mm_P.BoostVector() );
    Kminus_P.Boost( - mm_P.BoostVector() );
    e_mm = - (Kplus_P+Kminus_P).Vect().Unit();
    # Boost the Kaons back to lab frame
    Kplus_P.Boost( mm_P.BoostVector() );
    Kminus_P.Boost( mm_P.BoostVector() );

    # Unit vector along KK direction in the mm mass r.f.
    Kplus_P.Boost( - KKmm_P.BoostVector() );
    Kminus_P.Boost( - KKmm_P.BoostVector() );
    muplus_P.Boost( - KKmm_P.BoostVector() );
    muminus_P.Boost( - KKmm_P.BoostVector() );
    e_KKmm = (muplus_P + muminus_P).Vect().Unit();

    # Perpenticular vectors to KK and mm planes in the KKmmm r.f.
    eta_KK = ( Kplus_P.Vect().Cross( Kminus_P.Vect()) ).Unit();
    eta_mm = ( muplus_P.Vect().Cross( muminus_P.Vect()) ).Unit();

    Kplus_P.Boost( KKmm_P.BoostVector() );
    Kminus_P.Boost( KKmm_P.BoostVector() );
    muplus_P.Boost( KKmm_P.BoostVector() );
    muminus_P.Boost( KKmm_P.BoostVector() );

    # Helicity angles.
    Kplus_P.Boost( - KK_P.BoostVector() );
    muplus_P.Boost( - mm_P.BoostVector() );

    angles = 3*[0.]
    angles[0] = ( Kplus_P.Vect().Unit()  ).Dot(e_KK);
    angles[1] = ( muplus_P.Vect().Unit() ).Dot(e_mm);

    if eta_KK.Cross(eta_mm).Dot(e_KKmm) > 0  :        # sinphi = eta_KK.Cross(eta_mm).Dot(e_KKmm);
        angles[2] = + TMath.ACos( eta_KK.Dot(eta_mm) )   # cosphi = eta_KK.Dot(eta_mm);
    else :
        angles[2] = - TMath.ACos( eta_KK.Dot(eta_mm) )

    return angles
def TranslateHelicity(Hp, Hz, Hm, pHp, pHz, pHm):
    _Hp = complex(Hp *cos(pHp), Hp*sin(pHp))
    _Hm = complex(Hm *cos(pHm), Hm*sin(pHm))
    _Hz = complex(Hz *cos(pHz), Hz*sin(pHz))
## ## Define pHz 0.0

    _a1 = 1./sqrt(2) *(_Hp + _Hm)
    _a2 = 1./sqrt(2) *(_Hp - _Hm)
    suma =  Hp**2 + Hz**2 + Hm**2
    Apa2 = (_a1*_a1.conjugate()).real/suma
    Ape2 = (_a2*_a2.conjugate()).real/suma #0.1601
    A02 = 1.-Apa2-Ape2
    d0 = atan(_Hz.imag/_Hz.real)
    if _Hz.real < 0: d0 = d0 + pi
    
    dpa = atan(_a1.imag/_a1.real)
    if _a1.real < 0: dpa = dpa + pi
    
    dpe = atan(_a2.imag/_a2.real)
    if _a2.real < 0: dpe = dpe + pi
   # print "d0"
    return A02, Apa2, dpa-d0, dpe-d0
