from headers.StandardModules import *
from headers.DefaultFilePaths import *

def ConstructNEC(SimulationModel,
                 **kwargs):
    
    Default_GW = '{:<5s}{:<5.0f}{:<5.0f}{:>16.10f}{:>16.10f}{:>16.10f}{:>16.10f}{:>16.10f}{:>16.10f}{:>12.6f}{:<s}'
    Default_LD = '{:<5s}{:<5.0f}{:<5.0f}{:<5.0f}{:<5.0f}{:>12.1f}{:<s}'
    Default_GN = '{:<5s}{:<5.0f}{:<5.0f}{:<10.4f}{:>10.4f}{:<s}'
    Default_EX = '{:<5s}{:<5.0f}{:<5.0f}{:<5.0f}{:>16.10f}{:>16.10f}{:>16.10f}{:>16.10f}{:>16.10f}{:>16.10f}{:<s}'
    Default_FR = '{:<9s}{:>27.10f}{:>16.10f}{:>16.10f}{:>16.10f}{:>16.10f}{:>16.10f}{:<s}'
    Default_GS = '{:<5s}{:<5.0f}{:<5.0f}{:<5.1f}{:<s}'

    with open(path_to_nec_cards+"OctagonLoop.NEC","w") as text_file:
        
        # Writing the Comment Card
        text_file.write("CM \n")
        
        # Writing Comment Card Termination
        text_file.write("CE \n")
        
        # Writing the Element Card(s)
        for ele in range (0, len(SimulationModel.Elements)):
            
            text_file.write(Default_GW.format(SimulationModel.Elements[ele].PhysicalVolume.VolumeType,
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
        
        # Writing Default Dimension Scaling = 1, since the Units are Converted in Python
        text_file.write(Default_GS.format("GS",
                                          0,	
                                          0,	
                                          1.0, 
                                          "\n"))
        
        # Writing End of Geometry Card(s)
        text_file.write("GE \n")
        
        # Writing the Load Card(s)
        for ele in range (0, len(SimulationModel.Elements)):

            text_file.write(Default_LD.format("LD",
                                              SimulationModel.Elements[ele].LogicalVolume.Type,
                                              SimulationModel.Elements[ele].ElementNumber,
                                              SimulationModel.Elements[ele].LogicalVolume.FirstSegment, 
                                              SimulationModel.Elements[ele].LogicalVolume.LastSegment, 
                                              SimulationModel.Elements[ele].LogicalVolume.Conductivity,
                                              "\n"))    

        # Writing the Ground Card(s)
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
        
        # Writing the Source Card(s)
        for src in range (0, len(SimulationModel.Sources)):
            
            text_file.write(Default_EX.format("EX",
                                              SimulationModel.Sources[src].Type,
                                              SimulationModel.Sources[src].TagNumber,
                                              SimulationModel.Sources[src].SegmentNumber,
                                              SimulationModel.Sources[src].OptionalReporting,
                                              SimulationModel.Sources[src].Real,
                                              SimulationModel.Sources[src].Imaginary,
                                              SimulationModel.Sources[src].Magnitude,
                                              SimulationModel.Sources[src].Phase,
                                              SimulationModel.Sources[src].Normalization,
                                              "\n"))

        # Writing the Frequency Card
        for frq in range (0, len(SimulationModel.Frequencies)):
            
            text_file.write(Default_FR.format("FR",
                                              SimulationModel.Frequencies[frq].FrequencyStepping,
                                              SimulationModel.Frequencies[frq].NumberFrequencySteps,
                                              0,
                                              0,
                                              SimulationModel.Frequencies[frq].Frequency,
                                              SimulationModel.Frequencies[frq].FrequencySteppingIncrement,
                                              "\n"))

        # Writing End of Card (No Parameters Required)
        text_file.write("EN \n")

    return