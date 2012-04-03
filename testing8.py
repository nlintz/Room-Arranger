from visual import *
from visual.controls import *
import math

class Room(object):
    def __init__(self,width=15,height=10,length=12,ambient=0.2,lights=[0.5*norm(vector(0,0,-2)),0.25*norm(vector(0,0.5,2))],autoscale=False,walls=True):
        self.Width = width
        self.Height = height
        self.Length = length
        self.Display = display(center = (width/2.,height/2.,length/2.),
            uniform = True,
            range = (width,height,length),
            autoscale = autoscale,
            ambient = ambient,
            lights = lights,
            up = (0,0,1))
        self.Floor = box(pos=(width/2.,length/2.,0), axis = (1,0,0), size=(width,length,.01), color=(1,0,0))
        self.Walls = walls
        self.ObjectList = [self.Floor]
        if self.Walls:
            self.Ceiling = box(pos=(width/2.,length/2.,height), axis = (1,0,0), size=(width,length,.01))
            self.NorthWall = box(pos=(width/2.,0,height/2.), axis=(1,0,0), size = (width,.01,height))
            self.EastWall = box(pos=(width,length/2.,height/2.), axis=(1,0,0), size = (.01,length,height))
            self.SouthWall = box(pos=(width/2.,length,height/2.), axis=(1,0,0), size = (width,.01,height))
            self.WestWall = box(pos=(0,length/2.,height/2.), axis=(1,0,0),size = (.01,length,height))
            self.ObjectList = self.ObjectList + [self.Ceiling,self.NorthWall,self.EastWall,self.SouthWall,self.WestWall]
    def walls_view(self):
        if self.Display.forward.x>.01:
            self.WestWall.visible = False
            self.EastWall.visible = True
        if self.Display.forward.x<-.01:
            self.EastWall.visible = False
            self.WestWall.visible = True
        if self.Display.forward.y>.01:
            self.NorthWall.visible = False
            self.SouthWall.visible = True
        if self.Display.forward.y<-.01:
            self.SouthWall.visible = False
            self.NorthWall.visible = True
        if self.Display.forward.z>0.23:
            self.Floor.visible = False
            self.Ceiling.visible = True
        if self.Display.forward.z<0.23:
            self.Ceiling.visible = False
            self.Floor.visible = True


class DormRoom(Room):
    def __init__(self):
        Room.__init__(self, length = 18)
        self.DivWall1 = box(pos=(self.Width-4.5,12,self.Height/2.), axis=(1,0,0), size = (9,.01,self.Height))
        self.DivWall2 = box(pos=(1.5,12,self.Height/2.), axis=(1,0,0), size = (3,.01,self.Height),)
        self.SinkBack = box(pos=(self.Width-7,self.Length-4.5,self.Height/2.), axis=(1,0,0), size = (.01,3,self.Height))
        self.SinkSide = box(pos=(self.Width-8,self.Length-3,self.Height/2.), axis=(1,0,0), size = (2,.01,self.Height))
        self.Sink = box(pos=(self.Width-8,self.Length-4.5,2.), axis=(1,0,0), size = (2,3,4))
        self.Window = box(pos=(self.Width/2.,0.01,6), axis=(1,0,0), size = (4.5,.01,5.5), color=color.yellow, material = materials.emissive)
        self.ObjectList = self.ObjectList + [self.DivWall1,self.DivWall2,self.SinkBack,self.SinkSide,self.Sink,self.Window]
    def walls_view(self):
        if self.Display.forward.x>.01:
            self.WestWall.visible = False
            self.EastWall.visible = True
        if self.Display.forward.x<-.01:
            self.EastWall.visible = False
            self.WestWall.visible = True
        if self.Display.forward.y>.01:
            self.NorthWall.visible = False
            self.Window.visible = False
            self.SouthWall.visible = True
        if self.Display.forward.y<-.01:
            self.SouthWall.visible = False
            self.NorthWall.visible = True
            self.Window.visible = True
        if self.Display.forward.z>0.23:
            self.Floor.visible = False
            self.Ceiling.visible = True
        if self.Display.forward.z<0.23:
            self.Ceiling.visible = False
            self.Floor.visible = True
    
