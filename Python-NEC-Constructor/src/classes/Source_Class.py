class Source:
    
    def __init__(self,
                 Type,
                 TagNumber,
                 SegmentNumber,
                 OptionalReporting,
                 Real,
                 Imaginary,
                 Magnitude,
                 Phase,
                 Normalization,
                 **kwargs):
        
        self.Type = Type
        self.TagNumber = TagNumber
        self.SegmentNumber = SegmentNumber
        self.OptionalReporting = OptionalReporting
        self.Real = Real
        self.Imaginary = Imaginary
        self.Magnitude = Magnitude
        self.Phase = Phase
        self.Normalization = Normalization