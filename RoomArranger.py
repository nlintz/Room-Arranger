import sys
from PySide.QtGui import QApplication, QMainWindow, QTextEdit, QPushButton
from PySide import QtCore
from RoomArrangerGui_Final import Ui_MainWindow
from testing12 import *
from threading import Thread
from time import sleep

class MainWindow(QMainWindow, Ui_MainWindow):
    

    def __init__(self, parent=None, room=LeftDormRoom(),defaultsDict={},materialsList=[], materialsListDict={}):
        self.defaultsDict={'Microwave':[1.8,1,1], 'WallLight':[1], 'Poster':[2,2], 'Handle':[.5,materials.shiny], 'Olin_Chair':[], 'Table':[3,3,2.5,materials.wood], 'Chair':[2,2,1.8,materials.wood], 'Refrigerator':[1.6,1.83,2.75], 'Bed':[3.17,7.17,2.83,materials.wood], 'Bookshelf':[2.5,1.25,2.25,materials.wood], 'Closet':[3,1.85,6.25,materials.wood], 'Lamp':[5,materials.shiny], 'Desk':[2.5,5,2.5,materials.wood]}
        self.materialsListDict={11:materials.wood,12:materials.rough,13:materials.marble,1:materials.plastic,2:materials.earth,3:materials.diffuse,4:materials.emissive,5:materials.unshaded,6:materials.shiny,7:materials.chrome,8:materials.blazed,10:materials.silver,9:materials.bricks}
        self.startingRoom = room
        room.walls_view()
        
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
  
        self.TableButton.clicked.connect(self.make_Table)
        self.TableWidth.valueChanged.connect(self.changeTableWidth)
        self.TableLength.valueChanged.connect(self.changeTableLength)
        self.TableHeight.valueChanged.connect(self.changeTableHeight)
        
        self.MicrowaveButton.clicked.connect(self.make_Microwave)
        self.MIcrowaveWidth.valueChanged.connect(self.changeMicrowaveWidth)
        self.MicrowaveLength.valueChanged.connect(self.changeMicrowaveLength)
        self.MicrowaveHeight.valueChanged.connect(self.changeMicrowaveHeight)

        self.LampButton.clicked.connect(self.make_Lamp)
        self.LampHeight.valueChanged.connect(self.changeLampHeight)

        self.WallLightButton.clicked.connect(self.make_WallLight)
        self.WallLightHeight.valueChanged.connect(self.changeWallLightHeight)

        self.PosterButton.clicked.connect(self.make_Poster)
        self.PosterWidth.valueChanged.connect(self.changePosterWidth)
        self.PosterLength.valueChanged.connect(self.changePosterLength)


        self.OlinChairButton.clicked.connect(self.make_Olin_Chair)

        self.ChairButton.clicked.connect(self.make_Chair)
        self.ChairWidth.valueChanged.connect(self.changeChairWidth)
        self.ChairLength.valueChanged.connect(self.changeChairLength)
        self.ChairHeight.valueChanged.connect(self.changeChairHeight)

        self.RefrigeratorButton.clicked.connect(self.make_Refrigerator)
        self.RefrigeratorWidth.valueChanged.connect(self.changeRefrigeratorWidth)
        self.RefrigeratorLength.valueChanged.connect(self.changeRefrigeratorLength)
        self.RefrigeratorHeight.valueChanged.connect(self.changeRefrigeratorHeight)

        self.BedButton.clicked.connect(self.make_Bed)
        self.BedWidth.valueChanged.connect(self.changeBedWidth)
        self.BedLength.valueChanged.connect(self.changeBedLength)
        self.BedHeight.valueChanged.connect(self.changeBedHeight)

        self.BookshelfButton.clicked.connect(self.make_Bookshelf)
        self.BookshelfWidth.valueChanged.connect(self.changeBookshelfWidth)
        self.BookshelfLength.valueChanged.connect(self.changeBookshelfLength)
        self.BookshelfHeight.valueChanged.connect(self.changeBookshelfHeight)

        self.ClosetButton.clicked.connect(self.make_Closet)
        self.ClosetWidth.valueChanged.connect(self.changeClosetWidth)
        self.ClosetLength.valueChanged.connect(self.changeClosetLength)
        self.ClosetHeight.valueChanged.connect(self.changeClosetHeight)

        self.DeskButton.clicked.connect(self.make_Desk)
        self.DeskWidth.valueChanged.connect(self.changeDeskWidth)
        self.DeskLength.valueChanged.connect(self.changeDeskLength)
        self.DeskHeight.valueChanged.connect(self.changeDeskHeight)

        self.MaterialBox.activated.connect(self.changeMaterial)


        def oscillate():
            while(True):
                self.startingRoom.handler()
                sleep(.1)        
        oscillatingThread = Thread(target=oscillate)
        oscillatingThread.start()

    
    def make_Microwave(self):
        mw=Microwave(self.startingRoom,self.defaultsDict['Microwave'][0],self.defaultsDict['Microwave'][1],self.defaultsDict['Microwave'][2])
        
    def make_WallLight(self,):
        wl=WallLight(self.startingRoom,self.defaultsDict['WallLight'][0])

    def make_Desk(self):
        d=Desk(self.startingRoom)

    def make_Poster(self):
        p=Poster(self.startingRoom,self.defaultsDict['Poster'][0],self.defaultsDict['Poster'][1])

    def make_Handle(self):
        h=Handle(self.startingRoom,self.defaultsDict['Handle'][0],self.defaultsDict['Handle'][1])

    def make_Olin_Chair(self):
        oc=Olin_Chair(self.startingRoom)

    def make_Table(self):
        t=Table(self.startingRoom,self.defaultsDict['Table'][0],self.defaultsDict['Table'][1],self.defaultsDict['Table'][2],self.defaultsDict['Table'][3])
        
    def make_Chair(self):
        c=Chair(self.startingRoom,self.defaultsDict['Chair'][0],self.defaultsDict['Chair'][1],self.defaultsDict['Chair'][2],self.defaultsDict['Chair'][3])
        
    def make_Refrigerator(self):
        r=Refrigerator(self.startingRoom,self.defaultsDict['Refrigerator'][0],self.defaultsDict['Refrigerator'][1],self.defaultsDict['Refrigerator'][2])
       
    def make_Bed(self):
        b=Bed(self.startingRoom,self.defaultsDict['Bed'][0],self.defaultsDict['Bed'][1],self.defaultsDict['Bed'][2],self.defaultsDict['Bed'][3])
    
    def make_Bookshelf(self):
        bs = BookShelf(self.startingRoom,self.defaultsDict['Bookshelf'][0],self.defaultsDict['Bookshelf'][1],self.defaultsDict['Bookshelf'][2],self.defaultsDict['Bookshelf'][3])

    def make_Closet(self):
       cl=Closet(self.startingRoom,self.defaultsDict['Closet'][0],self.defaultsDict['Closet'][1],self.defaultsDict['Closet'][2],self.defaultsDict['Closet'][3])

    def make_Lamp(self):
        l=Lamp(self.startingRoom,self.defaultsDict['Lamp'][0],self.defaultsDict['Lamp'][1])


    def changeTableWidth(self,decimal):
        if decimal>0:
           self.defaultsDict['Table'][0]=decimal
        else:
            pass        
    def changeTableHeight(self,decimal):
        if decimal>0:
           self.defaultsDict['Table'][1]=decimal
        else:
            pass      
    def changeTableLength(self,decimal):
        if decimal>0:
           self.defaultsDict['Table'][2]=decimal
        else:
            pass                

    def changeMicrowaveWidth(self,decimal):
        if decimal>0:
           self.defaultsDict['Microwave'][0]=decimal
        else:
            pass        
    def changeMicrowaveHeight(self,decimal):
        if decimal>0:
           self.defaultsDict['Microwave'][1]=decimal
        else:
            pass      
    def changeMicrowaveLength(self,decimal):
        if decimal>0:
           self.defaultsDict['Microwave'][2]=decimal
        else:
            pass

    def changeLampHeight(self,decimal):
        if decimal>0:
            self.defualtsDict['Lamp'][0]=decimal
        else:
            pass

    def changeWallLightHeight(self,decimal):
        if decimal>0:
            self.defaultsDict['WallLight'][0]=decimal
        else:
            pass
        
    def changePosterWidth(self,decimal):
        if decimal>0:
            self.defaultsDict['WallLight'][0]=decimal
        else:
            pass
    def changePosterLength(self,decimal):
        if decimal>0:
            self.defaultsDict['WallLight'][0]=decimal
        else:
            pass

    def changeHandleLength(self,decimal):
        if decimal>0:
            self.defaultsDict['Handle'][0]=decimal
        else:
            pass

    def changeChairWidth(self,decimal):
        if decimal>0:
            self.defaultsDict['Chair'][0]=decimal
        else:
            pass
    def changeChairLength(self,decimal):
        if decimal>0:
            self.defaultsDict['Chair'][1]=decimal
        else:
            pass
    def changeChairHeight(self,decimal):
        if decimal>0:
            self.defaultsDict['Chair'][2]=decimal
        else:
            pass

    def changeRefrigeratorWidth(self,decimal):
        if decimal>0:
            self.defaultsDict['Refrigerator'][0]=decimal
        else:
            pass
    def changeRefrigeratorLength(self,decimal):
        if decimal>0:
            self.defaultsDict['Refrigerator'][1]=decimal
        else:
            pass
    def changeRefrigeratorHeight(self,decimal):
        if decimal>0:
            self.defaultsDict['Refrigerator'][2]=decimal
        else:
            pass

    def changeBedWidth(self,decimal):
        if decimal>0:
            self.defaultsDict['Bed'][0]=decimal
        else:
            pass
    def changeBedLength(self,decimal):
        if decimal>0:
            self.defaultsDict['Bed'][1]=decimal
        else:
            pass
    def changeBedHeight(self,decimal):
        if decimal>0:
            self.defaultsDict['Bed'][2]=decimal
        else:
            pass

    def changeBookshelfWidth(self,decimal):
        if decimal>0:
            self.defaultsDict['Bookshelf'][0]=decimal
        else:
            pass
    def changeBookshelfLength(self,decimal):
        if decimal>0:
            self.defaultsDict['Bookshelf'][1]=decimal
        else:
            pass
    def changeBookshelfHeight(self,decimal):
        if decimal>0:
            self.defaultsDict['Bookshelf'][2]=decimal
        else:
            pass

    def changeClosetWidth(self,decimal):
        if decimal>0:
            self.defaultsDict['Closet'][0]=decimal
        else:
            pass
    def changeClosetLength(self,decimal):
        if decimal>0:
            self.defaultsDict['Closet'][1]=decimal
        else:
            pass
    def changeClosetHeight(self,decimal):
        if decimal>0:
            self.defaultsDict['Closet'][2]=decimal
        else:
            pass

    def changeDeskWidth(self,decimal):
        if decimal>0:
            self.defaultsDict['Desk'][0]=decimal
        else:
            pass
    def changeDeskLength(self,decimal):
        if decimal>0:
            self.defaultsDict['Desk'][1]=decimal
        else:
            pass
    def changeDeskHeight(self,decimal):
        if decimal>0:
            self.defaultsDict['Desk'][2]=decimal
        else:
            pass

    def changeMaterial(self,material):
        if material != 0:
            if material == 1:
                self.defaultsDict['Bed'][3]=self.materialsListDict[1]
                self.defaultsDict['Bookshelf'][3]=self.materialsListDict[1]
                self.defaultsDict['Closet'][3]=self.materialsListDict[1]
                self.defaultsDict['Handle'][1]=self.materialsListDict[1]
                self.defaultsDict['Lamp'][1]=self.materialsListDict[1]
                self.defaultsDict['Desk'][3]=self.materialsListDict[1]
                self.defaultsDict['Table'][3]=self.materialsListDict[1]
                self.defaultsDict['Chair'][3]=self.materialsListDict[1]
            if material == 2:
                self.defaultsDict['Bed'][3]=self.materialsListDict[2]
                self.defaultsDict['Bookshelf'][3]=self.materialsListDict[2]
                self.defaultsDict['Closet'][3]=self.materialsListDict[2]
                self.defaultsDict['Handle'][1]=self.materialsListDict[2]
                self.defaultsDict['Lamp'][1]=self.materialsListDict[2]
                self.defaultsDict['Desk'][3]=self.materialsListDict[2]
                self.defaultsDict['Table'][3]=self.materialsListDict[2]
                self.defaultsDict['Chair'][3]=self.materialsListDict[2]
            if material == 3:
                self.defaultsDict['Bed'][3]=self.materialsListDict[3]
                self.defaultsDict['Bookshelf'][3]=self.materialsListDict[3]
                self.defaultsDict['Closet'][3]=self.materialsListDict[3]
                self.defaultsDict['Handle'][1]=self.materialsListDict[3]
                self.defaultsDict['Lamp'][1]=self.materialsListDict[3]
                self.defaultsDict['Desk'][3]=self.materialsListDict[3]
                self.defaultsDict['Table'][3]=self.materialsListDict[3]
                self.defaultsDict['Chair'][3]=self.materialsListDict[3]
            if material == 4:
                self.defaultsDict['Bed'][3]=self.materialsListDict[4]
                self.defaultsDict['Bookshelf'][3]=self.materialsListDict[4]
                self.defaultsDict['Closet'][3]=self.materialsListDict[4]
                self.defaultsDict['Handle'][1]=self.materialsListDict[4]
                self.defaultsDict['Lamp'][1]=self.materialsListDict[4]
                self.defaultsDict['Desk'][3]=self.materialsListDict[4]
                self.defaultsDict['Table'][3]=self.materialsListDict[4]
                self.defaultsDict['Chair'][3]=self.materialsListDict[4]
            if material == 5:
                self.defaultsDict['Bed'][3]=self.materialsListDict[5]
                self.defaultsDict['Bookshelf'][3]=self.materialsListDict[5]
                self.defaultsDict['Closet'][3]=self.materialsListDict[5]
                self.defaultsDict['Handle'][1]=self.materialsListDict[5]
                self.defaultsDict['Lamp'][1]=self.materialsListDict[5]
                self.defaultsDict['Desk'][3]=self.materialsListDict[5]
                self.defaultsDict['Table'][3]=self.materialsListDict[5]
                self.defaultsDict['Chair'][3]=self.materialsListDict[5]
            if material == 6:
                self.defaultsDict['Bed'][3]=self.materialsListDict[6]
                self.defaultsDict['Bookshelf'][3]=self.materialsListDict[6]
                self.defaultsDict['Closet'][3]=self.materialsListDict[6]
                self.defaultsDict['Handle'][1]=self.materialsListDict[6]
                self.defaultsDict['Lamp'][1]=self.materialsListDict[6]
                self.defaultsDict['Desk'][3]=self.materialsListDict[6]
                self.defaultsDict['Table'][3]=self.materialsListDict[6]
                self.defaultsDict['Chair'][3]=self.materialsListDict[6]
            if material == 7:
                self.defaultsDict['Bed'][3]=self.materialsListDict[7]
                self.defaultsDict['Bookshelf'][3]=self.materialsListDict[7]
                self.defaultsDict['Closet'][3]=self.materialsListDict[7]
                self.defaultsDict['Handle'][1]=self.materialsListDict[7]
                self.defaultsDict['Lamp'][1]=self.materialsListDict[7]
                self.defaultsDict['Desk'][3]=self.materialsListDict[7]
                self.defaultsDict['Table'][3]=self.materialsListDict[7]
                self.defaultsDict['Chair'][3]=self.materialsListDict[7]
            if material == 8:
                self.defaultsDict['Bed'][3]=self.materialsListDict[8]
                self.defaultsDict['Bookshelf'][3]=self.materialsListDict[8]
                self.defaultsDict['Closet'][3]=self.materialsListDict[8]
                self.defaultsDict['Handle'][1]=self.materialsListDict[8]
                self.defaultsDict['Lamp'][1]=self.materialsListDict[8]
                self.defaultsDict['Desk'][3]=self.materialsListDict[8]
                self.defaultsDict['Table'][3]=self.materialsListDict[8]
                self.defaultsDict['Chair'][3]=self.materialsListDict[8]
            if material == 9:
                self.defaultsDict['Bed'][3]=self.materialsListDict[9]
                self.defaultsDict['Bookshelf'][3]=self.materialsListDict[9]
                self.defaultsDict['Closet'][3]=self.materialsListDict[9]
                self.defaultsDict['Handle'][1]=self.materialsListDict[9]
                self.defaultsDict['Lamp'][1]=self.materialsListDict[9]
                self.defaultsDict['Desk'][3]=self.materialsListDict[9]
                self.defaultsDict['Table'][3]=self.materialsListDict[9]
                self.defaultsDict['Chair'][3]=self.materialsListDict[9]
            if material == 10:
                self.defaultsDict['Bed'][3]=self.materialsListDict[10]
                self.defaultsDict['Bookshelf'][3]=self.materialsListDict[10]
                self.defaultsDict['Closet'][3]=self.materialsListDict[10]
                self.defaultsDict['Handle'][1]=self.materialsListDict[10]
                self.defaultsDict['Lamp'][1]=self.materialsListDict[10]
                self.defaultsDict['Desk'][3]=self.materialsListDict[10]
                self.defaultsDict['Table'][3]=self.materialsListDict[10]
                self.defaultsDict['Chair'][3]=self.materialsListDict[10]
            if material == 11:
                self.defaultsDict['Bed'][3]=self.materialsListDict[11]
                self.defaultsDict['Bookshelf'][3]=self.materialsListDict[11]
                self.defaultsDict['Closet'][3]=self.materialsListDict[11]
                self.defaultsDict['Handle'][1]=self.materialsListDict[11]
                self.defaultsDict['Lamp'][1]=self.materialsListDict[11]
                self.defaultsDict['Desk'][3]=self.materialsListDict[11]
                self.defaultsDict['Table'][3]=self.materialsListDict[11]
                self.defaultsDict['Chair'][3]=self.materialsListDict[11]
            if material == 12:
                self.defaultsDict['Bed'][3]=self.materialsListDict[12]
                self.defaultsDict['Bookshelf'][3]=self.materialsListDict[12]
                self.defaultsDict['Closet'][3]=self.materialsListDict[12]
                self.defaultsDict['Handle'][1]=self.materialsListDict[12]
                self.defaultsDict['Lamp'][1]=self.materialsListDict[12]
                self.defaultsDict['Desk'][3]=self.materialsListDict[12]
                self.defaultsDict['Table'][3]=self.materialsListDict[12]
                self.defaultsDict['Chair'][3]=self.materialsListDict[12]       
        else:
            pass

if __name__ == '__main__':
    app = QApplication(sys.argv)
    frame = MainWindow()
    frame.startingRoom.shouldRun = True
    frame.show()
    app.exec_()    
