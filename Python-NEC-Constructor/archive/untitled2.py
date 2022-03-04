



SW4 = Element(ElementNumber=4,
              PhysicalVolume=SolidWire(X1 = SY.LSS/2, 
                                       Y1 = 0, 
                                       Z1 = 0, 
                                       X2 = -SY.LSS/2, 
                                       Y2 = 0,
                                       Z2 = 0,
                                       NumberSegments=SY.LSSseg,
                                       OuterRadius=SY.LERa_Ou,
                                       InnerRadius=SY.LERa_In),
              LogicalVolume=Load(Type='WireConductor',
                                 FirstSegment=0,
                                 LastSegment=0,
                                 Conductivity=58000000))

Rotation(Element=SW4.PhysicalVolume,
         Yaw=180,
         Pitch=45,
         Roll=0)

Translation(Element=SW4.PhysicalVolume, 
            TransX=SW3.PhysicalVolume.X2-SW4.PhysicalVolume.X1, 
            TransY=0, 
            TransZ=SW3.PhysicalVolume.Z2+SW4.PhysicalVolume.Z2)

SW5 = Element(ElementNumber=5,
              PhysicalVolume=SolidWire(X1 = -SY.LLS/2, 
                                       Y1 = 0, 
                                       Z1 = 0, 
                                       X2 = SY.LLS/2, 
                                       Y2 = 0,
                                       Z2 = 0,
                                       NumberSegments=SY.LSSseg,
                                       OuterRadius=SY.LERa_Ou,
                                       InnerRadius=SY.LERa_In),
              LogicalVolume=Load(Type='WireConductor',
                                 FirstSegment=0,
                                 LastSegment=0,
                                 Conductivity=58000000))

Translation(Element=SW5.PhysicalVolume, 
            TransX=0, 
            TransY=0, 
            TransZ=SW4.PhysicalVolume.Z2)

SW6 = Element(ElementNumber=6,
              PhysicalVolume=SolidWire(X1 = -SY.LSS/2, 
                                       Y1 = 0, 
                                       Z1 = 0, 
                                       X2 = SY.LSS/2, 
                                       Y2 = 0,
                                       Z2 = 0,
                                       NumberSegments=SY.LSSseg,
                                       OuterRadius=SY.LERa_Ou,
                                       InnerRadius=SY.LERa_In),
              LogicalVolume=Load(Type='WireConductor',
                                 FirstSegment=0,
                                 LastSegment=0,
                                 Conductivity=58000000))

Rotation(Element=SW6.PhysicalVolume,
         Yaw=0,
         Pitch=45,
         Roll=0)

Translation(Element=SW6.PhysicalVolume, 
            TransX=-SW2.PhysicalVolume.X1-SW6.PhysicalVolume.X1, 
            TransY=0, 
            TransZ=SW5.PhysicalVolume.Z2-SW6.PhysicalVolume.Z1)

SW7 = Element(ElementNumber=7,
              PhysicalVolume=SolidWire(X1 = 0, 
                                       Y1 = 0, 
                                       Z1 = SY.LSS/2, 
                                       X2 = 0, 
                                       Y2 = 0,
                                       Z2 = -SY.LSS/2,
                                       NumberSegments=SY.LSSseg,
                                       OuterRadius=SY.LERa_Ou,
                                       InnerRadius=SY.LERa_In),
              LogicalVolume=Load(Type='WireConductor',
                                 FirstSegment=0,
                                 LastSegment=0,
                                 Conductivity=58000000))

Translation(Element=SW7.PhysicalVolume, 
            TransX=-SW3.PhysicalVolume.X1, 
            TransY=0, 
            TransZ=SW6.PhysicalVolume.Z2+SW7.PhysicalVolume.Z2)



# Create Rotation Matrix Function
        
