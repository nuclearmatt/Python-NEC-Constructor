from headers.StandardModules import *
from methods.Chop import Chop

def Rotation(Element,
             Yaw,
             Pitch,
             Roll,
               **kwargs):
    
    # Converting Tait-Bryan Angles from Degrees to Radians for Calculation
    yaw = Yaw*np.pi/180.0
    pitch = Pitch*np.pi/180.0
    roll = Roll*np.pi/180.0
    
    Vec1 = ((Element.X1), 
            (Element.Y1), 
            (Element.Z1))
    
    Vec2 = ((Element.X2), 
            (Element.Y2), 
            (Element.Z2))

    # Intrinsic General 3D Rotation Matrix
    Rot = np.array((                 
                    (np.cos(yaw)*np.cos(pitch), np.cos(yaw)*np.sin(pitch)*np.sin(roll)-np.sin(yaw)*np.cos(roll), np.cos(yaw)*np.sin(pitch)*np.cos(roll)+np.sin(yaw)*np.sin(roll)),           
                    (np.sin(yaw)*np.cos(pitch), np.sin(yaw)*np.sin(pitch)*np.sin(roll)+np.cos(yaw)*np.cos(roll), np.sin(yaw)*np.sin(pitch)*np.cos(roll)-np.cos(yaw)*np.sin(roll)),           
                    (-np.sin(pitch), np.cos(pitch)*np.sin(roll), np.cos(pitch)*np.cos(roll))     
                    ))
    
    ((Element.X1), 
     (Element.Y1), 
     (Element.Z1)) = Chop(Vector=np.dot(Rot, Vec1))
    
    ((Element.X2), 
     (Element.Y2), 
     (Element.Z2)) = Chop(Vector=np.dot(Rot, Vec2))
    
    return