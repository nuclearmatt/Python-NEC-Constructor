from headers.StandardModules import *
from headers.DefaultFilePaths import *

def GeometryPointCheck(SimulationModel,
                       *kwargs):
    
    Default_GW = '{:<5s}{:<2.0f}{:^10s}{:>8.4f}{:^10s}{:>8.4f}{:^10s}{:>8.4f}'
    fig, ax1 = plt.subplots(figsize=(12,6))
    ax1 = plt.axes(projection ="3d")
    
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
        

        ax1.scatter3D(SimulationModel.Elements[ele].PhysicalVolume.X1,
                      SimulationModel.Elements[ele].PhysicalVolume.Y1,
                      SimulationModel.Elements[ele].PhysicalVolume.Z1, 
                      color='blue')
        
        ax1.scatter3D(SimulationModel.Elements[ele].PhysicalVolume.X2,
                      SimulationModel.Elements[ele].PhysicalVolume.Y2,
                      SimulationModel.Elements[ele].PhysicalVolume.Z2)
        
    # Saving Plot Output
    plt.tight_layout()
    plt.savefig(path_to_plots+"3D_Geometry_Test.pdf")