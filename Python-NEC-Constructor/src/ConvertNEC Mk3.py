# Importing Modules, Classes, Methods, and Headers (Other)
from headers.StandardModules import *
from headers.ClassesMethods import (Symbols, 
                                    Element,  
                                    SolidWire, 
                                    Load,
                                    Source,
                                    Ground,
                                    Frequency,
                                    SimulationModel, 
                                    Rotation,
                                    Translation, 
                                    MirrorElement, 
                                    CopyElement, 
                                    GeometryPointCheck, 
                                    ConstructNEC)

# Declaring Instance of Symbols Used
SY = Symbols()       

# Begin Element(s) Geometry Construction

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

# End Element(s) Geometry Construction

# Setting Source Properties
SRC1 = Source(Type=0, 
              TagNumber=SW1.ElementNumber,
              SegmentNumber=SY.SourcePlacement,
              OptionalReporting=0, 
              Real=1, 
              Imaginary=0, 
              Magnitude=1, 
              Phase=0, 
              Normalization=0)

# Setting Ground Properties
GND1 = Ground(GroundType=2,
              NumberRadials=0,
              RelativeEps=5,
              Conductivity=0.002)

# Setting Frequency Properties
FRQ1 = Frequency(FrequencyStepping=0, 
                 NumberFrequencySteps=0, 
                 Frequency=SY.OpFreq, 
                 FrequencySteppingIncrement=0)

# Declaring Instance of the Simulation Model
OctagonLoop = SimulationModel()

# Adding Elements to the Model
OctagonLoop.AddElement(SW1)
OctagonLoop.AddElement(SW2)
OctagonLoop.AddElement(SW3)
OctagonLoop.AddElement(SW4)
OctagonLoop.AddElement(SW5)
OctagonLoop.AddElement(SW6)
OctagonLoop.AddElement(SW7)
OctagonLoop.AddElement(SW8)

# Adding Ground(s) to the Model
OctagonLoop.AddGround(GND1)

# Adding Source(s) to the Model
OctagonLoop.AddSource(SRC1)

# Adding Frequency to the Model
OctagonLoop.AddFrequency(FRQ1)

# Rotating the Entire Model Assembly (Enter Degrees)
OctagonLoop.RotateModel(Yaw=0, 
                        Pitch=0, 
                        Roll=0)

# Translating the Entire Model Assembly (Enter Inches)
OctagonLoop.TranslateModel(TransX=0,
                           TransY=0,
                           TransZ=104)

# Output for Geometry Verification
GeometryPointCheck(OctagonLoop)

# Converting the Model Units
OctagonLoop.ConvertUnits(ConvertTo='Meters')

# Constructing the NEC Input File of the Model
ConstructNEC(OctagonLoop)

