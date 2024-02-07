from math import *
import operator as op
from formulas import *
import sys
import UI

valuesArr = {}
# lisy of keys from dictionary
desired = ""

kin = Kinematics()
cirMot = circleMotion()
din = Dynamics()
stat = Static()
enrg = Energy()
osc = Fluct()

usualVelocity = kin.usualVel()
angularVel = kin.angularVel()
accelerationVel = kin.accelerationVel()
newtonSecondRule = kin.newtonSecondRule()
accelerationDist = kin.accelerationDist()

anglDeg = cirMot.anglDeg()
FreqPer = cirMot.FreqPer()
velPer = cirMot.velPer()
velFreq = cirMot.velFreq()
velPerAngl = cirMot.velPerAngl()
velPiPer = cirMot.velPiPer()
velPiNu = cirMot.velPiNu()
velAngRad = cirMot.velAngRad()
acellAngleVel = cirMot.acellAngleVel()


FricForce = din.FricForce()
elasticForce = din.elasticForce()
GravityForce = din.GravityForce()
pulse = din.pulse()

momentForce = stat.momentForce()
density = stat.density()
pressure = stat.pressure()
waterPressure = stat.waterPressure()
pressureForce = stat.pressureForce()
archForce = stat.archForce()

work = enrg.work()
gravityWork = enrg.gravityWork()
elasticWork = enrg.elasticWork()
power = enrg.power()
powerForce = enrg.powerForce()
eKin = enrg.eKin()
ePot = enrg.ePot()
fullEnergy = enrg.fullEnergy()
heat = enrg.heat()
heatBurn = enrg.heatBurn()

wobbleMass = osc.wobbleMass()
wobbleLenght = osc.wobbleLenght()


var = {1: kin.angularVel.variables,
       2: kin.usualVel.variables,
       3: kin.accelerationVel.variables,
       4: kin.newtonSecondRule.variables,
       5: kin.accelerationDist.variables,
       6: cirMot.anglDeg.variables,
       7: cirMot.FreqPer.variables,
       8: cirMot.velPer.variables,
       9: cirMot.velFreq.variables,
       10: cirMot.velPerAngl.variables,
       11: cirMot.velPiPer.variables,
       12: cirMot.velPiNu.variables,
       13: cirMot.velAngRad.variables,
       14: cirMot.acellAngleVel.variables,
       15: din.FricForce.variables,
       16: din.elasticForce.variables,
       17: din.GravityForce.variables,
       18: din.pulse.variables,
       19: stat.momentForce.variables,
       20: stat.density.variables,
       21: stat.pressure.variables,
       22: stat.waterPressure.variables,
       23: stat.pressureForce.variables,
       24: stat.archForce.variables,
       25: enrg.work.variables,
       26: enrg.gravityWork.variables,
       27: enrg.elasticWork.variables,
       28: enrg.power.variables,
       29: enrg.powerForce.variables,
       30: enrg.eKin.variables,
       31: enrg.ePot.variables,
       32: enrg.fullEnergy.variables,
       33: enrg.heat.variables,
       34: enrg.heatBurn.variables,
       35: osc.wobbleMass.variables,
       36: osc.wobbleLenght.variables
       }


# _________________________________________________________________________________________________#
# temporary value input


def inputValues():
    f = 10
    while f != 11223344:
        i = input("Write value and quantity: ")
        a = input("Write value and quantity: ")
        valuesArr[a] = i

        f = float(i)
        pass


def clearValueArr(valuesArr):
    temporaryArr = []
    for i in valuesArr:
        temporaryArr.append(i)
        pass
    for key in temporaryArr:
        if valuesArr[key] == "11223344":
            del valuesArr[i]
            pass
    pass
    pass

# ______________________________________________________________________________________________________#
# str to float convertion


def is_number(str):
    try:
        float(str)
        return True
    except ValueError:
        return False

# turns str into float


def finalInput():
    inputValues()
    clearValueArr(valuesArr)
    for i in valuesArr:
        if is_number(valuesArr[i]):
            valuesArr[i] = float(valuesArr[i])

