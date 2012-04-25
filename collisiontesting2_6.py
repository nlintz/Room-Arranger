from visual import *

class Room(object):
    def __init__(self,width=15,height=10,length=12,ambient=0.2,lights=[0.5*norm(vector(0,0,-2)),0.25*norm(vector(0,0.5,2))],autoscale=False,walls=True):
        self.Width = width
        self.Height = height
        self.Length = length
        self.Display = display(center = (width/2.,height/2.,length/2.), #create the display window
            uniform = True,
            range = (width,height,length),
            autoscale = autoscale,
            ambient = ambient,
            lights = lights,
            up = (0,0,1))
        self.Walls = Walls(width, height, length, walls) #create the walls
        self.ObjectList = [self.Walls] #add the walls to the object list - room object list should only contain things with an object list. Those object lists should only contain objects
        
    def walls_view(self): #make the walls disappear if they're between the viewer and the center
        try:
            if self.Display.forward.x>.01:
                self.Walls.WestWall.visible = False
                self.Walls.EastWall.visible = True
            if self.Display.forward.x<-.01:
                self.Walls.EastWall.visible = False
                self.Walls.WestWall.visible = True
            if self.Display.forward.y>.01:
                self.Walls.NorthWall.visible = False
                self.Walls.SouthWall.visible = True
            if self.Display.forward.y<-.01:
                self.Walls.SouthWall.visible = False
                self.Walls.NorthWall.visible = True
            if self.Display.forward.z>0.23:
                self.Walls.Floor.visible = False
                self.Walls.Ceiling.visible = True
            if self.Display.forward.z<0.23:
                self.Walls.Ceiling.visible = False
                self.Walls.Floor.visible = True
        except:
            return


class Walls: #class only to be called by room function to create walls
    def __init__(self,width, height, length, walls): #width = x, height = z, length = y, walls = boolean
        self.Floor = box(pos=(width/2.,length/2.,0), size=(width,length,.01), color=(1,0,0))
        self.ObjectList = []
        if walls:
            self.Ceiling = box(pos=(width/2.,length/2.,height), size=(width,length,.01))
            self.NorthWall = box(pos=(width/2.,0,height/2.), size = (width,.01,height))
            self.EastWall = box(pos=(width,length/2.,height/2.), size = (.01,length,height))
            self.SouthWall = box(pos=(width/2.,length,height/2.), size = (width,.01,height))
            self.WestWall = box(pos=(0,length/2.,height/2.), size = (.01,length,height))
            self.ObjectList = self.ObjectList+[self.WestWall]
            

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
        picked= False
        for part in self.ObjectList:
            picked = (scene.mouse.pick == part) or picked
        if scene.mouse.events:
            for part in self.ObjectList:
                picked = (scene.mouse.pick == part) or picked
            if picked or drag or turn:
           #If something with the mouse happens
                m1 = scene.mouse.getevent() #Figure out what happened
                if m1.click:
                    drag = False
                    turn = False
                elif m1.press  and not m1.alt: #If mousebutton is pressed and alt is not
                    #If cursor position is within the bounds of the tabletop
                    for part in self.ObjectList:
                        drag = (m1.pick == part) or drag
                    if drag:
                        Drag_Pos = m1.pos #saves initial location
                    picked = False
                elif m1.press and m1.alt: #If mousebutton is pressed and alt is also
                    for part in self.ObjectList:
                        turn = (m1.pick==part) or turn
                    if turn:
                       Turn_Start = m1.pos
                    picked = False

        if drag:
            New_Pos = scene.mouse.pos
            if m1.drop or m1.click:
                drag = False
        while New_Pos and Drag_Pos and New_Pos!= Drag_Pos: #if the cursor has move from its initial location
            Move = New_Pos - Drag_Pos
            Drag_Pos = New_Pos #save new position
            #Move object to the new location
            for part in self.ObjectList:
                part.pos += Move
        
        if turn:
            Turn_End = scene.mouse.pos
            if m1.drop or m1.click:
                turn = False
        while Turn_End and Turn_Start and Turn_End!=Turn_Start:
            Distance = Turn_End.x - Turn_Start.x
            Turn_Start = Turn_End
            Spin = math.pi*(Distance/((self.Width+self.Length)))
            for part in self.ObjectList:
                part.rotate(angle = Spin, axis = (0,0,1), origin = self.ObjectList[0].pos)
        self.DragSettings = (drag, New_Pos, Drag_Pos, turn, Turn_Start, Turn_End, m1)
        
    def Snap_To_Grid(self, scene):
        picked = False
        for part in self.ObjectList:
            picked = (scene.mouse.pick == part) or picked
        if scene.kb.keys and picked:
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
                picked = False

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
        self.Leg_Height = (self.Height - self.Wood_Thickness/2.)
        # Indicated side for indicated dimension (Left side, X dimension = Left_X
        self.Left_X = self.Pos[0] - (self.Width/2.) + self.X_Margin 
        self.Right_X = self.Pos[0] + (self.Width/2.) - self.X_Margin
        self.Top_Y = self.Pos[1] + (self.Length/2.) - self.Y_Margin
        self.Bottom_Y = self.Pos[1] - (self.Length/2.) + self.Y_Margin
        self.Leg1 = cylinder(pos = (self.Left_X, self.Top_Y, (self.Pos[2]-(self.Wood_Thickness/2.))), \
                        axis = (0,0,-self.Leg_Height), radius = self.Leg_Radius, color = self.Leg_Color)
        self.Leg2 = cylinder(pos = (self.Right_X, self.Top_Y, (self.Pos[2]-(self.Wood_Thickness/2.))), \
                        axis = (0,0,-self.Leg_Height), radius = self.Leg_Radius, color = self.Leg_Color)
        self.Leg3 = cylinder(pos = (self.Left_X, self.Bottom_Y, (self.Pos[2]-(self.Wood_Thickness/2.))), \
                        axis = (0,0,-self.Leg_Height), radius = self.Leg_Radius, color = self.Leg_Color)
        self.Leg4 = cylinder(pos = (self.Right_X, self.Bottom_Y, (self.Pos[2]-(self.Wood_Thickness/2.))), \
                        axis = (0,0,-self.Leg_Height), radius = self.Leg_Radius, color = self.Leg_Color)
        self.ObjectList = [self.Leg1]
        

                        
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

