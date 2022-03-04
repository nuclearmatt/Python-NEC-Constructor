from headers.StandardModules import *
from methods.Rotation import Rotation
from methods.Translation import Translation

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
    
    def TranslateModel(self,
                       TransX,
                       TransY,
                       TransZ,
                       **kwargs):
        
        for ele in range (0, len(self.Elements)):
        
            Translation(Element=self.Elements[ele].PhysicalVolume,
                        TransX=TransX,
                        TransY=TransY,
                        TransZ=TransZ)
        
    def ConvertUnits(self,
                     ConvertTo,
                     **kwargs):
        
        if (ConvertTo == 'Meters'):
            ConversionFac = 1/12*1200/3937.0
        else:
            ConversionFac = 1.0

        for ele in range (0, len(self.Elements)):
            
            ((self.Elements[ele].PhysicalVolume.X1),
             (self.Elements[ele].PhysicalVolume.Y1),
             (self.Elements[ele].PhysicalVolume.Z1),
             (self.Elements[ele].PhysicalVolume.X2),
             (self.Elements[ele].PhysicalVolume.Y2),
             (self.Elements[ele].PhysicalVolume.Z2),
             (self.Elements[ele].PhysicalVolume.OuterRadius),
             (self.Elements[ele].PhysicalVolume.InnerRadius)) = ((self.Elements[ele].PhysicalVolume.X1*ConversionFac),
                                                                 (self.Elements[ele].PhysicalVolume.Y1*ConversionFac),
                                                                 (self.Elements[ele].PhysicalVolume.Z1*ConversionFac),
                                                                 (self.Elements[ele].PhysicalVolume.X2*ConversionFac),
                                                                 (self.Elements[ele].PhysicalVolume.Y2*ConversionFac),
                                                                 (self.Elements[ele].PhysicalVolume.Z2*ConversionFac),
                                                                 (self.Elements[ele].PhysicalVolume.OuterRadius*ConversionFac),
                                                                 (self.Elements[ele].PhysicalVolume.InnerRadius*ConversionFac))

        return