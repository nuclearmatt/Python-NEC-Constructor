# Importing Modules
import numpy as np
import matplotlib.pyplot as plt
import scipy as sp
from pathlib import Path
import os
import matplotlib.colors as mcolors
from random import SystemRandom
from scipy import stats
import skrf as rf

# Setting Default File Paths
current_dir = os.getcwd()
program_path = Path(current_dir).parent
path_to_data = str(program_path) + "/dat/"
path_to_plots = str(program_path) + "/plots/"



class Symbols:
    
    def __init__ (self,
                  **kwargs):
        self.LH = 96.0                              # Loop Lower Height
        self.LSS = 37.5                             # Loop Short Section
        self.LLS= 37.5                              # Loop Long Section
        self.LMS = 37.5                             # Loop Middle Section
        self.LNS = 8                                            # Loop Number Sides
        self.LIA = (180-(360/self.LoopNumberSides))             # Loop Interior Angle
        self.CuDia = 0.875                                      # Coper Tube Diameter
        self.LIAC = 360/self.LNS                                # Loop Interior Angle Compliment
        self.Design_Wavelength = 40/0.0254                      # Wavelength
        self.Design_Spacing = 1.75
        self.LAS = self.Design_Wavelength/self.Design_Spacing   # Loop Array Seperation
        self.LERa = self.CuDia/2                                # Copper Tube Radius
        self.LSSA = self.LSS*np.sin(self.LIAC)                  # Loop Short Side A
        self.LSSO = self.LSS*np.cos(self.LIAC)                  # Loop Short Side B
        self.L1RotA = 0.0
        self.L2RotA = 0.0
        self.LLSseg = 29
        self.LSSseg = 9
        self.Qcap = 5000
        self.OpFreq = 3.5
        self.Xs_C = 29**-12
        self.Xs_R = 1/(2*np.pi*self.OpFreq*10**6*self.Xs_C)/self.Qcap

SY = Symbols       
        
class StraightWire:
    
    def __init__ (self,
                  X1,
                  Y1,
                  Z1,
                  X2,
                  Y2,
                  Z2,
                  NumberSegments,
                  WireDiameter,
                  WireNumber,
                  **kwargs):
        
        self.NumberSegments = NumberSegments
        self.WireDiameter = WireDiameter
        self.WireNumber = WireNumber
        
        self.X1 = X1
        self.Y1 = Y1
        self.Z1 = Z1  
        self.X2 = X2
        self.Y2 = Y2
        self.Z2 = Z2
        
# Create Rotation Matrix Function
        
SW1 = StraightWire(X1=(SY.LLS/2)*np.cos(SY.L1RotA)-((-SY.LAS/2-(-SY.LAS/2))*np.sin(SY.L1RotA)), 
                   Y1=(SY.LLS/2)*np.sin(SY.L1RotA)+((-SY.LAS/2-(-SY.LAS/2))*np.cos(SY.L1RotA))+(-SY.LAS/2), 
                   Z1=SY.LH, 
                   X2=(-SY.LLS/2)*np.cos(SY.L1RotA)-((-SY.LAS/2-(-SY.LAS/2))*np.sin(SY.L1RotA))+0, 
                   Y2=(-SY.LLS/2)*np.sin(SY.L1RotA)+((-SY.LAS/2-(-SY.LAS/2))*np.cos(SY.L1RotA))+(-SY.LAS/2), 
                   Z2=SY.LH,
                   NumberSegments=SY.LSSseg,
                   WireDiameter=SY.LERa,
                   WireNumber=1)        
        
SW2 = StraightWire(X1=(-SY.LLS/2)*np.cos(SY.L1RotA)-((-SY.LAS/2-(-SY.LAS/2))*np.sin(SY.L1RotA))+0,
                   Y1=(-SY.LLS/2)*np.sin(SY.L1RotA)+((-SY.LAS/2-(-SY.LAS/2))*np.cos(SY.L1RotA))+(-SY.LAS/2),
                   Z1=SY.LH,
                   X2=-(SY.LLS/2+SY.LSSA)*np.cos(SY.L1RotA)-((-SY.LAS/2-(-SY.LAS/2))*np.sin(SY.L1RotA))+0,
                   Y2=-(SY.LLS/2+SY.LSSA)*np.sin(SY.L1RotA)+((-SY.LAS/2-(-SY.LAS/2))*np.cos(SY.L1RotA))+(-SY.LAS/2),
                   Z2=SY.LH+SY.LSSO,
                   NumberSegments=SY.LSSseg,
                   WireDiameter=SY.LERa,
                   WireNumber=2)

