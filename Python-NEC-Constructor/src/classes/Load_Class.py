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