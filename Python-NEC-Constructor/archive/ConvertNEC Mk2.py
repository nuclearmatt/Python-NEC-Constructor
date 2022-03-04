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
import copy

# Setting Default File Paths
current_dir = os.getcwd()
program_path = Path(current_dir).parent
path_to_data = str(program_path) + "/dat/"
path_to_plots = str(program_path) + "/plots/"

class Symbols:
    
    def __init__ (self,
                  **kwargs):
        
        self.LH = 104.0                                                 # Loop Lower Height (in)
        self.LSS = 30.0                                                 # Loop Short Section (in)
        self.LLS = 60.0                                                 # Loop Long Section (in)
        self.LMS = self.LSS                                             # Loop Middle Section (in)
        self.LNS = 8                                                    # Loop Number Sides
        self.LIA = (180-(360/self.LNS))                                 # Loop Interior Angle (degrees)
        self.CuDia = 0.875                                              # Coper Tube Outer Diameter (in)
        self.LIAC = 360/self.LNS                                        # Loop Interior Angle Compliment (degrees)
        self.Design_Wavelength = 40*1/12*1200/3937                      # Wavelength (in)
        self.Design_Spacing = 1.75
        self.LAS = self.Design_Wavelength/self.Design_Spacing           # Loop Array Seperation (in)
        self.LERa_Ou = self.CuDia/2                                     # Copper Tube Outer Radius (in)        
        self.LERa_In = 0.785/2                                          # Copper Tube Inner Radius (in)
        self.LSSA = self.LSS*np.sin(self.LIAC)                          # Loop Short Side A (in)
        self.LSSO = self.LSS*np.cos(self.LIAC)                          # Loop Short Side B (in)
        self.L1RotA = 0.0                                               # Loop 1 Rotation Angle (degrees)
        self.L2RotA = 0.0                                               # Loop 2 Rotation Angle (degrees)
        self.LLSseg = 29                                                # Number of Segments
        self.LSSseg = 9                                                 # Number of Segments
        self.Qcap = 5000
        self.OpFreq = 3.5                                               # Operating Frequency (MHz)
        self.Xs_C = 29**-12                                             # Series Capacitor Capacitance (pF)
        self.Xs_R = 1/(2*np.pi*self.OpFreq*10**6*self.Xs_C)/self.Qcap   # Series Capacitor Resistance (ohms)

class SimulationModel:
    
    def __init__ (self):
        
        self.Elements = []
        self.Grounds = []
        self.Sources = []
        self.Frequencies = []
        
    def AddElement(self,
                   Element,
                   **kwargs):
        
        self.Elements.append(Element)
        
        return
    
    def AddGround(self,
                  Ground,
                  **kwargs):

        self.Grounds.append(Ground)
        
        return
    
    def AddSource(self,
                  Source,
                  **kwargs):

        self.Sources.append(Source)
        
        return
    
    def AddFrequency(self,
                     Frequency,
                     **kwargs):
        
        self.Frequencies.append(Frequency)
        
        return
    
    def RotateModel(self,
                    Yaw,
                    Pitch,
                    Roll,
                    **kwargs):
        
        for ele in range (0, len(self.Elements)):
            
            Rotation(Element=self.Elements[ele].PhysicalVolume, 
                     Yaw=Yaw, 
                     Pitch=Pitch, 
                     Roll=Roll)
    
    def ConvertUnits(self,
                     ConvertTo,
                     **kwargs):
        
        if (ConvertTo == 'Meters'):
            ConversionFac = 1/12*1200/3937
        else:
            ConversionFac = 1.0

        for ele in range (0, len(self.Elements)):
            
            self.Elements[ele].PhysicalVolume.X1 = self.Elements[ele].PhysicalVolume.X1*ConversionFac
        

        return
        
class Element:
    
    def __init__ (self,
                  ElementNumber,
                  PhysicalVolume,
                  LogicalVolume,
                  **kwargs):
        
        self.ElementNumber = ElementNumber
        self.PhysicalVolume = PhysicalVolume
        self.LogicalVolume = LogicalVolume

