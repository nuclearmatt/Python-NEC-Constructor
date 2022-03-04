from headers.StandardModules import *
from methods.Chop import Chop

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