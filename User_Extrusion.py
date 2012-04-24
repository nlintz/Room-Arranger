from visual import *
import math

def User_Made_Furniture(scene, Curve1=[], Thickness = 2, Positions = [], radius = 0.1,
                        User_Shape = None, Starting_Orientation = (1,0,0)):
    profile = Positions
    #scene.autoscale = False
    scene.forward=Starting_Orientation
    while True:
        if scene.mouse.events:
            m1 = scene.mouse.getevent()
            if m1.click:
                outline = None
                if outline:
                    outline.visible = False
                Curve1.append((m1.pos.x*(abs(scene.forward.x-1)),
                              m1.pos.y*(abs(scene.forward.y-1)),
                              m1.pos.z*(abs(scene.forward.z-1))))
                if scene.forward.x:
                    Positions.append((m1.pos.z, m1.pos.y))
                elif scene.forward.y:
                    Positions.append((m1.pos.x, m1.pos.z))
                elif scene.forward.z:
                    Positions.append((m1.pos.y, m1.pos.z))
                outline = curve(pos = Curve1, radius = radius)
                
        if scene.kb.keys and Positions:
            k = scene.kb.getkey()
            if k == 'end':
                for thing in scene.objects:
                    thing.visible = False
                Positions.append(Positions[0])
                User_Shape = shapes.pointlist(pos = Positions)
                User_Demo = extrusion(pos = [(0,0,0),(-Thickness*Starting_Orientation[0],
                                                      -Thickness*Starting_Orientation[1],
                                                      -Thickness*Starting_Orientation[2])],
                                       shape = User_Shape,
                                       material = materials.earth)
            elif k =='a':
                scene.forward = None
                
User_Made_Furniture(scene)
