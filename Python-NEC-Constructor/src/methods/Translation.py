def Translation(Element,
                TransX,
                TransY,
                TransZ,
                **kwargs):

    ((Element.X1),
     (Element.Y1), 
     (Element.Z1)) = ((Element.X1 + TransX), 
                      (Element.Y1 + TransY), 
                      (Element.Z1 + TransZ))
                      
    ((Element.X2), 
     (Element.Y2), 
     (Element.Z2)) = ((Element.X2 + TransX), 
                      (Element.Y2 + TransY), 
                      (Element.Z2 + TransZ))

    return              