class Furniture:
    def __init__(self, Room, Width, Length, Height, Position = []):
        Room.Display.select()
        self.Width = Width
        self.Length = Length
        self.Height = Height
        self.ObjectList = []
        self.Grid_Resolution = 1./12
        self.DragSettings = (False,None,None,False,None,None,None) #inital values for the drag function
        if Position == []:
            self.Pos = vector(0,0,Height)
        else:
            self.Pos = Position
        Room.ObjectList = Room.ObjectList + [self]

    def drag(self, scene):

        drag, New_Pos, Drag_Pos, turn, Turn_Start, Turn_End, m1 = self.DragSettings
        
        if scene.mouse.events: #If something with the mouse happens
            m1 = scene.mouse.getevent() #Figure out what happened
            if m1.press  and not m1.alt: #If mousebutton is pressed and alt is not
                #If cursor position is within the bounds of the tabletop
                for part in self.ObjectList:
                    drag = (m1.pick == part) or drag
                if drag:
                    Drag_Pos = m1.pos #saves initial location
            elif m1.press and m1.alt: #If mousebutton is pressed and alt is also
                for part in self.ObjectList:
                    turn = (m1.pick==part) or turn
                if turn:
                   Turn_Start = m1.pos

        if scene.kb.keys:
            k1 = scene.kb.getkey()
            if k1 == 's':
                Grid_X = int(self.ObjectList[0].pos.x/self.Grid_Resolution)
                Grid_Y = int(self.ObjectList[0].pos.y/self.Grid_Resolution)
                Grid_Z = int(self.ObjectList[0].pos.z/self.Grid_Resolution)
                Move_Pos = vector(self.ObjectList[0].pos.x- Grid_X*self.Grid_Resolution, \
                                  self.ObjectList[0].pos.y- Grid_Y*self.Grid_Resolution, \
                                  self.ObjectList[0].pos.z- Grid_Z*self.Grid_Resolution,)
                for part in self.ObjectList:
                    part.pos -= Move_Pos
                
        if drag:
            New_Pos = scene.mouse.pos
            if m1.drop:
                drag = False
        while New_Pos and Drag_Pos and New_Pos!= Drag_Pos: #if the cursor has move from its initial location
            Move = New_Pos - Drag_Pos
            Drag_Pos = New_Pos #save new position
            #Move object to the new location
            for part in self.ObjectList:
                part.pos += Move
        
        if turn:
            Turn_End = scene.mouse.pos
            if m1.drop:
                turn = False
        while Turn_End and Turn_Start and Turn_End!=Turn_Start:
            Distance = Turn_End.x - Turn_Start.x
            Turn_Start = Turn_End
            Spin = math.pi*(Distance/((self.Width+self.Length)))
            for part in self.ObjectList:
                part.rotate(angle = Spin, axis = (0,0,1), origin = self.ObjectList[0].pos)
        self.DragSettings = (drag, New_Pos, Drag_Pos, turn, Turn_Start, Turn_End, m1)

    def collide(self, room): #STILL IN PROGRESS
        for thing in room.ObjectList:
            if thing != self:
                try:
                    if thing.ObjectList:
                        thing.collide(room)
                except:
                    if thing.__class__.__name__ == 'box':
                        for component in self.ObjectList:
                            if component.__class__.__name__ == 'box':
                                flag = 0
                                dist = component.pos - thing.pos
                                if component.size.x+thing.size.x > abs(dist.x):
                                    flag += 1
                                if component.size.y+thing.size.y > abs(dist.y):
                                    flag += 1
                                if component.size.x+thing.size.z > abs(dist.z):
                                    flag += 1
                                if flag == 3:
                                    return True
        return False
                        
                    