SW3 = StraightWire(X1=-(SY.LLS/2+SY.LSSA)*np.cos(SY.L1RotA)-((-SY.LAS/2-(-SY.LAS/2))*np.sin(SY.L1RotA))+0,
                   Y1=-(SY.LLS/2+SY.LSSA)*np.sin(SY.L1RotA)+((-SY.LAS/2-(-SY.LAS/2))*np.cos(SY.L1RotA))+(-SY.LAS/2),
                   Z1=SY.LH+SY.LSSO,
                   X2=-(SY.LLS/2+SY.LSSA)*np.cos(SY.L1RotA)-((-SY.LAS/2-(-SY.LAS/2))*np.sin(SY.L1RotA))+0,
                   Y2=-(SY.LLS/2+SY.LSSA)*np.sin(SY.L1RotA)+((-SY.LAS/2-(-SY.LAS/2))*np.cos(SY.L1RotA))+(-SY.LAS/2),
                   Z2=SY.LH+SY.LSSO+SY.LMS,
                   NumberSegments=SY.LSSseg,
                   WireDiameter=SY.LERa,
                   WireNumber=3)
                   
SW4 = StraightWire(X1=-(SY.LLS/2+SY.LSSA)*np.cos(SY.L1RotA)-((-SY.LAS/2-(-SY.LAS/2))*np.sin(SY.L1RotA))+0,
                   Y1=-(SY.LLS/2+SY.LSSA)*np.sin(SY.L1RotA)+((-SY.LAS/2-(-SY.LAS/2))*np.cos(SY.L1RotA))+(-SY.LAS/2),
                   Z1=SY.LH+SY.LSSO+SY.LMS,
                   X2=-SY.LLS/2*np.cos(SY.L1RotA)-((-SY.LAS/2-(-SY.LAS/2))*np.sin(SY.L1RotA))+0,
                   Y2=-(SY.LLS/2)*np.sin(SY.L1RotA)+((-SY.LAS/2-(-SY.LAS/2))*np.cos(SY.L1RotA))+(-SY.LAS/2),
                   Z2=SY.LH+2*SY.LSSO+SY.LMS,
                   NumberSegments=SY.LSSseg,
                   WireDiameter=SY.LERa,
                   WireNumber=4)

SW5 = StraightWire(X1=-SY.LLS/2*np.cos(SY.L1RotA)-((-SY.LAS/2-(-SY.LAS/2))*np.sin(SY.L1RotA))+0,
                   Y1=-(SY.LLS/2)*np.sin(SY.L1RotA)+((-SY.LAS/2-(-SY.LAS/2))*np.cos(SY.L1RotA))+(-SY.LAS/2),
                   Z1=SY.LH+2*SY.LSSO+SY.LMS,
                   X2=SY.LLS/2*np.cos(SY.L1RotA)-((-SY.LAS/2-(-SY.LAS/2))*np.sin(SY.L1RotA))+0	,
                   Y2=(SY.LLS/2)*np.sin(SY.L1RotA)+((-SY.LAS/2-(-SY.LAS/2))*np.cos(SY.L1RotA))+(-SY.LAS/2),
                   Z2=SY.LH+2*SY.LSSO+SY.LMS,
                   NumberSegments=SY.LSSseg,
                   WireDiameter=SY.LERa,
                   WireNumber=5)

SW6 = StraightWire(X1=SY.LLS/2*np.cos(SY.L1RotA)-((-SY.LAS/2-(-SY.LAS/2))*np.sin(SY.L1RotA))+0,
                   Y1=(SY.LLS/2)*np.sin(SY.L1RotA)+((-SY.LAS/2-(-SY.LAS/2))*np.cos(SY.L1RotA))+(-SY.LAS/2),
                   Z1=SY.LH+2*SY.LSSO+SY.LMS,
                   X2=(SY.LLS/2+SY.LSSA)*np.cos(SY.L1RotA)-((-SY.LAS/2-(-SY.LAS/2))*np.sin(SY.L1RotA))+0,
                   Y2=(SY.LLS/2+SY.LSSA)*np.sin(SY.L1RotA)+((-SY.LAS/2-(-SY.LAS/2))*np.cos(SY.L1RotA))+(-SY.LAS/2),
                   Z2=SY.LH+SY.LSSO+SY.LMS,
                   NumberSegments=SY.LSSseg,
                   WireDiameter=SY.LERa,
                   WireNumber=6)

