# Importing Modules
from headers.StandardModules import *

class Symbols:
    
    def __init__ (self,
                  **kwargs):
        
        self.LH = 104.0                                                 # Loop Lower Height (in)
        self.LSS = 30.0                                                 # Loop Short Section (in)
        self.LLS = 60.0                                                 # Loop Long Section (in)
        self.LMS = self.LSS                                             # Loop Middle Section (in)
        self.LNS = 8                                                    # Loop Number Sides
        self.LIA = (180-(360/self.LNS))                                 # Loop Interior Angle (degrees)
        self.CuDia = 0.875                                              # Coper Tube Outer Diameter (in)
        self.LIAC = 360/self.LNS                                        # Loop Interior Angle Compliment (degrees)  
        self.LERa_Ou = self.CuDia/2                                     # Copper Tube Outer Radius (in)        
        self.LERa_In = 0.785/2                                          # Copper Tube Inner Radius (in)
        self.LSSA = self.LSS*np.sin(self.LIAC)                          # Loop Short Side A (in)
        self.LSSO = self.LSS*np.cos(self.LIAC)                          # Loop Short Side B (in)
        self.LLSseg = 9                                                 # Number of Segments
        self.LSSseg = 9                                                 # Number of Segments
        self.SourcePlacement = int(self.LLSseg*0.5)                     # Segment Number to Place Source
        
        self.Design_Wavelength = 40*1/12*1200/3937                      # Wavelength (in)
        self.Design_Spacing = 1.75
        self.LAS = self.Design_Wavelength/self.Design_Spacing           # Loop Array Seperation (in)
                        
        self.Qcap = 5000
        self.OpFreq = 7.1                                               # Operating Frequency (MHz)
        self.Xs_C = 29**-12                                             # Series Capacitor Capacitance (pF)
        self.Xs_R = 1/(2*np.pi*self.OpFreq*10**6*self.Xs_C)/self.Qcap   # Series Capacitor Resistance (ohms)