class Table(Furniture):
    def __init__(self, Room, Width,Length, Height, Wood_Thickness, Position = [], Leg_Radius = 0.5,\
                 Wood_Color = (255,0,0), Leg_Color = (0,255,0)):
        Furniture.__init__(self, Room, Width, Length, Height, Position)
        self.Wood_Thickness = Wood_Thickness
        self.X_Margin = Width/10. #Distance from leg center to edge
        self.Y_Margin = Length/10. #Distance from leg center to edge
        self.Leg_Radius = Leg_Radius
        self.Wood_Color = Wood_Color
        self.Leg_Color = Leg_Color
        self.CounterTop = box(pos = (self.Pos), size = (self.Width, self.Length, self.Wood_Thickness), \
                         color = self.Wood_Color, material = materials.wood)
        #Dimensions for the table legs
        Leg_Height = (self.Height - self.Wood_Thickness/2.)
        # Indicated side for indicated dimension (Left side, X dimension = Left_X
        Left_X = self.Pos[0] - (self.Width/2.) + self.X_Margin 
        Right_X = self.Pos[0] + (self.Width/2.) - self.X_Margin
        Top_Y = self.Pos[1] + (self.Length/2.) - self.Y_Margin
        Bottom_Y = self.Pos[1] - (self.Length/2.) + self.Y_Margin
        self.Leg1 = cylinder(pos = (Left_X, Top_Y, (self.Pos[2]-(self.Wood_Thickness/2.))), \
                        axis = (0,0,-Leg_Height), radius = self.Leg_Radius, color = self.Leg_Color)
        self.Leg2 = cylinder(pos = (Right_X, Top_Y, (self.Pos[2]-(self.Wood_Thickness/2.))), \
                        axis = (0,0,-Leg_Height), radius = self.Leg_Radius, color = self.Leg_Color)
        self.Leg3 = cylinder(pos = (Left_X, Bottom_Y, (self.Pos[2]-(self.Wood_Thickness/2.))), \
                        axis = (0,0,-Leg_Height), radius = self.Leg_Radius, color = self.Leg_Color)
        self.Leg4 = cylinder(pos = (Right_X, Bottom_Y, (self.Pos[2]-(self.Wood_Thickness/2.))), \
                        axis = (0,0,-Leg_Height), radius = self.Leg_Radius, color = self.Leg_Color)
        self.ObjectList = [self.CounterTop, self.Leg1, self.Leg2, self.Leg3, self.Leg4]
        

                        
class Chair(Table):
    def __init__(self, Room, Width, Length, Stool_Height, Back_Height, Wood_Thickness, Position = [],):
        Table.__init__(self, Width, Length, Stool_Height, Wood_Thickness, Position, Room = Room)
        self.Back_Height = Back_Height
        self.Seat_Color = (255, 255, 0)
        self.Back_Color = (0, 255, 255)
        self.Leg_Color = (0, 0, 255)
        Back_Y = self.Pos[1]+(self.Width/2.)-(self.Wood_Thickness/2.)
        Back_Z = self.Pos[2]+(self.Back_Height/2.)+(self.Wood_Thickness/2)
        self.Back = box(pos = (self.Pos[0], Back_Y, Back_Z),\
                   size = (self.Width, self.Wood_Thickness, self.Back_Height), material = materials.wood)
        self.ObjectList = self.ObjectList + [self.Back]


class Refrigerator(Furniture):
    def __init__(self, Room, Width, Length, Height, Position = [],):
        Furniture.__init__(self, Room, Width, Length, Height, Position)
        self.Body = box(pos = self.Pos, size = (self.Width, self.Length, self.Height))
        self.ObjectList = [self.Body]

class Bed(Furniture):
    def __init__(self, Width,Length, Height, Back_Height, Wood_Thickness, Mattress_Thickness = 8./12, Position = [], Leg_Radius = 0.5,\
                 Wood_Color = (255,0,0), Sheet_Color = (255, 255, 255)):
        Furniture.__init__(self, Width, Length, Height, Position)
        self.Mattress_Thickness = Mattress_Thickness
        self.Back_Height = Back_Height
        self.Sheet_Color = Sheet_Color
        self.Wood_Thickness = Wood_Thickness
        self.Wood_Color = Wood_Color
        self.Mattress = box(pos = (self.Pos), size = (self.Width, self.Length, self.Mattress_Thickness), \
                         color = self.Sheet_Color)
        self.Head_Pos = self.Pos+vector(0, self.Length/2., self.Back_Height/2.- self.Height)
        self.Foot_Pos = self.Pos+vector(0, -self.Length/2., self.Back_Height/2.- self.Height)
        self.HeadBoard = box(pos = self.Head_Pos, size = (self.Width, self.Wood_Thickness, self.Back_Height),\
                             color = self.Wood_Color, material = materials.wood)
        self.FootBoard = box(pos = self.Foot_Pos, size = (self.Width, self.Wood_Thickness, self.Back_Height),\
                             color = self.Wood_Color, material = materials.wood)        
        self.ObjectList = [self.Mattress, self.HeadBoard, self. FootBoard]