SW1 = StraightWire.Geometry(X1=(SY.LLS/2)*np.cos(SY.L1RotA)-((-SY.LAS/2-(-SY.LAS/2))*np.sin(SY.L1RotA)), 
                            Y1=(SY.LLS/2)*np.sin(SY.L1RotA)+((-SY.LAS/2-(-SY.LAS/2))*np.cos(SY.L1RotA))+(-SY.LAS/2), 
                            Z1=SY.LH, 
                            X2=(-SY.LLS/2)*np.cos(SY.L1RotA)-((-SY.LAS/2-(-SY.LAS/2))*np.sin(SY.L1RotA))+0, 
                            Y2=(-SY.LLS/2)*np.sin(SY.L1RotA)+((-SY.LAS/2-(-SY.LAS/2))*np.cos(SY.L1RotA))+(-SY.LAS/2), 
                            Z2=SY.LH,
                            NumberSegments=SY.LSSseg,
                            WireDiameter=SY.LERa,
                            WireNumber=1)        
        
SW2 = StraightWire.Geometry(X1=(-SY.LLS/2)*np.cos(SY.L1RotA)-((-SY.LAS/2-(-SY.LAS/2))*np.sin(SY.L1RotA))+0,
                            Y1=(-SY.LLS/2)*np.sin(SY.L1RotA)+((-SY.LAS/2-(-SY.LAS/2))*np.cos(SY.L1RotA))+(-SY.LAS/2),
                            Z1=SY.LH,
                            X2=-(SY.LLS/2+SY.LSSA)*np.cos(SY.L1RotA)-((-SY.LAS/2-(-SY.LAS/2))*np.sin(SY.L1RotA))+0,
                            Y2=-(SY.LLS/2+SY.LSSA)*np.sin(SY.L1RotA)+((-SY.LAS/2-(-SY.LAS/2))*np.cos(SY.L1RotA))+(-SY.LAS/2),
                            Z2=SY.LH+SY.LSSO,
                            NumberSegments=SY.LSSseg,
                            WireDiameter=SY.LERa,
                            WireNumber=2)

SW3 = StraightWire.Geometry(X1=-(SY.LLS/2+SY.LSSA)*np.cos(SY.L1RotA)-((-SY.LAS/2-(-SY.LAS/2))*np.sin(SY.L1RotA))+0,
                            Y1=-(SY.LLS/2+SY.LSSA)*np.sin(SY.L1RotA)+((-SY.LAS/2-(-SY.LAS/2))*np.cos(SY.L1RotA))+(-SY.LAS/2),
                            Z1=SY.LH+SY.LSSO,
                            X2=-(SY.LLS/2+SY.LSSA)*np.cos(SY.L1RotA)-((-SY.LAS/2-(-SY.LAS/2))*np.sin(SY.L1RotA))+0,
                            Y2=-(SY.LLS/2+SY.LSSA)*np.sin(SY.L1RotA)+((-SY.LAS/2-(-SY.LAS/2))*np.cos(SY.L1RotA))+(-SY.LAS/2),
                            Z2=SY.LH+SY.LSSO+SY.LMS,
                            NumberSegments=SY.LSSseg,
                            WireDiameter=SY.LERa,
                            WireNumber=3)
                   
SW4 = StraightWire.Geometry(X1=-(SY.LLS/2+SY.LSSA)*np.cos(SY.L1RotA)-((-SY.LAS/2-(-SY.LAS/2))*np.sin(SY.L1RotA))+0,
                            Y1=-(SY.LLS/2+SY.LSSA)*np.sin(SY.L1RotA)+((-SY.LAS/2-(-SY.LAS/2))*np.cos(SY.L1RotA))+(-SY.LAS/2),
                            Z1=SY.LH+SY.LSSO+SY.LMS,
                            X2=-SY.LLS/2*np.cos(SY.L1RotA)-((-SY.LAS/2-(-SY.LAS/2))*np.sin(SY.L1RotA))+0,
                            Y2=-(SY.LLS/2)*np.sin(SY.L1RotA)+((-SY.LAS/2-(-SY.LAS/2))*np.cos(SY.L1RotA))+(-SY.LAS/2),
                            Z2=SY.LH+2*SY.LSSO+SY.LMS,
                            NumberSegments=SY.LSSseg,
                            WireDiameter=SY.LERa,
                            WireNumber=4)