def find_corners(*things):
    '''Find the corners you need to project on axes for the separating axis theorem.
        Works for boxes and cylinders only, and only in the xy plane (cylinders must be a circle in the xy plane).
        For cylinders, finds the points on the circumfrence along the axis pointing towards the boxes center.
        For boxes, finds the corners.'''
    res = []
    for thing in things:
        if thing.__class__.__name__ == 'box':
            ax = thing.axis
            p = [.5*vector(thing.size.x,thing.size.y,0), #makes a list of the corner points assuming a box at (0,0,0) perpendicular to x and y axes
                 .5*vector(thing.size.x,-1*thing.size.y,0),
                 .5*vector(-1*thing.size.x,-1*thing.size.y,0),
                 .5*vector(-1*thing.size.x,thing.size.y,0)]
            angle = ax.diff_angle(vector(1,0,0))
            for i in range(len(p)): #rotate and shift the box
                p[i] = rotate(p[i], angle = angle, axis = (0,0,1))
                p[i] = p[i] + thing.pos
                #test = sphere(pos = p[i], radius = .1, color = color.blue)
            res.append(p)
        if thing.__class__.__name__ == 'cylinder':
            if thing.axis.x==0 and thing.axis.y==0:
                p = []
                for thing2 in things:
                    if thing2 != thing:
                        ax = thing.pos - thing2.pos
                        vec = vector(ax.x,ax.y,0)
                        vec.mag = thing.radius
                        p.append(thing.pos + vec)
                        p.append(thing.pos - vec)
                        #test1 = sphere(pos = p[0], radius = .1, color = color.red)
                        #test2 = sphere(pos = p[1], radius = .1, color = color.red)
                res.append(p)
    return tuple(res)

def has_intersect_xy(p1,p2): #FUCK YOU
    '''takes two lists of the vectors that are the corners of two concave shapes
        and finds if the shapes intersect using the separating axis theorem.
        Has some bug I haven't found yet - doesn't detect collsion in all cases.'''
    #print 'p1', p1, 'p2', p2
    Flag = 0
    for i in range(len(p1)):
        proj1 = [] #initialize lists to hold the projections of the corners onto the vectors
        proj2 = []
        p3 = p1
        p4 = p2
        side = p1[i] - p1[i-1] #find the sides we need to check along
        if len(p1)<3 and i==1: #basically if this a cylinder and the second time through
            vec = side #also check the vector going through the center
        else: 
            vec = cross(side,vector(0,0,1)) #the vector you need to check, in general, is the one perpendicular to the side
        for j in range(len(p1)): #find all the projections of p1 onto the vector
            p3[j] = rotate(p1[j], angle = p1[j].diff_angle(vector(1,0,0)), axis = (0,0,1))
            vec1 = rotate(vec, angle = p1[j].diff_angle(vector(1,0,0)), axis = (0,0,1))
            proj1.append(mag(proj(p3[j],vec1))*cmp(p3[j].x,0))
        for k in range(len(p2)): #find all the projections of p2 onto the vector
            p4[k] = rotate(p2[k], angle = p2[k].diff_angle(vector(1,0,0)), axis = (0,0,1))
            vec2 = rotate(vec, angle = p2[k].diff_angle(vector(1,0,0)), axis = (0,0,1))
            proj2.append(mag(proj(p4[k],vec2))*cmp(p4[k].x,0))
        #print 'proj1', proj1
        #print 'proj2', proj2
        if not ((max(proj2) > max(proj1) and min(proj2) > max(proj1)) or (max(proj2) < min(proj1) and min(proj2) < min(proj1))): #if the aren't disjoint
            Flag += 1
    for i in range(len(p2)): # do the same as above, with the second object's points
        proj1 = []
        proj2 = []
        side = p2[i] - p2[i-1]
        if len(p2)<3 and i==1:
            vec = side
        else:
            vec = cross(side,vector(0,0,1))
        #print vec
        for j in range(len(p1)):
            p3[j] = rotate(p1[j], angle = p1[j].diff_angle(vector(1,0,0)), axis = (0,0,1))
            vec1 = rotate(vec, angle = p1[j].diff_angle(vector(1,0,0)), axis = (0,0,1))
            proj1.append(mag(proj(p3[j],vec1))*cmp(p3[j].x,0))
        for k in range(len(p2)):
            p4[k] = rotate(p2[k], angle = p2[k].diff_angle(vector(1,0,0)), axis = (0,0,1))
            vec2 = rotate(vec, angle = p2[k].diff_angle(vector(1,0,0)), axis = (0,0,1))
            proj2.append(mag(proj(p4[k],vec2))*cmp(p4[k].x,0))
        #print 'proj1', proj1
        #print 'proj2', proj2
        if not ((max(proj2) > max(proj1) and min(proj2) > max(proj1)) or (max(proj2) < min(proj1) and min(proj2) < min(proj1))):
            Flag += 1
    if Flag == len(p1)+len(p2): #if they have overlapped on every vector, they collide (in the x,y plane)
        return True
    else:
        return False