#defines missing quantity(among input ones)
def missingQuantity(valueNames, methodVar):
    # ---------------------------
    temporaryArr = []
    for i in methodVar:
        temporaryArr.append(i)
        pass
    # ---------------------------
    for i in valueNames:
        for j in methodVar:
            if i == j:
                temporaryArr.remove(i)

    return temporaryArr


# quantity comparison (percentage)
def quantityComparison(valueNames, variables):
    temporaryArr = []
    for i in valueNames:
        temporaryArr.append(i)

    converged = 0

    for i in valueNames:
        for j in variables:
            if i == j:
                converged += 1
            pass
    comparisonPercentage = (converged/len(valueNames)) * 100
    return comparisonPercentage

#useles part(idk)
def quantityComparisonArr(valueNames, variables):
    temporaryArr = []
    for i in valueNames:
        temporaryArr.append(i)

    converged = 0

    for i in valueNames:
        for j in variables:
            if i == j:
                converged += 1
            pass
    return temporaryArr

#finding max arr similarity percentage(among all possible variants)!!!!!
#BUT returnes the percentage array
def definingBestfunc(valueNames, desi, variables):
    temporaryArr = {}
    for i in var:
        a = quantityComparison(valueNames, var.get(i))
        temporaryArr[i] = a
        pass
    maxPercantage = max(temporaryArr.items(), key=op.itemgetter(1))
    return temporaryArr