SW5 = StraightWire.Geometry(X1=-SY.LLS/2*np.cos(SY.L1RotA)-((-SY.LAS/2-(-SY.LAS/2))*np.sin(SY.L1RotA))+0,
                            Y1=-(SY.LLS/2)*np.sin(SY.L1RotA)+((-SY.LAS/2-(-SY.LAS/2))*np.cos(SY.L1RotA))+(-SY.LAS/2),
                            Z1=SY.LH+2*SY.LSSO+SY.LMS,
                            X2=SY.LLS/2*np.cos(SY.L1RotA)-((-SY.LAS/2-(-SY.LAS/2))*np.sin(SY.L1RotA))+0	,
                            Y2=(SY.LLS/2)*np.sin(SY.L1RotA)+((-SY.LAS/2-(-SY.LAS/2))*np.cos(SY.L1RotA))+(-SY.LAS/2),
                            Z2=SY.LH+2*SY.LSSO+SY.LMS,
                            NumberSegments=SY.LSSseg,
                            WireDiameter=SY.LERa,
                            WireNumber=5)

SW6 = StraightWire.Geometry(X1=SY.LLS/2*np.cos(SY.L1RotA)-((-SY.LAS/2-(-SY.LAS/2))*np.sin(SY.L1RotA))+0,
                            Y1=(SY.LLS/2)*np.sin(SY.L1RotA)+((-SY.LAS/2-(-SY.LAS/2))*np.cos(SY.L1RotA))+(-SY.LAS/2),
                            Z1=SY.LH+2*SY.LSSO+SY.LMS,
                            X2=(SY.LLS/2+SY.LSSA)*np.cos(SY.L1RotA)-((-SY.LAS/2-(-SY.LAS/2))*np.sin(SY.L1RotA))+0,
                            Y2=(SY.LLS/2+SY.LSSA)*np.sin(SY.L1RotA)+((-SY.LAS/2-(-SY.LAS/2))*np.cos(SY.L1RotA))+(-SY.LAS/2),
                            Z2=SY.LH+SY.LSSO+SY.LMS,
                            NumberSegments=SY.LSSseg,
                            WireDiameter=SY.LERa,
                            WireNumber=6)

SW7 = StraightWire.Geometry(X1=(SY.LLS/2+SY.LSSA)*np.cos(SY.L1RotA)-((-SY.LAS/2-(-SY.LAS/2))*np.sin(SY.L1RotA))+0,
                            Y1=(SY.LLS/2+SY.LSSA)*np.sin(SY.L1RotA)+((-SY.LAS/2-(-SY.LAS/2))*np.cos(SY.L1RotA))+(-SY.LAS/2),
                            Z1=SY.LH+SY.LSSO+SY.LMS,
                            X2=(SY.LLS/2+SY.LSSA)*np.cos(SY.L1RotA)-((-SY.LAS/2-(-SY.LAS/2))*np.sin(SY.L1RotA))+0,
                            Y2=(SY.LLS/2+SY.LSSA)*np.sin(SY.L1RotA)+((-SY.LAS/2-(-SY.LAS/2))*np.cos(SY.L1RotA))+(-SY.LAS/2),
                            Z2=SY.LH+SY.LSSO,
                            NumberSegments=SY.LSSseg,
                            WireDiameter=SY.LERa,
                            WireNumber=7)

SW8 = StraightWire.Geometry(X1=(SY.LLS/2+SY.LSSA)*np.cos(SY.L1RotA)-((-SY.LAS/2-(-SY.LAS/2))*np.sin(SY.L1RotA))+0,
                            Y1=(SY.LLS/2+SY.LSSA)*np.sin(SY.L1RotA)+((-SY.LAS/2-(-SY.LAS/2))*np.cos(SY.L1RotA))+(-SY.LAS/2),
                            Z1=SY.LH+SY.LSSO,
                            X2=SY.LLS/2*np.cos(SY.L1RotA)-((-SY.LAS/2-(-SY.LAS/2))*np.sin(SY.L1RotA))+0,
                            Y2=(SY.LLS/2)*np.sin(SY.L1RotA)+((-SY.LAS/2-(-SY.LAS/2))*np.cos(SY.L1RotA))+(-SY.LAS/2),
                            Z2=SY.LH,
                            NumberSegments=SY.LSSseg,
                            WireDiameter=SY.LERa,
                            WireNumber=8)