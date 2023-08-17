import numpy as np

class simple3d:
    def __init__(self):
        self.screen = np.empty((16,16), dtype="str")
        self.screen[:] = ' '
        self.vproyec = []

    #Objeto.Cubo(5,5,5,[2(X),2(Y)])
    def Cube(self, x:int= 0, y:int = 0, z:int = 0, cord:list = [0,0],d:int = 0):
        """
        x : x size of the object
        y : y size of the object
        z : z size of the object
        cord : cords of the 0 0 0 point [X,Y]        
        d : distance from the camera to the object
        """       
        self.vertex000 = np.array([cord[0],cord[1],0],dtype=np.int8)
        self.vertex100 = np.array([x+cord[0],cord[1],0],dtype=np.int8)
        self.vertex101 = np.array([x+cord[0],cord[1],z],dtype=np.int8)
        self.vertex001 = np.array([cord[0],cord[1],z],dtype=np.int8)
        self.vertex010 = np.array([cord[0],y+cord[1],0],dtype=np.int8)
        self.vertex110 = np.array([x+cord[0],y+cord[1],0],dtype=np.int8)
        self.vertex111 = np.array([x+cord[0],y+cord[1],z],dtype=np.int8)
        self.vertex011 = np.array([cord[0],y+cord[1],z],dtype=np.int8)
        
        self.vertexes = np.array([
                                    self.vertex000,
                                    self.vertex100,
                                    self.vertex101,
                                    self.vertex001,
                                    self.vertex010,
                                    self.vertex110,
                                    self.vertex111,
                                    self.vertex011,
                                ],dtype=np.int8)
        for vertex in range(8):
            if vertex < 8:
                x1, y1, z1 = self.vertexes[vertex]
                
                Xproyection1 = int(x1 * (d / (z1 + d)))
                Yproyection1 = int(y1 * (d / (z1 + d)))
                self.vproyec.append([Xproyection1, Yproyection1])
                
                #x2,y2,z2 = self.vertices[vertice+1]
                #xprojection2 = int(x2 * (d / (z2 + d)))
                #yprojection2 = int(y2 * (d / (z2 + d)))
                
                #self.screen[yprojection1][xprojection1] = "#"
                #dda(yprojection1, yprojection2,xprojection1,xprojection2)
    def dda(self, y1, y2, x1, x2):
        # delta y (dy) y delta x (dx)
        dy = y2 - y1
        dx = x2 - x1

        # Assignation of the step
        step = max(np.abs(dx),np.abs(dy))
        Xincr = dx / step
        Yincr = dy / step
        pxX,pxY = x1,y1 

        for i in range(step+1):
            self.screen[int(pxY)][int(pxX)] = "#"
            pxX += Xincr
            pxY += Yincr