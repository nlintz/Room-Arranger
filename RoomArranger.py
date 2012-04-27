import sys
from PySide.QtGui import QApplication, QMainWindow, QTextEdit, QPushButton
from PySide import QtCore
from RoomArrangerGui import Ui_RoomArranger
from testing11 import *
from threading import Thread
from time import sleep

class MainWindow(QMainWindow, Ui_RoomArranger):
    

    def __init__(self, parent=None, room=DormRoom(),defaultsDict={}):
        self.defaultsDict={'Microwave':[1.8,1,1], 'WallLight':[1], 'Poster':[2,2], 'Handle':[.5], 'Olin_Chair':[], 'Table':[3,3,2.5], 'Chair':[2,2,1.8], 'Refrigerator':[1.6,1.83,2.75], 'Bed':[3.17,7.17,2.83], 'Bookshelf':[2.5,1.25,2.25], 'Closet':[3,1.85,6.25], 'Lamp':[5], 'Desk':[2.5,5,2.5]}
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

        self.HandleButton.clicked.connect(self.make_Handle)
        self.HandleLength.valueChanged.connect(self.changeHandleLength)

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
        h=Handle(self.startingRoom)

    def make_Olin_Chair(self):
        oc=Olin_Chair(self.startingRoom)

    def make_Table(self):
        t=Table(self.startingRoom,self.defaultsDict['Table'][0],self.defaultsDict['Table'][1],self.defaultsDict['Table'][2])
        
    def make_Chair(self):
        c=Chair(self.startingRoom)
        
    def make_Refrigerator(self):
        r=Refrigerator(self.startingRoom)
       
    def make_Bed(self):
        b=Bed(self.startingRoom)
    
    def make_Bookshelf(self):
        bs = BookShelf(self.startingRoom)

    def make_Closet(self):
       cl=Closet(self.startingRoom)

    def make_Lamp(self):
        l=Lamp(self.startingRoom,self.defaultsDict['Table'][0])


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

    def changeHandleLength():
        if decimal>0:
            self.defaultsDict['Handle'][0]=decimal
        else:
            pass

    def changeChairWidth():
        if decimal>0:
            self.defaultsDict['Chair'][0]=decimal
        else:
            pass
    def changeChairLength():
        if decimal>0:
            self.defaultsDict['Chair'][1]=decimal
        else:
            pass
    def changeChairHeight():
        if decimal>0:
            self.defaultsDict['Chair'][2]=decimal
        else:
            pass

    def changeRefrigeratorWidth():
        if decimal>0:
            self.defaultsDict['Refrigerator'][0]=decimal
        else:
            pass
    def changeRefrigeratorLength():
        if decimal>0:
            self.defaultsDict['Refrigerator'][1]=decimal
        else:
            pass
    def changeRefrigeratorHeight():
        if decimal>0:
            self.defaultsDict['Refrigerator'][2]=decimal
        else:
            pass

    def changeBedWidth():
        if decimal>0:
            self.defaultsDict['Bed'][0]=decimal
        else:
            pass
    def changeBedLength():
        if decimal>0:
            self.defaultsDict['Bed'][1]=decimal
        else:
            pass
    def changeBedHeight():
        if decimal>0:
            self.defaultsDict['Bed'][2]=decimal
        else:
            pass

    def changeBookshelfWidth():
        if decimal>0:
            self.defaultsDict['Bookshelf'][0]=decimal
        else:
            pass
    def changeBookshelfLength():
        if decimal>0:
            self.defaultsDict['Bookshelf'][1]=decimal
        else:
            pass
    def changeBookshelfHeight():
        if decimal>0:
            self.defaultsDict['Bookshelf'][2]=decimal
        else:
            pass

    def changeClosetWidth():
        if decimal>0:
            self.defaultsDict['Closet'][0]=decimal
        else:
            pass
    def changeClosetLength():
        if decimal>0:
            self.defaultsDict['Closet'][1]=decimal
        else:
            pass
    def changeClosetHeight():
        if decimal>0:
            self.defaultsDict['Closet'][2]=decimal
        else:
            pass

    def changeDeskWidth():
        if decimal>0:
            self.defaultsDict['Desk'][0]=decimal
        else:
            pass
    def changeDeskLength():
        if decimal>0:
            self.defaultsDict['Desk'][1]=decimal
        else:
            pass
    def changeDeskHeight():
        if decimal>0:
            self.defaultsDict['Desk'][2]=decimal
        else:
            pass

if __name__ == '__main__':
    app = QApplication(sys.argv)
    frame = MainWindow()
    frame.startingRoom.shouldRun = True
    frame.show()

    app.exec_()    

