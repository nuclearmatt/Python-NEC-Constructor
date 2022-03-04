from headers.StandardModules import *

def Chop(Vector,
         **kwargs):
    
    # Setting Extremely Small Values (Round Off Errors) to Zero
    for i in range (0, len(Vector)):
        if np.abs(Vector[i]) < 0.0000001:
            Vector[i] = 0
    
    return Vector