def matchMethod(method, array):
    result = 0
    match method:
        case 1:
            result = angularVel.angularVel(
                W=array[kin.angularVel.variables[0]], R=array[kin.angularVel.variables[1]], V=array[kin.angularVel.variables[2]])
        case 2:
            result = usualVelocity.usualVel(
                S=array[kin.usualVel.variables[0]], T=array[kin.usualVel.variables[1]], V=array[kin.usualVel.variables[2]])
        case 3:
            result = accelerationVel.accelerationVel(V0=array[kin.accelerationVel.variables[0]], T=array[kin.accelerationVel.variables[1]],
                                                     A=array[kin.accelerationVel.	variables[2]], V=array[kin.accelerationVel.variables[3]])
        case 4:
            result = newtonSecondRule.newtonSecondRule(A=array[kin.newtonSecondRule.variables[0]], M=array[kin.newtonSecondRule.variables[1]], F=array[kin.newtonSecondRule.variables[2]])
        case 5:
            result = accelerationDist.accelerationDist(V0=array[kin.accelerationDist.variables[0]], T=array[kin.accelerationDist.variables[1]],
                                                       A=array[kin.accelerationDist.	variables[2]], S=array[kin.accelerationDist.variables[3]])
        case 6:
            result = anglDeg.anglDeg(Fi=array[cirMot.anglDeg.variables[0]],
                                     R=array[cirMot.anglDeg.variables[1]], S=array[cirMot.anglDeg.variables[2]])
        case 7:
            result = FreqPer.FreqPer(
                Nu=array[cirMot.FreqPer.variables[0]], T=array[cirMot.FreqPer.variables[1]])
        case 8:
            result = velPer.velPer(V=array[cirMot.velPer.variables[0]], Pi=array[cirMot.velPer.variables[1]],
                                   T=array[cirMot.velPer.variables[2]], R=array[cirMot.velPer.variables[3]])
        case 9:
            result = velFreq.velFreq(V=array[cirMot.velFreq.variables[0]], Pi=array[cirMot.velFreq.variables[1]],
                                     Nu=array[cirMot.velFreq.variables[2]], R=array[cirMot.velFreq.variables[3]])
        case 10:
            result = velPerAngl.velPerAngl(
                W=array[cirMot.velPerAngl.variables[1]], Fi=array[cirMot.velPerAngl.variables[0]], T=array[cirMot.velPerAngl.variables[2]])
        case 11:
            result = velPiPer.velPiPer(W=array[cirMot.velPiPer.variables[0]],
                                       Pi=array[cirMot.velPiPer.variables[1]], T=array[cirMot.velPiPer.variables[2]])
        case 12:
            result = velPiNu.velPiNu(W=array[cirMot.velPiNu.variables[0]],
                                     Pi=array[cirMot.velPiNu.variables[1]], Nu=array[cirMot.velPiNu.variables[2]])
        case 13:
            result = velAngRad.velAngRad(
                W=array[cirMot.velAngRad.variables[1]], V=array[cirMot.velAngRad.variables[0]], R=array[cirMot.velAngRad.variables[2]])
        case 14:
            result = acellAngleVel.acellAngleVel(
                W=array[cirMot.acellAngleVel.variables[1]], A=array[cirMot.acellAngleVel.variables[0]], R=array[cirMot.acellAngleVel.variables[2]])
        case 15:
            result = FricForce.FricForce(F=array[din.FricForce.variables[0]],
                                         U=array[din.FricForce.variables[1]], N=array[din.FricForce.variables[2]])
        case 16:
            result = elasticForce.elasticForce(
                F=array[din.elasticForce.variables[0]], K=array[din.elasticForce.variables[1]], X=array[din.elasticForce.variables[2]])
        case 17:
            result = GravityForce.GravityForce(
                F=array[din.GravityForce.variables[0]], G=array[din.GravityForce.variables[1]], M=array[din.GravityForce.variables[2]])
        case 18:
            result = pulse.pulse(
                P=array[din.pulse.variables[0]], V=array[din.pulse.variables[1]], M=array[din.pulse.variables[2]])
        case 19:
            result = momentForce.momentForce(
                F=array[stat.momentForce.variables[0]], M=array[stat.momentForce.variables[1]], D=array[stat.momentForce.variables[2]])
        case 20:
            result = density.density(
                P=array[stat.density.variables[0]], M=array[stat.density.variables[1]], V=array[stat.density.variables[2]])
        case 21:
            result = pressure.pressure(
                P=array[stat.pressure.variables[0]], F=array[stat.pressure.variables[1]], S=array[stat.pressure.variables[2]])
        case 22:
            result = waterPressure.waterPressure(P=array[stat.waterPressure.variables[0]], H=array[stat.waterPressure.variables[1]],
                                                 D=array[stat.waterPressure.variables[2]], G=array[stat.waterPressure.variables[3]])
        case 23:
            result = pressureForce.pressureForce(F=array[stat.pressureForce.variables[0]], D=array[stat.pressureForce.variables[1]],
                                                 H=array[stat.pressureForce.variables[2]], G=array[stat.pressureForce.variables[3]], S=array[stat.pressureForce.variables[4]])
        case 24:
            result = archForce.archForce(F=array[stat.archForce.variables[0]], D=array[stat.archForce.variables[1]],
                                         V=array[stat.archForce.variables[2]], G=array[stat.archForce.variables[3]])
        case 25:
            result = work.work(F=array[enrg.work.variables[0]],
                               A=array[enrg.work.variables[1]], S=array[enrg.work.variables[2]])
        case 26:
            result = gravityWork.gravityWork(M=array[enrg.gravityWork.variables[0]], H=array[enrg.gravityWork.variables[1]],
                                             G=array[enrg.gravityWork.variables[2]], A=array[enrg.gravityWork.variables[3]])
        case 27:
            result = elasticWork.elasticWork(
                A=array[enrg.elasticWork.variables[0]], X=array[enrg.elasticWork.variables[1]], K=array[enrg.elasticWork.variables[2]])
        case 28:
            result = power.power(N=array[enrg.power.variables[0]],
                                 A=array[enrg.power.variables[1]], T=array[enrg.power.variables[2]])
        case 29:
            result = powerForce.powerForce(
                P=array[enrg.powerForce.variables[0]], F=array[enrg.powerForce.variables[1]], V=array[enrg.powerForce.variables[2]])
        case 30:
            result = eKin.eKin(E=array[enrg.eKin.variables[0]],
                               M=array[enrg.eKin.variables[1]], V=array[enrg.eKin.variables[2]])
        case 31:
            result = ePot.ePot(E=array[enrg.ePot.variables[0]], M=array[enrg.ePot.variables[1]],
                               H=array[enrg.ePot.variables[2]], G=array[enrg.ePot.variables[3]])
        case 32:
            result = fullEnergy.fullEnergy(
                P=array[enrg.fullEnergy.variables[0]], K=array[enrg.fullEnergy.variables[1]], F=array[enrg.fullEnergy.variables[2]])
        case 33:
            result = heat.heat(H=array[enrg.heat.variables[0]], DT=array[enrg.heat.variables[1]],
                               C=array[enrg.heat.variables[2]], M=array[enrg.heat.variables[3]])
        case 34:
            result = heatBurn.heatBurn(
                Q=array[enrg.heatBurn.variables[0]], QH=array[enrg.heatBurn.variables[1]], M=array[enrg.heatBurn.variables[2]])
        case 35:
            result = wobbleMass.wobbleMass(
                M=array[osc.wobbleMass.variables[0]], W=array[osc.wobbleMass.variables[1]], K=array[osc.wobbleMass.variables[2]])
        case 36:
            result = wobbleLenght.wobbleLenght(
                G=array[osc.wobbleMass.variables[0]], W=array[osc.wobbleMass.variables[1]], L=array[osc.wobbleMass.variables[2]])
        
    return result