SW7 = StraightWire(X1=(SY.LLS/2+SY.LSSA)*np.cos(SY.L1RotA)-((-SY.LAS/2-(-SY.LAS/2))*np.sin(SY.L1RotA))+0,
                   Y1=(SY.LLS/2+SY.LSSA)*np.sin(SY.L1RotA)+((-SY.LAS/2-(-SY.LAS/2))*np.cos(SY.L1RotA))+(-SY.LAS/2),
                   Z1=SY.LH+SY.LSSO+SY.LMS,
                   X2=(SY.LLS/2+SY.LSSA)*np.cos(SY.L1RotA)-((-SY.LAS/2-(-SY.LAS/2))*np.sin(SY.L1RotA))+0,
                   Y2=(SY.LLS/2+SY.LSSA)*np.sin(SY.L1RotA)+((-SY.LAS/2-(-SY.LAS/2))*np.cos(SY.L1RotA))+(-SY.LAS/2),
                   Z2=SY.LH+SY.LSSO,
                   NumberSegments=SY.LSSseg,
                   WireDiameter=SY.LERa,
                   WireNumber=7)

SW8 = StraightWire(X1=(SY.LLS/2+SY.LSSA)*np.cos(SY.L1RotA)-((-SY.LAS/2-(-SY.LAS/2))*np.sin(SY.L1RotA))+0,
                   Y1=(SY.LLS/2+SY.LSSA)*np.sin(SY.L1RotA)+((-SY.LAS/2-(-SY.LAS/2))*np.cos(SY.L1RotA))+(-SY.LAS/2),
                   Z1=SY.LH+SY.LSSO,
                   X2=SY.LLS/2*np.cos(SY.L1RotA)-((-SY.LAS/2-(-SY.LAS/2))*np.sin(SY.L1RotA))+0,
                   Y2=(SY.LLS/2)*np.sin(SY.L1RotA)+((-SY.LAS/2-(-SY.LAS/2))*np.cos(SY.L1RotA))+(-SY.LAS/2),
                   Z2=SY.LH,
                   NumberSegments=SY.LSSseg,
                   WireDiameter=SY.LERa,
                   WireNumber=8)

# GW WireNumber NumberSegments X1 Y1 Z1 X2 Y2 Z2

class Load:
        
    def __init__ (self,
                  Type,
                  TagNumber,
                  FirstSegment,
                  LastSegment,
                  Conductivity,
                  **kwargs):
    
        self.Type = Type
        self.TagNumber = TagNumber
        self.FirstSegment = FirstSegment
        self.LastSegment = LastSegment
        self.Conductor = Conductivity

    
LD1 = Load(Type='StraightWire',
           TagNumber=1,
           FirstSegment=,
           LastSegment=,
           Conductivity=)

LD1 = Load(Type='StraightWire',
           TagNumber=1,
           FirstSegment=,
           LastSegment=,
           Conductivity=)

LD1 = Load(Type='StraightWire',
           TagNumber=1,
           FirstSegment=,
           LastSegment=,
           Conductivity=)

LD1 = Load(Type='StraightWire',
           TagNumber=1,
           FirstSegment=,
           LastSegment=,
           Conductivity=)

LD1 = Load(Type='StraightWire',
           TagNumber=1,
           FirstSegment=,
           LastSegment=,
           Conductivity=)   



 
CM
CE


GS	0	0	0.0254
GE	0

LD	5	1	0	0	58000000
LD	5	2	0	0	58000000
LD	5	3	0	0	58000000
LD	5	4	0	0	58000000
LD	5	5	0	0	58000000
LD	5	6	0	0	58000000
LD	5	7	0	0	58000000
LD	5	8	0	0	58000000

GN	-1
EK
EX	0	1	15	0	1	0	0	'9
FR	0	0	0	0	OpFreq	0
EN

        
        
        
        
        
        