class Element:
    
    def __init__ (self,
                  ElementNumber,
                  PhysicalVolume,
                  LogicalVolume,
                  **kwargs):
        
        self.ElementNumber = ElementNumber
        self.PhysicalVolume = PhysicalVolume
        self.LogicalVolume = LogicalVolume