#clears array from desired one(if there is one)
def missingClearFunc(missingVal, desired):
    temporaryArr = []
    for i in missingVal:
        temporaryArr.append(i)

    for i in missingVal:
        if i == desired:
            temporaryArr.remove(i)
            pass

    return temporaryArr




# deletes desired from arr
def desiredClear(valuesArr, desired):
    temporaryArr = {}
    for i in valuesArr:
        temporaryArr[i] = valuesArr[i]
    for i in valuesArr:
        if i == desired:
            temporaryArr.pop(i)

    return temporaryArr



#valuesArr(input from the app)
#desires(something we look for)
#odds(comparisonPersentage????)
#
def methodCheck(odds, valuesArr, variables, desired):
    suitable = 0
    temporaryArr = {}
    temporaryArrS = {}
    # recreation temporary valuesArr
    for i in valuesArr:
        temporaryArrS[i] = valuesArr[i]
    # ////////////////////////////////////////////////////////
    res = 0
    temporaryValues = desiredClear(valuesArr, desired)
    temporaryNames = list(temporaryValues)
    # /////////////////////////////////////////////////
    #checks CAN desired even be found
    for i in odds:
        misNum = missingQuantity(temporaryNames, variables[i])
        print(misNum)
        if odds.get(i) > 0:
            if len(misNum) > 1:
                print("NO")
                pass
            elif len(misNum) == 1:
                temporaryArrS[misNum[0]] = "f"
                res = matchMethod(i, temporaryArrS)
                temporaryArr[misNum[0]] = res
                suitable += 1
                print("YES")
                print(temporaryArr)
            elif len(misNum) < 1:
                print("NO")
                pass

    return temporaryArr, suitable

#fully clears array
def valueArrClear(valuesArr):
    valueArr = {}
    return valueArr

def finalSolver(odds, valuesArr, variables, desi):
    s = 0
    res = 0
    temporaryArr = {}
    print(valuesArr)
    for i in valuesArr:
        temporaryArr[i] = valuesArr[i]
    temporaryArr = desiredClear(temporaryArr, desi)
    while s < 1:
        methodCheckRes = methodCheck(odds, temporaryArr, variables, desired)
        temporaryArr.update(methodCheckRes[0])
        for i in temporaryArr:
            print(i)
            print(desi)
            if i == desi:
                s += 1
                res = temporaryArr[i]
        print(temporaryArr)
        print("||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||")
        pass

    return res


# пробдемы:
# последовательность
# более глубокие задачи
# недостаток библиотеки
