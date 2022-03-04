# Importing Modules
import numpy as np
import matplotlib.pyplot as plt
import scipy as sp
from pathlib import Path
import os
import matplotlib.colors as mcolors
from random import SystemRandom
from scipy import stats

# Setting Default File Paths
current_dir = os.getcwd()
program_path = Path(current_dir).parent
path_to_data = str(program_path) + "/dat/"
path_to_plots = str(program_path) + "/plots/"


class SimulationConstants:
    def __init__(self):
        
        PermeabilityFreeSpace = 4*np.pi*10**-7
        FeetToMeters = 1200/3937
        InchesToFeet = 1/12
        MetersToCenti = 1/10


class Loop:
    def __init__(self, 
                 ConductorDiameter,
                 AntennaCircumferance,
                 WidthCorrection,
                 NumberTurns,
                 UpperOperatingFrequency,
                 LowerOperatingFrequency,
                 **kwargs):
        
        self.ConductorDiameter = ConductorDiameter*1/12*1200/3937                                   # m
        self.ConductorRadius = 0.5*self.ConductorDiameter                                           # m
        self.NumberTurns = NumberTurns 
        self.AntennaCircumferance = AntennaCircumferance*1200/3937                                  # m        
        self.PermeabilityFreeSpace = 4*np.pi*10**-7                                                 # H/m
        self.PermeativityFreeSpace = 1/(self.PermeabilityFreeSpace*sp.constants.speed_of_light**2)  # F/m, eps0
        self.ConductorConductivity = 5.80*10**7                                                     # S/m
        self.OperatingFrequencies = np.arange(start=LowerOperatingFrequency,
                                              stop=UpperOperatingFrequency,
                                              step=0.005)
        self.AngularFrequencies = 2*np.pi*self.OperatingFrequencies*10**6
        self.Wavelengths = sp.constants.speed_of_light/(self.OperatingFrequencies*10**6)        
        
        # This calculation assumes equal sides, factoring out the long side
        self.WidthCorrection = WidthCorrection #5.0*1200/3937
        self.NumberSides = 8
        self.AdjustedAntennaCircumferance = self.AntennaCircumferance - self.WidthCorrection
        self.Side = self.AdjustedAntennaCircumferance/self.NumberSides                              # m
        self.X = self.Side/np.sqrt(2)                                                               # m
        self.Diameter = self.Side + 2*self.X                                                        # m
        self.CircumscribedRadius = self.Side/(2*np.sin(45*np.pi/180/2))                             # m
        
        # This is the corrected loop area, factorin in the additional length
        self.Area = 2*(1+np.sqrt(2))*self.Side**2 + 0.5*self.WidthCorrection*(self.Side+2*self.X)
        
    class Z_in:
        def __init__(self):
            self.Reactance
            self.Resistance
    
    def WavelengthFraction(self):
        
        return self.AntennaCircumferance/self.Wavelengths    
               
    def RadiationResistance(self):
        
        return 20.0*np.pi**2*(self.AntennaCircumferance/self.Wavelengths)**4*self.NumberTurns**2 
        
    def HighFrequencyResistance(self):
        
        return self.AntennaCircumferance/(2*np.pi*self.ConductorRadius)*self.SurfaceResistance()
        
    def SurfaceResistance(self):
        
        return (self.AngularFrequencies*self.PermeabilityFreeSpace/(2*self.ConductorConductivity))**0.5
        
    
    
    
    
    
    
    
    def ExternalInductance(self):
                        
        B2R = self.ConductorRadius/(self.AntennaCircumferance/(2*np.pi))
        
        #SNL = self.CircumscribedRadius*self.NumberTurns/((self.NumberTurns+1)*self.ConductorDiameter)
        
        #B2R = (self.ConductorRadius/(2*self.CircumscribedRadius))
                
        SNL = self.Side*self.NumberTurns/((self.NumberTurns+1)*self.ConductorDiameter)
        
        class Inductance(self):
            def __init__(self):
                
                ARRL = 0.016*self.NumberTurns**2*self.Side*100*(np.log(2.613*SNL)+0.75143+(0.07153*1/SNL))                          # Micro Henries
                Grover = 0.016*self.NumberTurns**2*self.Side*100*(np.log(1/B2R)+0.75143+0.18693*B2R+0.11969*B2R**2-0.08234*B2R**4)  # Micro Henries
        
        
        
        
        L1 = 0.016*self.NumberTurns**2*self.Side*100*(np.log(2.613*SNL)+0.75143+(0.07153*1/SNL))                        # Micro Henries
        
        L2 = 0.016*self.NumberTurns**2*self.Side*100*(np.log(1/B2R)+0.75143+0.18693*B2R+0.11969*B2R**2-0.08234*B2R**4)  # Micro Henries
        
        return Inductance() #L1, L2
    
    def InternalInductance(self):
        
        Li = 10**6*self.AntennaCircumferance/(self.AngularFrequencies*2*np.pi*self.ConductorRadius)*(self.AngularFrequencies*self.PermeabilityFreeSpace/(2*self.ConductorConductivity))**0.5   # Micro Henries
        
        return Li
    
    
    
    

            
            
    def InputImpedance(self):
        
        ImpedanceIn = self.Z_in
        
        ImpedanceIn.Reactance = self.AngularFrequencies*(self.InternalInductance() + self.ExternalInductance().ARRL)*10**-6
        
        ImpedanceIn.Resistance = self.RadiationResistance() + self.HighFrequencyResistance()
        
        return ImpedanceIn
    
    
    def ResonatingCapacitance(self):
        
        #return self.AngularFrequencies**-1*self.InputImpedance()[1]/(self.InputImpedance()[0]**2+self.InputImpedance()[1]**2)*10**12       # Pico Farads
        return self.AngularFrequencies**-1*self.InputImpedance().Reactance /(self.InputImpedance().Resistance**2+self.InputImpedance().Reactance**2)*10**12       # Pico Farads

    
    
    
    
    
    
    
    
    
    
    
    
    def SelfCapacitance(self):
        
        Dia = self.Diameter
        
        Len = self.ConductorDiameter
        
        Kc = 0.717439*(Dia/Len)+0.933048*(Dia/Len)**1.5+0.106*(Dia/Len)**2
        
        eps0 = self.PermeativityFreeSpace
        
        epsx = self.PermeativityFreeSpace
        
        epsi = self.PermeativityFreeSpace
        
        pit = Len/self.NumberTurns
        
        psi = np.arctan(pit/(np.pi*Dia))
        
        Medhurst =4/np.pi*eps0*Len*(1+0.8249*(Dia/Len)+2.329*(Dia/Len)**1.5)*10**12
        
        CL_DAE = 4/np.pi*eps0*Len*(1+Kc*(1+epsi/epsx)/2)*(1/np.cos(psi)**2)*10**12
        
        mac = 1.127350207*eps0*Len*(1+Kc*(1+epsi/epsx)/2)*10**12
        
        NEC2 = 1/self.ExternalInductance()[0]*10**6*(2*np.pi*42.62*10**6)**-2*10**12
        
        return Medhurst, CL_DAE, mac, NEC2
    
    
    
    
    
    
    
    def Plot(self):
         
        # Setting Plot Formats
        plt.rcParams["font.family"] = "Palatino Linotype"
        
        # Creating Plot of Calculated Resonating Capacitance vs Operating Frequency
        fig, ax1 = plt.subplots(figsize=(12,6))
            
        ax1.set_xlabel(r'Operating Frequency [MHz]',
                       fontname="Palatino Linotype",
                       fontsize=12)
    
        ax1.set_ylabel(r'Resonating Capacitance [pF]',
                       fontname="Palatino Linotype",
                       fontsize=12)
    
        ax1.tick_params(right=True, 
                        labelright=True)
        
        #ax1.set_yscale('log')
        
        ax1.plot(self.OperatingFrequencies,
                 self.ResonatingCapacitance(),
                 "-o",
                 markersize=1,
                 label="Cap",
                 alpha=0.9)
    
        ax1.legend(loc=0)
    
        # Saving Plot Output
        plt.tight_layout()
        plt.savefig(path_to_plots+"Resonating_Capacitance_Required.pdf")

        # Creating Plot of Calculated Radiation Resistance vs Operating Frequency
        fig, ax1 = plt.subplots(figsize=(12,6))
            
        ax1.set_xlabel(r'Operating Frequency [MHz]',
                       fontname="Palatino Linotype",
                       fontsize=12)
    
        ax1.set_ylabel(r'Radiation Resistance [Ohms]',
                       fontname="Palatino Linotype",
                       fontsize=12)
    
        ax1.tick_params(right=True, 
                        labelright=True)
        
        ax1.plot(self.OperatingFrequencies,
                 self.RadiationResistance(),
                 "-o",
                 markersize=1,
                 label="RadR",
                 alpha=0.9)
    
        ax1.legend(loc=0)
    
        # Saving Plot Output
        plt.tight_layout()
        plt.savefig(path_to_plots+"Radiation_Resistance.pdf")























        return      
        
     
    
    
    
    # Not needed for single turn loop, HF Resistance is used, if more than one turn, then use this equation.
    def OhmicResistance(self):
        
        return self.NumberTurns*self.AntennaCircumferance/(2*np.pi)*1/(self.ConductorRadius)*self.SurfaceResistance()*(0+1)
    
    
    def SkinEffectResistance(self):
        
        return self.NumberTurns/(2*np.pi*self.ConductorRadius)*self.SurfaceResistance()
    
    
    
    
    
    

    








    
OctagonLoop = Loop(ConductorDiameter=0.875,
                   AntennaCircumferance=25.0,
                   WidthCorrection=0.0,
                   NumberTurns=1,
                   UpperOperatingFrequency=42.62,
                   LowerOperatingFrequency=3.5)    
    
    
    
    
    
    
    
#print(OctagonLoop.CircumscribedRadius, OctagonLoop.AntennaCircumferance/(2*np.pi))

#print(OctagonLoop.Area)

#print(OctagonLoop.SelfCapacitance())

#print(OctagonLoop.ResonatingCapacitance())
  
    
#print(OctagonLoop.InputImpedance()[0])

#print(OctagonLoop.InputImpedance().Reactance)
    
OctagonLoop.Plot()
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