def has_intersect_z(*things):
    '''finds if two objects (cylinders or boxes that have their vertical orientation parallel
        to (0,0,1)) intersect vertically (on the z axis)'''
    things = list(things)
    while len(things) > 1:#while there remain two objects that have not been checked against each other
        thing1 = things.pop(0)
        if thing1.__class__.__name__ == 'box':
            center1 = thing1.pos.z
            dist1 = .5*thing1.size.z #the distance to the top and bottom from the center
        if thing1.__class__.__name__ == 'cylinder' and thing1.axis.x == 0 and thing1.axis.y == 0: #if this is a vertically oriented cylinder
            #print 'cylinder'
            dist1 = .5*thing1.length
            center1 = thing1.pos.z + (dist1 * (thing1.axis.z/abs(thing1.axis.z))) #the vertical center of the cylinder
        #test1 = sphere(pos = (0,0,center1+dist1), color=color.red, radius = .3)
        #test2 = sphere(pos = (0,0,center1-dist1), color=color.blue, radius = .3)
        for thing2 in things: #same as above
            if thing2.__class__.__name__ == 'box':
                center2 = thing2.pos.z
                dist2 = .5*thing2.size.z
            if thing2.__class__.__name__ == 'cylinder' and thing2.axis.x == 0 and thing1.axis.y == 0:
                #print 'cylinder'
                dist2 = .5*thing2.length
                center2 = thing2.pos.z + (dist2 * (thing2.axis.z/abs(thing2.axis.z)))
            #test1 = sphere(pos = (0,0,center2+dist2), color=color.red, radius = .3)
            #test2 = sphere(pos = (0,0,center2-dist2), color=color.blue, radius = .3)
            if center1+dist1 > center2-dist2 and center1-dist1 < center2+dist2: #If the two vertical spans are not disjoint
                return True
    return False
            


def collide(thing1,thing2):
    '''only works for boxes and cylinders with axis n*(0,0,1).
        Finds if they collide in the x, y, and z directions'''
    p1,p2 = find_corners(thing1,thing2)
    if has_intersect_xy(p1,p2):
        #print 'xy'
        return has_intersect_z(thing1,thing2)
    return False

def are_colliding(thing1,thing2):
    '''takes things with object list and tests every thing in each object list against each other for a collision.'''
    try:
        for subthing1 in thing1.ObjectList:
            try:
                for subthing2 in thing2.ObjectList:
                    if collide(subthing1,subthing2):
                        test = sphere(pos = subthing1.pos, radius = .1, color = color.green)
                        return thing2, subthing1, subthing2
            except:
                return 'damn it'
    except:
        return 'damn it'
    return False

def collide_with_room(thing, room):
    for other_thing in room.ObjectList:
        if other_thing != thing:
            x = are_colliding(thing,other_thing)
            if x:
                return x
    return False

room = Room()
test1 = Table(room,1,1,1,.1)
#test2 = Refrigerator(room,1,1,1)
print room.ObjectList
print room.ObjectList[0].ObjectList
print room.ObjectList[1].ObjectList
#print room.ObjectList[2].ObjectList

'''for thing in test1.ObjectList:
    thing.visible = False'''

while True:
    rate(20)
    room.walls_view()
    test1.drag(room.Display)
    print collide_with_room(test1,room)


'''It's passing a table to find corneres - probably as a result of tweaking to make the room work.
Consider putting all the room walls inside their own list, and refernce the list?'''