class SolidWire:
    
    def __init__ (self,
                  X1,
                  Y1,
                  Z1,
                  X2,
                  Y2,
                  Z2,
                  NumberSegments,
                  OuterRadius,
                  InnerRadius,
                  **kwargs):
            
        self.NumberSegments = NumberSegments
        self.OuterRadius = OuterRadius
        self.InnerRadius = InnerRadius
    
        self.X1 = X1
        self.Y1 = Y1
        self.Z1 = Z1  
        self.X2 = X2
        self.Y2 = Y2
        self.Z2 = Z2
        
    def Length(self):
        return (np.sqrt((self.X1-self.X2)**2+(self.Y1-self.Y2)**2+(self.Z1-self.Z2)**2)).round(10)
    
    def Volume(self):
        return (np.pi*((0.5*self.OuterRadius)**2 - (0.5*self.InnerRadius)**2)*self.Length()).round(10)
        
class Load:
        
    def __init__ (self,
                  Type,
                  FirstSegment,
                  LastSegment,
                  Conductivity,
                  **kwargs):
                
        self.Type = Type
        self.FirstSegment = FirstSegment
        self.LastSegment = LastSegment
        self.Conductivity = Conductivity
        
class Source:
    
    def __init__(self,
                 Type,
                 TagNumber,
                 OptionalReporting,
                 Real,
                 Imaginary,
                 Magnitude,
                 Phase,
                 Normalization,
                 **kwargs):
        
        self.Type = Type
        self.TagNumber = TagNumber
        self.OptionalReporting = OptionalReporting
        self.Real = Real
        self.Imaginary = Imaginary
        self.Magnitude = Magnitude
        self.Phase = Phase
        self.Normalization = Normalization
        

class Ground:
    
    def __init__(self,
                 GroundType,
                 NumberRadials,
                 RelativeEps,
                 Conductivity,
                 **kwargs):
        
        self.GroundType = GroundType
        self.NumberRadials = NumberRadials
        self.RelativeEps = RelativeEps
        self.Conductivity = Conductivity

class Frequency:
    
    def __init__(self,
                 FrequencyStepping,
                 NumberFrequencySteps,
                 Frequency,
                 FrequencySteppingIncrement,
                 **kwargs):
        
        self.FrequencyStepping = FrequencyStepping
        self.NumberFrequencySteps = NumberFrequencySteps
        self.Frequency = Frequency
        self.FrequencySteppingIncrement = FrequencySteppingIncrement
        
def Chop(Vector,
         **kwargs):
    
    # Setting Extremely Small Values (Round Off Errors) to Zero
    for i in range (0, len(Vector)):
        if np.abs(Vector[i]) < 0.0000001:
            Vector[i] = 0
    
    return Vector
    
def Translation(Element,
                TransX,
                TransY,
                TransZ,
                **kwargs):

    ((Element.X1),
     (Element.Y1), 
     (Element.Z1)) = ((Element.X1 + TransX), 
                      (Element.Y1 + TransY), 
                      (Element.Z1 + TransZ))
                      
    ((Element.X2), 
     (Element.Y2), 
     (Element.Z2)) = ((Element.X2 + TransX), 
                      (Element.Y2 + TransY), 
                      (Element.Z2 + TransZ))

    return              
    
def Rotation(Element,
             Yaw,
             Pitch,
             Roll,
               **kwargs):
    
    # Converting Tait-Bryan Angles from Degrees to Radians for Calculation
    yaw = Yaw*np.pi/180.0
    pitch = Pitch*np.pi/180.0
    roll = Roll*np.pi/180.0
    
    Vec1 = ((Element.X1), 
            (Element.Y1), 
            (Element.Z1))
    
    Vec2 = ((Element.X2), 
            (Element.Y2), 
            (Element.Z2))

    # Intrinsic General 3D Rotation Matrix
    Rot = np.array((                 
                    (np.cos(yaw)*np.cos(pitch), np.cos(yaw)*np.sin(pitch)*np.sin(roll)-np.sin(yaw)*np.cos(roll), np.cos(yaw)*np.sin(pitch)*np.cos(roll)+np.sin(yaw)*np.sin(roll)),           
                    (np.sin(yaw)*np.cos(pitch), np.sin(yaw)*np.sin(pitch)*np.sin(roll)+np.cos(yaw)*np.cos(roll), np.sin(yaw)*np.sin(pitch)*np.cos(roll)-np.cos(yaw)*np.sin(roll)),           
                    (-np.sin(pitch), np.cos(pitch)*np.sin(roll), np.cos(pitch)*np.cos(roll))     
                    ))
    
    ((Element.X1), 
     (Element.Y1), 
     (Element.Z1)) = Chop(Vector=np.dot(Rot, Vec1))
    
    ((Element.X2), 
     (Element.Y2), 
     (Element.Z2)) = Chop(Vector=np.dot(Rot, Vec2))
    
    return

