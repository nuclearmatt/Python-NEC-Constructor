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