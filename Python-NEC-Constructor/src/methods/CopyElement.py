from headers.StandardModules import *

def CopyElement(Element,
                ElementNumber,
                **kwargs):
    
    NewElement = copy.deepcopy(Element)
    NewElement.ElementNumber = ElementNumber
    
    return NewElement