def CopyElement(Element,
                ElementNumber,
                **kwargs):
    
    NewElement = copy.deepcopy(Element)
    NewElement.ElementNumber = ElementNumber
    
    return NewElement

def MirrorElement(Element,
                  ElementNumber,
                  **kwargs):
    
    MirroredElement = copy.deepcopy(Element)
    
    Vec2 = np.array(((MirroredElement.PhysicalVolume.X2), 
                     (MirroredElement.PhysicalVolume.Y2), 
                     (MirroredElement.PhysicalVolume.Z2)))

    Vec1 = np.array(((MirroredElement.PhysicalVolume.X1), 
                     (MirroredElement.PhysicalVolume.Y1), 
                     (MirroredElement.PhysicalVolume.Z1)))
    
    Vec1_Mirror = Chop(-1*Vec2)
    Vec2_Mirror = Chop(-1*Vec1)
    
    MirroredElement.PhysicalVolume.X1 = Vec1_Mirror[0]
    MirroredElement.PhysicalVolume.Y1 = Vec1_Mirror[1]
    MirroredElement.PhysicalVolume.Z1 = Vec2[2]
    
    MirroredElement.PhysicalVolume.X2 = Vec2_Mirror[0]
    MirroredElement.PhysicalVolume.Y2 = Vec2_Mirror[1]
    MirroredElement.PhysicalVolume.Z2 = Vec1[2]
    
    MirroredElement.ElementNumber = ElementNumber

    return MirroredElement

def GeometryPointCheck(SimulationModel,
                       *kwargs):
    
    Default_GW = '{:<5s}{:<2.0f}{:^10s}{:>8.4f}{:^10s}{:>8.4f}{:^10s}{:>8.4f}'

    for ele in range (0, len(SimulationModel.Elements)):
        
        print(Default_GW.format("SW ",
                                SimulationModel.Elements[ele].ElementNumber,
                                "X1 = ",
                                SimulationModel.Elements[ele].PhysicalVolume.X1,
                                "Y1 = ",
                                SimulationModel.Elements[ele].PhysicalVolume.Y1,
                                "Z1 = ",
                                SimulationModel.Elements[ele].PhysicalVolume.Z1, 
                                "\n"))
        
        print(Default_GW.format("SW ",
                                SimulationModel.Elements[ele].ElementNumber,
                                "X2 = ",
                                SimulationModel.Elements[ele].PhysicalVolume.X2,
                                "Y2 = ",
                                SimulationModel.Elements[ele].PhysicalVolume.Y2,
                                "Z2 = ",
                                SimulationModel.Elements[ele].PhysicalVolume.Z2, 
                                "\n"))
        print("\n")
        
    return    