class BookShelf(Furniture):
    def __init__(self, Width, Length, Height, Shelf_Number, Wood_Thickness,\
                 Position = [], Wood_Color = (255, 0, 0)):
        Furniture.__init__(self, Width, Length, Height, Position)
        if Position == []:
            self.Pos = vector(0,0,0)
        else:
             self.Pos = Position
        self.Wood_Thickness = Wood_Thickness
        self.Shelf_Number = Shelf_Number
        self.Wood_Color = Wood_Color
        self.Back_Pos = self.Pos + vector(0, Length, Height/2.)
        self.Backing = box(pos = self.Back_Pos, size = (self.Width,\
                       self.Wood_Thickness, self.Height), color = self.Wood_Color,\
                       material = materials.wood)
        self.Left_Pos = self.Pos + vector(Width/2., Length/2., Height/2.)
        self.Right_Pos = self.Pos + vector(-Width/2., Length/2., Height/2.)
        self.Left_Wall = box(pos = self.Left_Pos, size = (self.Wood_Thickness, \
                         self.Length, self.Height), color = self.Wood_Color,\
                         material = materials.wood)
        self.Right_Wall = box(pos = self.Right_Pos, size = (self.Wood_Thickness, \
                         self.Length, self.Height), color = self.Wood_Color,\
                         material = materials.wood)
        self.ObjectList = [self.Backing, self.Left_Wall, self.Right_Wall]
        self.Shelf_Increment = self.Height/float(self.Shelf_Number)
        for step in range(0,Shelf_Number):
            self.ObjectList.append(box(pos = self.Pos + vector(0, Length/2.,\
                                    step*self.Shelf_Increment), size = (self.Width, \
                                    self.Length, self.Wood_Thickness), color = self.Wood_Color,\
                                    material = materials.wood))

class Closet(BookShelf):
    def __init__(self, Width, Length, Height, Wood_Thickness, Hanger_Height = None, Open = False,
                 Position = [],Wood_Color = (255, 0, 0), Hanger_Radius = 1./12):
        BookShelf.__init__(self, Width, Length, Height, 1, Wood_Thickness,
                           Position, Wood_Color)
        self.Open = Open
        self.Hanger_Radius = Hanger_Radius
        if Hanger_Height == None:
            self.Hanger_Height = Height*0.8
        else:
            self.Hanger_Height = Hanger_Height
        self.Top_Pos = vector(0, Length/2., self.Height)
        self.Top = box(pos = self.Top_Pos, size = (self.Width, self.Length, self.Wood_Thickness),
                       color = self.Wood_Color, material = materials.wood)
        if not self.Open:
            self.Left_Front_Pos = (self.Width/4., 0, self.Height/2.)
            self.Right_Front_Pos = (-self.Width/4., 0, self.Height/2.)
            self.Front_Size = (self.Width/2., self.Wood_Thickness, self.Height)
        elif self.Open:
            self.Left_Front_Pos = (self.Width/2., -self.Width/4., self.Height/2.)
            self.Right_Front_Pos = (-self.Width/2., -self.Width/4., self.Height/2.)
            self.Front_Size = (self.Wood_Thickness, self.Width/2., self.Height)
            
        self.Left_Front = box(pos= self.Left_Front_Pos, size = self.Front_Size,
                              color = self.Wood_Color, material = materials.wood)
        self.Right_Front = box(pos = self.Right_Front_Pos, size= self.Front_Size,
                               color = self.Wood_Color, material = materials.wood)
        self.Hanger_Bar = cylinder(pos = (self.Right_Pos.x, self.Right_Pos.y, self.Hanger_Height),\
                                   axis = (self.Width, 0, 0), radius = self.Hanger_Radius, \
                                   color = self.Wood_Color, material = materials.wood)
        self.ObjectList.append(self.Top)
        self.ObjectList.append(self.Left_Front)
        self.ObjectList.append(self.Right_Front)
        self.ObjectList.append(self.Hanger_Bar)

    '''def spread(self, scene):
        clicked = False
        if scene.mouse.events: #If something with the mouse happens
            m1 = scene.mouse.getevent() #Figure out what happened
            if m1.press  and m1.ctrl: #If mousebutton is pressed and alt is not
                for part in self.ObjectList:
                    clicked = (m1.pick == part) or clicked
            if clicked:
                self.Open = not self.Open
                clicked = False'''            

room1 = DormRoom()
test = Table(room1,2,4,3,.05)
b1 = sphere(color = (0,1,0))
b2 = sphere(pos=(0,0,1),color=color.red)
b3 = sphere(pos = (0,1,0),color=color.blue)
b4 = sphere(pos=(1,0,0),color=color.orange)

while True:
    rate(20)
    room1.walls_view()
    test.drag(room1.Display)
    print(test.collide(room1))


