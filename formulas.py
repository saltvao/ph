from math import *


# https://bez-smenki.ru/material/formuly-mehanika/


class Kinematics():
    def __init__(self):
        pass

    class angularVel:
        variables = ["angleVelocity", "radius", "usualVelocity"]

        def angularVel(self, W=0, R=0, V=0):
            if V == "f":
                v = W * R
                return v
            elif W == "f":
                w = V / R
                return w
            elif R == "f":
                r = V / W
                return r

    class usualVel:
        variables = ["distance", "time", "usualVelocity"]

        def usualVel(self, S=0, T=0, V=0):
            if V == "f":
                v = S / T
                return v
            elif S == "f":
                s = V * T
                return s
            elif T == "f":
                t = S / V
                return t

    class accelerationVel:
        variables = ["zeroVelocity", "time", "acceleration", "accelerationVelocity"]

        def accelerationVel(self, V0=0, A=0, T=0, V=0):
            if V == "f":
                v = V0 + A * T
                return v
            elif A == "f":
                a = (V - V0) / T
                return a
            elif T == "f":
                t = (V - V0) / A
                return t
            elif V0 == "f":
                v0 = V - (A * T)
                return v0

    class newtonSecondRule:
        variables = ["acceleration", "mass", "force"]

        def newtonSecondRule(self, A=0, M=0, F=0):
            if F == "f":
                f = A * M
                return f
            elif A == "f":
                a = F / M
                return a
            elif M == "f":
                m = F / A
                return m

    pass

    class accelerationDist:
        variables = ["zeroVelocity", "time", "acceleration", "distance"]

        def accelerationDist(self, V0=0, A=0, T=0, S=0):
            if S == "f":
                s = (V0 * T) + ((A * T * T) / 2)
                return s
            elif A == "f":
                a = 2 * ((S - (V0 * T)) / T * T)
                return a
            elif T == "f":
                D = (4*V0*V0) - (4 * A * (-2*S))
                arr = []
                t1 = ((-2*V0) + (sqrt(D)))/(2*A)
                t2 = ((-2*V0) - (sqrt(D)))/(2*A)
                arr.append(t1)
                arr.append(t2)
                for i in arr:
                    if i < 0:
                        arr.remove(i)
                return arr[0]
            elif V0 == "f":
                v0 = (S - ((A * T * T) / 2)) / T
                return v0

    pass


class circleMotion():  # движ окружности
    # fi = s/r
    class anglDeg:
        variables = ["angle", "radius", "distance"]

        def anglDeg(self, Fi=0, R=0, S=0):
            if Fi == "f":
                fi = S / R
                return fi
            elif S == "f":
                s = Fi * R
                return s
            elif R == "f":
                r = S / Fi
                return r

    class FreqPer:  # nu = 1/T
        variables = ["frequency", "period"]

        def FreqPer(self, Nu=0, T=0):
            if Nu == "f":
                nu = 1.0 / T
                return nu
            elif T == "f":
                t = 1.0 / Nu
                return t

    # v = 2pir/t
    class velPer:
        variables = ["usualVelocity", "pi", "period", "radius"]

        def velPer(self, V=0, R=0, T=0, Pi=3.14):
            if V == "f":
                v = (2 * Pi * R) / T
                return v
            elif T == "f":
                t = (2 * Pi * R) / V
                return t
            elif R == "f":
                r = (V * T) / (2 * pi)
                return r

    class velFreq:
        variables = ["usualVelocity", "pi", "frequency", "radius"]

        def velFreq(self, V=0, R=0, Nu=0, Pi=3.14):
            if V == "f":
                v = 2 * Pi * R * Nu
                return v
            elif Nu == "f":
                nu = V / (2 * Pi * R)
                return nu
            elif R == "f":
                r = V / (2 * pi * Nu)
                return r

    class velPerAngl:  # w = fi/t
        variables = ["angle", "angleVelocity", "time", ]

        def velPerAngl(self, W=0, Fi=0, T=0):
            if W == "f":
                w = Fi / T
                return w
            elif T == "f":
                t = Fi / W
                return t
            elif Fi == "f":
                fi = W / T
                return fi

    class velPiPer:  # w = 2pi/T
        variables = ["angleVelocity", "pi", "period", ]

        def velPiPer(self, W=0, Pi=3.14, T=0):
            if W == "f":
                w = (2 * Pi) / T
                return w
            elif T == "f":
                t = (2 * Pi) / W
                return t

    class velPiNu:  # w = 2pi*nu
        variables = ["angleVelocity", "pi", "frequency", ]

        def velPiNu(self, W=0, Pi=3.14, Nu=0):
            if W == "f":
                w = 2 * Pi * Nu
                return w
            elif Nu == "f":
                nu = W / (2 * Pi)
                return nu

    class velAngRad:  # v = wr
        variables = ["usualVelocity", "angleVelocity", "radius", ]

        def velAngRad(self, W=0, V=0, R=0):
            if W == "f":
                w = V / R
                return w
            elif V == "f":
                v = W * R
                return v
            elif R == "f":
                r = V / W
                return r

    class acellAngleVel:  # a = w^2r
        variables = ["acceleration", "angleVelocity", "radius", ]

        def acellAngleVel(self, W=0, A=0, R=0):
            if W == "f":
                w = sqrt(A / R)
                return w
            elif A == "f":
                a = W * W * R
                return a
            elif R == "f":
                r = A / W * W
                return r