def ConstructNEC(SimulationModel,
                 **kwargs):
    
    Default_GW = '{:<5s}{:<5.0f}{:<5.0f}{:>16.10f}{:>16.10f}{:>16.10f}{:>16.10f}{:>16.10f}{:>16.10f}{:>12.6f}{:<s}'
    Default_LD = '{:<5s}{:<5.0f}{:<5.0f}{:<5.0f}{:<5.0f}{:>12.1f}{:<s}'
    Default_GN = '{:<5s}{:<5.0f}{:<5.0f}{:<10.4f}{:>10.4f}{:<s}'
    Default_EX = '{:<5s}{:<4.0f}{:<4.0f}{:>16.10f}{:>16.10f}{:>16.10f}{:>16.10f}{:>16.10f}{:>16.10f}{:<s}'
    Default_FR = '{:<5s}{:>24.10f}{:>16.10f}{:>16.10f}{:>16.10f}{:>16.10f}{:>16.10f}{:<s}'

    with open("OctagonLoop.NEC","w") as text_file:
        text_file.write("CM \n")
        text_file.write("CE \n")
        
        for ele in range (0, len(SimulationModel.Elements)):
            
            text_file.write(Default_GW.format("GW ",
                                              SimulationModel.Elements[ele].ElementNumber,
                                              SimulationModel.Elements[ele].PhysicalVolume.NumberSegments,
                                              SimulationModel.Elements[ele].PhysicalVolume.X1, 
                                              SimulationModel.Elements[ele].PhysicalVolume.Y1, 
                                              SimulationModel.Elements[ele].PhysicalVolume.Z1, 
                                              SimulationModel.Elements[ele].PhysicalVolume.X2, 
                                              SimulationModel.Elements[ele].PhysicalVolume.Y2, 
                                              SimulationModel.Elements[ele].PhysicalVolume.Z2,
                                              SimulationModel.Elements[ele].PhysicalVolume.OuterRadius,
                                              "\n"))
        text_file.write("GS 	0	0	0.0254 \n")
        
        text_file.write("GE \n")
        
        for ele in range (0, len(SimulationModel.Elements)):

            text_file.write(Default_LD.format("LD",
                                              SimulationModel.Elements[ele].LogicalVolume.Type,
                                              SimulationModel.Elements[ele].ElementNumber,
                                              SimulationModel.Elements[ele].LogicalVolume.FirstSegment, 
                                              SimulationModel.Elements[ele].LogicalVolume.LastSegment, 
                                              SimulationModel.Elements[ele].LogicalVolume.Conductivity,
                                              "\n"))    

        for gnd in range (0, len(SimulationModel.Grounds)):

            if(SimulationModel.Grounds[gnd].GroundType==-1):
                
                Default_GN = '{:<5s}{:<5.0f}{:<s}'
                
                text_file.write(Default_GN.format("GN",
                                                  SimulationModel.Grounds[gnd].GroundType, 
                                                  "\n"))  
            else:
                
                text_file.write(Default_GN.format("GN",
                                                  SimulationModel.Grounds[gnd].GroundType, 
                                                  SimulationModel.Grounds[gnd].NumberRadials, 
                                                  SimulationModel.Grounds[gnd].RelativeEps, 
                                                  SimulationModel.Grounds[gnd].Conductivity,
                                                  "\n"))  
                
        # Blank or Zero indicates use of the Extended (Fat) Wire Kernel
        text_file.write("EK \n")
        
        for src in range (0, len(SimulationModel.Sources)):
            
            text_file.write(Default_EX.format("EX",
                                              SimulationModel.Sources[src].Type,
                                              SimulationModel.Sources[src].TagNumber,
                                              SimulationModel.Sources[src].OptionalReporting,
                                              SimulationModel.Sources[src].Real,
                                              SimulationModel.Sources[src].Imaginary,
                                              SimulationModel.Sources[src].Magnitude,
                                              SimulationModel.Sources[src].Phase,
                                              SimulationModel.Sources[src].Normalization,
                                              "\n"))

        for frq in range (0, len(SimulationModel.Frequencies)):
            
            text_file.write(Default_FR.format("FR",
                                              SimulationModel.Frequencies[frq].FrequencyStepping,
                                              SimulationModel.Frequencies[frq].NumberFrequencySteps,
                                              0,
                                              0,
                                              SimulationModel.Frequencies[frq].Frequency,
                                              SimulationModel.Frequencies[frq].FrequencySteppingIncrement,
                                              "\n"))

        # End of Card (No Parameters Required)
        text_file.write("EN \n")

    return




SY = Symbols()       

SW1 = Element(ElementNumber=1,
              PhysicalVolume=SolidWire(X1 = SY.LLS/2, 
                                       Y1 = 0, 
                                       Z1 = 0, 
                                       X2 = -SY.LLS/2, 
                                       Y2 = 0,
                                       Z2 = 0,
                                       NumberSegments=SY.LSSseg,
                                       OuterRadius=SY.LERa_Ou,
                                       InnerRadius=SY.LERa_In),
              LogicalVolume=Load(Type=5,
                                 FirstSegment=0,
                                 LastSegment=0,
                                 Conductivity=58000000))

SW2 = Element(ElementNumber=2,
              PhysicalVolume=SolidWire(X1 = SY.LSS/2, 
                                       Y1 = 0, 
                                       Z1 = 0, 
                                       X2 = -SY.LSS/2, 
                                       Y2 = 0,
                                       Z2 = 0,
                                       NumberSegments=SY.LSSseg,
                                       OuterRadius=SY.LERa_Ou,
                                       InnerRadius=SY.LERa_In),
              LogicalVolume=Load(Type=5,
                                 FirstSegment=0,
                                 LastSegment=0,
                                 Conductivity=58000000))

Rotation(Element=SW2.PhysicalVolume,
         Yaw=0,
         Pitch=45,
         Roll=0)

