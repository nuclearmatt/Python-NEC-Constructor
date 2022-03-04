from headers.StandardModules import *

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
        
        self.StartPoint = np.array((X1,Y1,Z1))
        self.StopPoint = np.array((X2,Y2,Z2))
        
        self.VolumeType = "GW"
        
    def Length(self):
        return (np.sqrt((self.X1-self.X2)**2+(self.Y1-self.Y2)**2+(self.Z1-self.Z2)**2)).round(10)
    
    def Volume(self):
        return (np.pi*((0.5*self.OuterRadius)**2 - (0.5*self.InnerRadius)**2)*self.Length()).round(10)
        