class Dynamics():  # динамика
    class FricForce:
        variables = ["dynForce", "uFriction", "ForceN"]

        def FricForce(self, F=0, U=0, N=0):
            if F == "f":
                f = U * N
                return f
            elif U == "f":
                u = F / N
                return u
            elif N == "f":
                n = F / U
                return n

    class elasticForce:
        variables = ["dynForce", "coeff", "deltaX"]

        def elasticForce(self, F=0, K=0, X=0):
            if F == "f":
                f = (-1) * K * X
                return f
            elif K == "f":
                k = F / X
                return k
            elif X == "f":
                x = F / K
                return x

    class GravityForce:
        variables = ["dynForce", "acceleration", "mass"]

        def GravityForce(self, F=0, G=10, M=0):
            if F == "f":
                f = M * G
                return f
            elif M == "f":
                m = F / G
                return m

    

    class pulse:
        variables = ["pulse", "usualVelocity", "mass"]

        def pulse(self, P=0, M=0, V=0):
            if P == "f":
                p = M * V
                return p
            elif V == "f":
                v = P / M
                return v
            elif M == "f":
                m = P / V
                return m


class Static():
    class momentForce:
        variables = ["dynForce", "moment", "distance"]

        def momentForce(self, F=0, M=0, D=0):
            if M == "f":
                m = F * D
                return m
            elif F == "f":
                f = M / D
                return f
            elif D == "f":
                d = M / F
                return d

    class density:
        variables = ["density", "mass", "volume"]

        def density(self, P=0, M=0, V=0):
            if P == "f":
                p = M / V
                return p
            elif M == "f":
                m = P * V
                return m
            elif V == "f":
                v = M / P
                return v

    class pressure:
        variables = ["pressure", "statForce", "square"]

        def pressure(self, P=0, F=0, S=0):
            if P == "f":
                p = F / S
                return p
            elif F == "f":
                f = P * S
                return f
            elif S == "f":
                s = F / P
                return s

    class waterPressure:
        variables = ["pressure", "height", "densityLiquid", "acceleration"]

        # P =
        def waterPressure(self, P=0, D=0, H=0, G=10):
            if P == "f":
                p = D * G * H
                return p
            elif D == "f":
                d = P / (G * H)
                return d
            elif H == "f":
                h = P / (D * G)
                return h

    class pressureForce:
        variables = ["statForce", "densityLiquid", "height", "acceleration", "square"]

        def pressureForce(self, F=0, D=0, H=0, S=0, G=10):
            if F == "f":
                f = D * G * H * S
                return f
            elif D == "f":
                d = F / (G * H * S)
                return d
            elif H == "f":
                h = F / (D * G * S)
                return h
            elif S == "f":
                s = F / (D * G * H)
                return s

    class archForce:
        variables = ["statForce", "densityLiquid", "volume", "acceleration"]

        def archForce(self, F=0, D=0, V=0, G=10):
            if F == "f":
                f = D * G * V
                return f
            elif D == "f":
                d = F / (G * V)
                return d
            elif V == "f":
                v = F / (D * G)
                return v