Translation(Element=SW2.PhysicalVolume, 
            TransX=-SW2.PhysicalVolume.X1-SW1.PhysicalVolume.X1, 
            TransY=0, 
            TransZ=-SW2.PhysicalVolume.Z1)

SW3 = Element(ElementNumber=3,
              PhysicalVolume=SolidWire(X1 = 0, 
                                       Y1 = 0, 
                                       Z1 = -SY.LSS/2, 
                                       X2 = 0, 
                                       Y2 = 0,
                                       Z2 = SY.LSS/2,
                                       NumberSegments=SY.LSSseg,
                                       OuterRadius=SY.LERa_Ou,
                                       InnerRadius=SY.LERa_In),
              LogicalVolume=Load(Type=5,
                                 FirstSegment=0,
                                 LastSegment=0,
                                 Conductivity=58000000))

Translation(Element=SW3.PhysicalVolume, 
            TransX=SW2.PhysicalVolume.X2, 
            TransY=0, 
            TransZ=SW2.PhysicalVolume.Z2+SW3.PhysicalVolume.Z2)

SW4 = Element(ElementNumber=4,
              PhysicalVolume=SolidWire(X1 = SY.LSS/2, 
                                       Y1 = 0, 
                                       Z1 = 0, 
                                       X2 = -SY.LSS/2, 
                                       Y2 = 0,
                                       Z2 = 0,
                                       NumberSegments=SY.LSSseg,
                                       OuterRadius=SY.LERa_Ou,
                                       InnerRadius=SY.LERa_In),
              LogicalVolume=Load(Type=5,
                                 FirstSegment=0,
                                 LastSegment=0,
                                 Conductivity=58000000))

Rotation(Element=SW4.PhysicalVolume,
         Yaw=180,
         Pitch=45,
         Roll=0)

Translation(Element=SW4.PhysicalVolume, 
            TransX=SW3.PhysicalVolume.X2-SW4.PhysicalVolume.X1, 
            TransY=0, 
            TransZ=SW3.PhysicalVolume.Z2+SW4.PhysicalVolume.Z2)

SW5 = Element(ElementNumber=5,
              PhysicalVolume=SolidWire(X1 = -SY.LLS/2, 
                                       Y1 = 0, 
                                       Z1 = 0, 
                                       X2 = SY.LLS/2, 
                                       Y2 = 0,
                                       Z2 = 0,
                                       NumberSegments=SY.LSSseg,
                                       OuterRadius=SY.LERa_Ou,
                                       InnerRadius=SY.LERa_In),
              LogicalVolume=Load(Type=5,
                                 FirstSegment=0,
                                 LastSegment=0,
                                 Conductivity=58000000))

Translation(Element=SW5.PhysicalVolume, 
            TransX=0, 
            TransY=0, 
            TransZ=SW4.PhysicalVolume.Z2)

SW6 = MirrorElement(Element=SW4,
                    ElementNumber=6)

SW7 = MirrorElement(Element=SW3,
                    ElementNumber=7)

SW8 = MirrorElement(Element=SW2,
                    ElementNumber=8)

SRC1 = Source(Type=0, 
              TagNumber=SW1.ElementNumber, 
              OptionalReporting=0, 
              Real=1, 
              Imaginary=0, 
              Magnitude=1, 
              Phase=0, 
              Normalization=0)

GND1 = Ground(GroundType=-1,
              NumberRadials=None,
              RelativeEps=None,
              Conductivity=None)

FRQ1 = Frequency(FrequencyStepping=0, 
                 NumberFrequencySteps=0, 
                 Frequency=SY.OpFreq, 
                 FrequencySteppingIncrement=0)

OctagonLoop = SimulationModel()

OctagonLoop.AddElement(SW1)
OctagonLoop.AddElement(SW2)
OctagonLoop.AddElement(SW3)
OctagonLoop.AddElement(SW4)
OctagonLoop.AddElement(SW5)
OctagonLoop.AddElement(SW6)
OctagonLoop.AddElement(SW7)
OctagonLoop.AddElement(SW8)

OctagonLoop.AddGround(GND1)

OctagonLoop.AddSource(SRC1)

OctagonLoop.AddFrequency(FRQ1)

OctagonLoop.RotateModel(Yaw=0, 
                        Pitch=0, 
                        Roll=0)

#GeometryPointCheck(OctagonLoop)


ConstructNEC(OctagonLoop)











