import sys
import math

#all units in inches, rad, and lbf
trackWidth = 48 #inches
instlRatio = 0.275 #unitless

while True:
    outputText = """Pick a mode: 1 to calculate K_phiB (total a-arm stiffness"),
    2 to calcuate K_thetaB (A-arm rod stiffness),
    3 to calculate lever arm length
    4 to convert from in-lb/deg to in-lb/rad
    5 to convert from in-lb/rad to in-lb/deg
    6 to calculate tube length, minus mid rod end, tube plugs"""
    print(outputText)
    mode = input()
    if(int(mode) == 1):
        K_thetaB = float(input("Enter ARB bar stiffness in (in-lb)/deg: "))
        levArm = float(input("Enter lever arm length in inches: "))
        K_phiB = K_thetaB*180*(instlRatio**2)*(trackWidth**2)/(math.pi*(levArm**2))
        print("K_phiB (total ARB stiffness) in in-lb/rad: " + str(K_phiB))
        print("K_phiB (total ARB stiffness) in in-lb/deg: " + str(K_phiB*math.pi/180))
    elif(int(mode)==2):
        levArm = float(input("Enter lever arm length in inches: "))
        K_phiB = float(input("Enter total ARB stiffness in (in-lb)/deg: "))
        K_thetaB = K_phiB*180*(levArm**2)/(math.pi*(instlRatio*trackWidth)**2)
        print("K_thetaB (bar stiffness) in in-lb/rad: " +str(K_thetaB))
        print("K_thetaB (bar stiffness) in in-lb/deg: " +str(K_thetaB*math.pi/180))
    elif(int(mode) == 3):
        K_thetaB = float(input("Enter ARB bar stiffness in (in-lb)/deg: "))
        K_phiB = float(input("Enter total ARB stiffness in (in-lb)/deg: "))
        levArm = math.sqrt(K_thetaB * ((instlRatio * trackWidth)**2)/(K_phiB))
        print("Lever arm length in inches: " + str(levArm))
    elif(int(mode)==4):
        inlbdeg = float(input("Enter number in in-lb/deg: "))
        print("Value in in-lb/rad: " + str(inlbdeg*180/math.pi))
    elif(int(mode)==5):
        inlbrad = float(input("Enter number in in-lb/rad: "))
        print("Value in in-lb/deg: " +str(inlbrad*math.pi/180))
    elif(int(mode)==6):
        totalLength = float(input("Enter total length in inches: "))
        rodEnd = 1.562 - 0.5
        plugLength = 0.125       
        print("Tube length: " + str(totalLength - 2*rodEnd - 2*plugLength))
        
