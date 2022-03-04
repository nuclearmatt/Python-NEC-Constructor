class Frequency:
    
    def __init__(self,
                 FrequencyStepping,
                 NumberFrequencySteps,
                 Frequency,
                 FrequencySteppingIncrement,
                 **kwargs):
        
        self.FrequencyStepping = FrequencyStepping
        self.NumberFrequencySteps = NumberFrequencySteps
        self.Frequency = Frequency
        self.FrequencySteppingIncrement = FrequencySteppingIncrement