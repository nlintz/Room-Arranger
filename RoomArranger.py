import sys
from PySide.QtGui import QApplication, QMainWindow, QTextEdit, QPushButton
from PySide import QtCore
from Gui3 import Ui_MainWindow
from testing10 import *
from threading import Thread
from time import sleep

class MainWindow(QMainWindow, Ui_MainWindow):
    

    def __init__(self, parent=None, room=DormRoom()):
        self.startingRoom = room
        room.walls_view()
        
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)  

  
        self.Table.clicked.connect(self.make_Table)
        self.Chair.clicked.connect(self.make_Chair)
        self.Refrigerator.clicked.connect(self.make_Refrigerator)
        self.Bed.clicked.connect(self.make_Bed)
        self.Bookshelf.clicked.connect(self.make_BookShelf)
        self.Closet.clicked.connect(self.make_Closet)
        self.Lamp.clicked.connect(self.make_Lamp)
        #self.pushButton_10.clicked.connect(self.drag_method)
        

        def oscillate():
            while(True):
                self.startingRoom.handler()
                sleep(.1)
        
        oscillatingThread = Thread(target=oscillate)
        oscillatingThread.start()

    

    def isActiveWindow(self,event):
        if self.isActiveWindow():
            #event.ignore()
            print 'active window'
        else:
            print 'not active window'
            self.startingRoom.handler()
            


    def isActiveWindow(self,e):
        if not isActiveWindow():
            self.drag_method()
            #time = 0
            #while time<10:#
                #rate(20)
                #sleep(.001)
                #self.drag_method()
                #self.startingRoom.walls_view()
                #time+=1

    def make_Table(self):
       
        t=Table(self.startingRoom,2,4,3,.5)
        #while True:
        #    rate(20)
        #    t.drag(self.startingRoom.Display)
        
        #self.drag_method(t)
        
    def make_Chair(self):
        #Chair(self.startingRoom,2,3,4,3,2)
        c=Chair(self.startingRoom,2,3,4,3,2)
        
    def make_Refrigerator(self):
        #Refrigerator(self.startingRoom,2,3,4)
        r=Refrigerator(self.startingRoom,2,3,4)
       
    def make_Bed(self):
        b=Bed(self.startingRoom,2,3,4,2,4)
        
    def make_BookShelf(self):
        bs = BookShelf(self.startingRoom,2,4,5,4,5)

    def make_Closet(self):
       cl=Closet(self.startingRoom,2,4,4,.2)

    def make_Lamp(self):
        l=Lamp(self.startingRoom, 6,.5,.16,.5,.1,1)
    
    
                


if __name__ == '__main__':
    app = QApplication(sys.argv)
    frame = MainWindow()
    frame.startingRoom.shouldRun = True
    frame.show()

    app.exec_()    