class Energy():
    class work:
        variables = ["energyForce", "work", "distance"]

        # F = A/S
        def work(self, F=0, A=0, S=0):
            if F == "f":
                f = A / S
                return f
            elif A == "f":
                a = F * S
                return a
            elif S == "f":
                s = A / F
                return s

    class gravityWork:
        variables = ["mass", "height", "acceleration", "work"]

        # a = mgh
        def gravityWork(self, M=0, H=0, A=0, G=10):
            if A == "f":
                a = M * G * H
                return a
            elif M == "f":
                m = A / (G * H)
                return m
            elif H == "f":
                h = A / (M * H)
                return h

    class elasticWork:
        variables = ["work", "distance", "coeff"]

        def elasticWork(self, A=0, X=0, K=0):
            if A == "f":
                a = K * X * X / 2
                return a
            elif X == "f":
                x = sqrt(A * 2 / K)
                return x
            elif K == "f":
                k = 2 * A / (X * X)
                return K

    class power:  # N = a/t
        variables = ["power", "work", "time"]

        def power(self, P=0, A=0, T=0):
            if P == "f":
                p = A / T
                return p
            elif A == "f":
                a = P * T
                return a
            elif T == "f":
                t = A / P
                return t

    class powerForce:  # N = FV
        variables = ["power", "energyForce", "velocity"]

        def powerForce(self, P=0, F=0, V=0):
            if P == "f":
                p = F * V
                return p
            elif F == "f":
                f = P / V
                return f
            elif V == "f":
                v = P / F
                return v

    class eKin:  # Ek = Mv2/2
        variables = ["kineticEnergy", "mass", "usualVelocity"]

        def eKin(self, E=0, M=0, V=0):
            if E == "f":
                e = (M * V * V) / 2
                return e
            elif M == "f":
                m = (2 * E) / (V * V)
                return m
            elif V == "f":
                v = sqrt(2 * E / M)
                return v

    class ePot:  # Ep = MGH
        variables = ["potentialEnergy", "mass", "distance", "acceleration"]

        def ePot(self, E=0, M=0, H=0, G=10):
            if E == "f":
                e = M * G * H
                return e
            elif M == "f":
                m = E / (G * H)
                return m
            elif H == "f":
                h = E / (M * G)
                return h

    class fullEnergy:
        variables = ["potentialEnergy", "kineticEnergy", "fullEnergy"]

        def fullEnergy(self, K=0, P=0, F=0):
            if F == "f":
                f = K + P
                return f
            elif K == "f":
                k = F - P
                return k
            elif P == "f":
                p = F - K
                return p

    class heat:
        variables = ["heat", "deltaTemp ", "сHeat", "mass"]

        def heat(self, Q=0, DT=0, C=0, M=0):
            if Q == "f":
                q = C * M * DT
                return q
            elif C == "f":
                c = Q / (M * DT)
                return c
            elif M == "f":
                m = Q / (C * DT)
                return m
            elif DT == "f":
                t = Q(C * M)
                return t

    class heatBurn:
        variables = ["heat", "qHeat", "mass"]

        def heatBurn(self, Q=0, QH=0, M=0):
            if Q == "f":
                q = QH * M
                return q
            elif QH == "f":
                qh = Q / M
                return qh
            elif M == "f":
                m = Q / QH
                return m


class Fluct():  # колебания

    class wobbleMass:  # w = sqrt K/m
        variables = ["mass", "angleVelocity", "coeff"]

        def wobbleMass(self, W=0, K=0, M=0):
            if W == "f":
                w = sqrt(K / M)
                return w
            elif M == "f":
                m = K / (W * W)
                return m
            elif K == "f":
                k = W * W * M
                return k

    class wobbleLenght:  # w = sqrt g/l
        variables = ["acceleration", "angleVelocity", "distance"]

        def wobbleLenght(self, W=0, G=0, L=0):
            if W == "f":
                w = sqrt(G / L)
                return w
            elif L == "f":
                l = G / (W * W)
                return l
            elif G == "f":
                g = W * W * L
                return g


#  без газов, без электричества
