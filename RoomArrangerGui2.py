# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Gui5.ui'
#
# Created: Tue May  1 12:20:13 2012
#      by: pyside-uic 0.2.11 running on PySide 1.1.0
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 1001)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayoutWidget = QtGui.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 10, 332, 897))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtGui.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.Furniture_Label = QtGui.QLabel(self.gridLayoutWidget)
        self.Furniture_Label.setObjectName("Furniture_Label")
        self.gridLayout.addWidget(self.Furniture_Label, 0, 0, 1, 1)
        self.TopSpacerLabel = QtGui.QLabel(self.gridLayoutWidget)
        self.TopSpacerLabel.setText("")
        self.TopSpacerLabel.setObjectName("TopSpacerLabel")
        self.gridLayout.addWidget(self.TopSpacerLabel, 0, 1, 1, 1)
        self.ElectronicsLabel = QtGui.QLabel(self.gridLayoutWidget)
        self.ElectronicsLabel.setObjectName("ElectronicsLabel")
        self.gridLayout.addWidget(self.ElectronicsLabel, 0, 2, 1, 1)
        self.BedButton = QtGui.QPushButton(self.gridLayoutWidget)
        self.BedButton.setObjectName("BedButton")
        self.gridLayout.addWidget(self.BedButton, 1, 0, 1, 1)
        self.PosterButton = QtGui.QPushButton(self.gridLayoutWidget)
        self.PosterButton.setObjectName("PosterButton")
        self.gridLayout.addWidget(self.PosterButton, 1, 1, 1, 1)
        self.MicrowaveButton = QtGui.QPushButton(self.gridLayoutWidget)
        self.MicrowaveButton.setObjectName("MicrowaveButton")
        self.gridLayout.addWidget(self.MicrowaveButton, 1, 2, 1, 1)
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_30 = QtGui.QLabel(self.gridLayoutWidget)
        self.label_30.setObjectName("label_30")
        self.verticalLayout.addWidget(self.label_30)
        self.BedWidth = QtGui.QSpinBox(self.gridLayoutWidget)
        self.BedWidth.setMaximum(10)
        self.BedWidth.setObjectName("BedWidth")
        self.verticalLayout.addWidget(self.BedWidth)
        self.label_31 = QtGui.QLabel(self.gridLayoutWidget)
        self.label_31.setObjectName("label_31")
        self.verticalLayout.addWidget(self.label_31)
        self.BedLength = QtGui.QSpinBox(self.gridLayoutWidget)
        self.BedLength.setMaximum(10)
        self.BedLength.setObjectName("BedLength")
        self.verticalLayout.addWidget(self.BedLength)
        self.label_32 = QtGui.QLabel(self.gridLayoutWidget)
        self.label_32.setObjectName("label_32")
        self.verticalLayout.addWidget(self.label_32)
        self.BedHeight = QtGui.QSpinBox(self.gridLayoutWidget)
        self.BedHeight.setMaximum(10)
        self.BedHeight.setObjectName("BedHeight")
        self.verticalLayout.addWidget(self.BedHeight)
        self.gridLayout.addLayout(self.verticalLayout, 2, 0, 1, 1)
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_27 = QtGui.QLabel(self.gridLayoutWidget)
        self.label_27.setObjectName("label_27")
        self.verticalLayout_2.addWidget(self.label_27)
        self.PosterWidth = QtGui.QSpinBox(self.gridLayoutWidget)
        self.PosterWidth.setMaximum(10)
        self.PosterWidth.setObjectName("PosterWidth")
        self.verticalLayout_2.addWidget(self.PosterWidth)
        self.label_28 = QtGui.QLabel(self.gridLayoutWidget)
        self.label_28.setObjectName("label_28")
        self.verticalLayout_2.addWidget(self.label_28)
        self.PosterLength = QtGui.QSpinBox(self.gridLayoutWidget)
        self.PosterLength.setMaximum(10)
        self.PosterLength.setObjectName("PosterLength")
        self.verticalLayout_2.addWidget(self.PosterLength)
        self.gridLayout.addLayout(self.verticalLayout_2, 2, 1, 1, 1)
        self.verticalLayout_3 = QtGui.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_18 = QtGui.QLabel(self.gridLayoutWidget)
        self.label_18.setObjectName("label_18")
        self.verticalLayout_3.addWidget(self.label_18)
        self.MIcrowaveWidth = QtGui.QSpinBox(self.gridLayoutWidget)
        self.MIcrowaveWidth.setMaximum(10)
        self.MIcrowaveWidth.setObjectName("MIcrowaveWidth")
        self.verticalLayout_3.addWidget(self.MIcrowaveWidth)
        self.label_19 = QtGui.QLabel(self.gridLayoutWidget)
        self.label_19.setObjectName("label_19")
        self.verticalLayout_3.addWidget(self.label_19)
        self.MicrowaveLength = QtGui.QSpinBox(self.gridLayoutWidget)
        self.MicrowaveLength.setMaximum(10)
        self.MicrowaveLength.setObjectName("MicrowaveLength")
        self.verticalLayout_3.addWidget(self.MicrowaveLength)
        self.label_20 = QtGui.QLabel(self.gridLayoutWidget)
        self.label_20.setObjectName("label_20")
        self.verticalLayout_3.addWidget(self.label_20)
        self.MicrowaveHeight = QtGui.QSpinBox(self.gridLayoutWidget)
        self.MicrowaveHeight.setMaximum(10)
        self.MicrowaveHeight.setObjectName("MicrowaveHeight")
        self.verticalLayout_3.addWidget(self.MicrowaveHeight)
        self.gridLayout.addLayout(self.verticalLayout_3, 2, 2, 1, 1)
        self.BookshelfButton = QtGui.QPushButton(self.gridLayoutWidget)
        self.BookshelfButton.setObjectName("BookshelfButton")
        self.gridLayout.addWidget(self.BookshelfButton, 3, 0, 1, 1)
        self.TableButton = QtGui.QPushButton(self.gridLayoutWidget)
        self.TableButton.setObjectName("TableButton")
        self.gridLayout.addWidget(self.TableButton, 3, 1, 1, 1)
        self.WallLightButton = QtGui.QPushButton(self.gridLayoutWidget)
        self.WallLightButton.setObjectName("WallLightButton")
        self.gridLayout.addWidget(self.WallLightButton, 3, 2, 1, 1)
        self.verticalLayout_4 = QtGui.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_9 = QtGui.QLabel(self.gridLayoutWidget)
        self.label_9.setObjectName("label_9")
        self.verticalLayout_4.addWidget(self.label_9)
        self.BookshelfWidth = QtGui.QSpinBox(self.gridLayoutWidget)
        self.BookshelfWidth.setMaximum(10)
        self.BookshelfWidth.setObjectName("BookshelfWidth")
        self.verticalLayout_4.addWidget(self.BookshelfWidth)
        self.label_10 = QtGui.QLabel(self.gridLayoutWidget)
        self.label_10.setObjectName("label_10")
        self.verticalLayout_4.addWidget(self.label_10)
        self.BookshelfLength = QtGui.QSpinBox(self.gridLayoutWidget)
        self.BookshelfLength.setMaximum(10)
        self.BookshelfLength.setObjectName("BookshelfLength")
        self.verticalLayout_4.addWidget(self.BookshelfLength)
        self.label_11 = QtGui.QLabel(self.gridLayoutWidget)
        self.label_11.setObjectName("label_11")
        self.verticalLayout_4.addWidget(self.label_11)
        self.BookshelfHeight = QtGui.QSpinBox(self.gridLayoutWidget)
        self.BookshelfHeight.setMaximum(10)
        self.BookshelfHeight.setObjectName("BookshelfHeight")
        self.verticalLayout_4.addWidget(self.BookshelfHeight)
        self.gridLayout.addLayout(self.verticalLayout_4, 4, 0, 1, 1)
        self.verticalLayout_5 = QtGui.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label_21 = QtGui.QLabel(self.gridLayoutWidget)
        self.label_21.setObjectName("label_21")
        self.verticalLayout_5.addWidget(self.label_21)
        self.TableWidth = QtGui.QSpinBox(self.gridLayoutWidget)
        self.TableWidth.setMaximum(10)
        self.TableWidth.setObjectName("TableWidth")
        self.verticalLayout_5.addWidget(self.TableWidth)
        self.label_22 = QtGui.QLabel(self.gridLayoutWidget)
        self.label_22.setObjectName("label_22")
        self.verticalLayout_5.addWidget(self.label_22)
        self.TableLength = QtGui.QSpinBox(self.gridLayoutWidget)
        self.TableLength.setMaximum(10)
        self.TableLength.setObjectName("TableLength")
        self.verticalLayout_5.addWidget(self.TableLength)
        self.label_23 = QtGui.QLabel(self.gridLayoutWidget)
        self.label_23.setObjectName("label_23")
        self.verticalLayout_5.addWidget(self.label_23)
        self.TableHeight = QtGui.QSpinBox(self.gridLayoutWidget)
        self.TableHeight.setMaximum(10)
        self.TableHeight.setObjectName("TableHeight")
        self.verticalLayout_5.addWidget(self.TableHeight)
        self.gridLayout.addLayout(self.verticalLayout_5, 4, 1, 1, 1)
        self.verticalLayout_6 = QtGui.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.label_34 = QtGui.QLabel(self.gridLayoutWidget)
        self.label_34.setObjectName("label_34")
        self.verticalLayout_6.addWidget(self.label_34)
        self.WallLightHeight = QtGui.QSpinBox(self.gridLayoutWidget)
        self.WallLightHeight.setMaximum(10)
        self.WallLightHeight.setObjectName("WallLightHeight")
        self.verticalLayout_6.addWidget(self.WallLightHeight)
        self.gridLayout.addLayout(self.verticalLayout_6, 4, 2, 1, 1)
        self.ClosetButton = QtGui.QPushButton(self.gridLayoutWidget)
        self.ClosetButton.setObjectName("ClosetButton")
        self.gridLayout.addWidget(self.ClosetButton, 5, 0, 1, 1)
        self.verticalLayout_7 = QtGui.QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.label_3 = QtGui.QLabel(self.gridLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_7.addWidget(self.label_3)
        self.ClosetWidth = QtGui.QSpinBox(self.gridLayoutWidget)
        self.ClosetWidth.setMaximum(10)
        self.ClosetWidth.setObjectName("ClosetWidth")
        self.verticalLayout_7.addWidget(self.ClosetWidth)
        self.label_4 = QtGui.QLabel(self.gridLayoutWidget)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_7.addWidget(self.label_4)
        self.ClosetLength = QtGui.QSpinBox(self.gridLayoutWidget)
        self.ClosetLength.setMaximum(10)
        self.ClosetLength.setObjectName("ClosetLength")
        self.verticalLayout_7.addWidget(self.ClosetLength)
        self.label_5 = QtGui.QLabel(self.gridLayoutWidget)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_7.addWidget(self.label_5)
        self.ClosetHeight = QtGui.QSpinBox(self.gridLayoutWidget)
        self.ClosetHeight.setMaximum(10)
        self.ClosetHeight.setObjectName("ClosetHeight")
        self.verticalLayout_7.addWidget(self.ClosetHeight)
        self.gridLayout.addLayout(self.verticalLayout_7, 6, 0, 1, 1)
        self.HandleButton = QtGui.QPushButton(self.gridLayoutWidget)
        self.HandleButton.setObjectName("HandleButton")
        self.gridLayout.addWidget(self.HandleButton, 5, 1, 1, 1)
        self.LampButton = QtGui.QPushButton(self.gridLayoutWidget)
        self.LampButton.setObjectName("LampButton")
        self.gridLayout.addWidget(self.LampButton, 5, 2, 1, 1)
        self.verticalLayout_8 = QtGui.QVBoxLayout()
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.label_33 = QtGui.QLabel(self.gridLayoutWidget)
        self.label_33.setObjectName("label_33")
        self.verticalLayout_8.addWidget(self.label_33)
        self.HandleLength = QtGui.QSpinBox(self.gridLayoutWidget)
        self.HandleLength.setMaximum(10)
        self.HandleLength.setObjectName("HandleLength")
        self.verticalLayout_8.addWidget(self.HandleLength)
        self.gridLayout.addLayout(self.verticalLayout_8, 6, 1, 1, 1)
        self.verticalLayout_9 = QtGui.QVBoxLayout()
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.label_29 = QtGui.QLabel(self.gridLayoutWidget)
        self.label_29.setObjectName("label_29")
        self.verticalLayout_9.addWidget(self.label_29)
        self.LampHeight = QtGui.QSpinBox(self.gridLayoutWidget)
        self.LampHeight.setMaximum(10)
        self.LampHeight.setObjectName("LampHeight")
        self.verticalLayout_9.addWidget(self.LampHeight)
        self.gridLayout.addLayout(self.verticalLayout_9, 6, 2, 1, 1)
        self.DeskButton = QtGui.QPushButton(self.gridLayoutWidget)
        self.DeskButton.setObjectName("DeskButton")
        self.gridLayout.addWidget(self.DeskButton, 7, 0, 1, 1)
        self.ChairButton = QtGui.QPushButton(self.gridLayoutWidget)
        self.ChairButton.setObjectName("ChairButton")
        self.gridLayout.addWidget(self.ChairButton, 7, 1, 1, 1)
        self.RefrigeratorButton = QtGui.QPushButton(self.gridLayoutWidget)
        self.RefrigeratorButton.setObjectName("RefrigeratorButton")
        self.gridLayout.addWidget(self.RefrigeratorButton, 7, 2, 1, 1)
        self.verticalLayout_10 = QtGui.QVBoxLayout()
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.label_12 = QtGui.QLabel(self.gridLayoutWidget)
        self.label_12.setObjectName("label_12")
        self.verticalLayout_10.addWidget(self.label_12)
        self.DeskWidth = QtGui.QSpinBox(self.gridLayoutWidget)
        self.DeskWidth.setMaximum(10)
        self.DeskWidth.setObjectName("DeskWidth")
        self.verticalLayout_10.addWidget(self.DeskWidth)
        self.label_13 = QtGui.QLabel(self.gridLayoutWidget)
        self.label_13.setObjectName("label_13")
        self.verticalLayout_10.addWidget(self.label_13)
        self.DeskLength = QtGui.QSpinBox(self.gridLayoutWidget)
        self.DeskLength.setMaximum(10)
        self.DeskLength.setObjectName("DeskLength")
        self.verticalLayout_10.addWidget(self.DeskLength)
        self.label_14 = QtGui.QLabel(self.gridLayoutWidget)
        self.label_14.setObjectName("label_14")
        self.verticalLayout_10.addWidget(self.label_14)
        self.DeskHeight = QtGui.QSpinBox(self.gridLayoutWidget)
        self.DeskHeight.setMaximum(10)
        self.DeskHeight.setObjectName("DeskHeight")
        self.verticalLayout_10.addWidget(self.DeskHeight)
        self.gridLayout.addLayout(self.verticalLayout_10, 8, 0, 1, 1)
        self.verticalLayout_11 = QtGui.QVBoxLayout()
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.label_24 = QtGui.QLabel(self.gridLayoutWidget)
        self.label_24.setObjectName("label_24")
        self.verticalLayout_11.addWidget(self.label_24)
        self.ChairWidth = QtGui.QSpinBox(self.gridLayoutWidget)
        self.ChairWidth.setMaximum(10)
        self.ChairWidth.setObjectName("ChairWidth")
        self.verticalLayout_11.addWidget(self.ChairWidth)
        self.label_25 = QtGui.QLabel(self.gridLayoutWidget)
        self.label_25.setObjectName("label_25")
        self.verticalLayout_11.addWidget(self.label_25)
        self.ChairLength = QtGui.QSpinBox(self.gridLayoutWidget)
        self.ChairLength.setMaximum(10)
        self.ChairLength.setObjectName("ChairLength")
        self.verticalLayout_11.addWidget(self.ChairLength)
        self.label_26 = QtGui.QLabel(self.gridLayoutWidget)
        self.label_26.setObjectName("label_26")
        self.verticalLayout_11.addWidget(self.label_26)
        self.ChairHeight = QtGui.QSpinBox(self.gridLayoutWidget)
        self.ChairHeight.setMaximum(10)
        self.ChairHeight.setObjectName("ChairHeight")
        self.verticalLayout_11.addWidget(self.ChairHeight)
        self.gridLayout.addLayout(self.verticalLayout_11, 8, 1, 1, 1)
        self.verticalLayout_12 = QtGui.QVBoxLayout()
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.label_35 = QtGui.QLabel(self.gridLayoutWidget)
        self.label_35.setObjectName("label_35")
        self.verticalLayout_12.addWidget(self.label_35)
        self.RefrigeratorWidth = QtGui.QSpinBox(self.gridLayoutWidget)
        self.RefrigeratorWidth.setMaximum(10)
        self.RefrigeratorWidth.setObjectName("RefrigeratorWidth")
        self.verticalLayout_12.addWidget(self.RefrigeratorWidth)
        self.label_36 = QtGui.QLabel(self.gridLayoutWidget)
        self.label_36.setObjectName("label_36")
        self.verticalLayout_12.addWidget(self.label_36)
        self.RefrigeratorLength = QtGui.QSpinBox(self.gridLayoutWidget)
        self.RefrigeratorLength.setMaximum(10)
        self.RefrigeratorLength.setObjectName("RefrigeratorLength")
        self.verticalLayout_12.addWidget(self.RefrigeratorLength)
        self.label_37 = QtGui.QLabel(self.gridLayoutWidget)
        self.label_37.setObjectName("label_37")
        self.verticalLayout_12.addWidget(self.label_37)
        self.RefrigeratorHeight = QtGui.QSpinBox(self.gridLayoutWidget)
        self.RefrigeratorHeight.setMaximum(10)
        self.RefrigeratorHeight.setObjectName("RefrigeratorHeight")
        self.verticalLayout_12.addWidget(self.RefrigeratorHeight)
        self.gridLayout.addLayout(self.verticalLayout_12, 8, 2, 1, 1)
        self.OlinChairButton = QtGui.QPushButton(self.gridLayoutWidget)
        self.OlinChairButton.setObjectName("OlinChairButton")
        self.gridLayout.addWidget(self.OlinChairButton, 9, 0, 1, 1)
        self.MaterialsLabel = QtGui.QLabel(self.gridLayoutWidget)
        self.MaterialsLabel.setObjectName("MaterialsLabel")
        self.gridLayout.addWidget(self.MaterialsLabel, 10, 1, 1, 1)
        self.MaterialBox = QtGui.QComboBox(self.gridLayoutWidget)
        self.MaterialBox.setObjectName("MaterialBox")
        self.MaterialBox.addItem("")
        self.MaterialBox.addItem("")
        self.MaterialBox.addItem("")
        self.MaterialBox.addItem("")
        self.MaterialBox.addItem("")
        self.MaterialBox.addItem("")
        self.MaterialBox.addItem("")
        self.MaterialBox.addItem("")
        self.MaterialBox.addItem("")
        self.MaterialBox.addItem("")
        self.MaterialBox.addItem("")
        self.MaterialBox.addItem("")
        self.MaterialBox.addItem("")
        self.MaterialBox.addItem("")
        self.MaterialBox.addItem("")
        self.gridLayout.addWidget(self.MaterialBox, 10, 2, 1, 1)
        self.widget = QtGui.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(0, 0, 2, 2))
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtGui.QHBoxLayout(self.widget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 25))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "MainWindow", None, QtGui.QApplication.UnicodeUTF8))
        self.Furniture_Label.setText(QtGui.QApplication.translate("MainWindow", "Furniture", None, QtGui.QApplication.UnicodeUTF8))
        self.ElectronicsLabel.setText(QtGui.QApplication.translate("MainWindow", "Electronics", None, QtGui.QApplication.UnicodeUTF8))
        self.BedButton.setText(QtGui.QApplication.translate("MainWindow", "Bed", None, QtGui.QApplication.UnicodeUTF8))
        self.PosterButton.setText(QtGui.QApplication.translate("MainWindow", "Poster", None, QtGui.QApplication.UnicodeUTF8))
        self.MicrowaveButton.setText(QtGui.QApplication.translate("MainWindow", "Microwave", None, QtGui.QApplication.UnicodeUTF8))
        self.label_30.setText(QtGui.QApplication.translate("MainWindow", "Width", None, QtGui.QApplication.UnicodeUTF8))
        self.label_31.setText(QtGui.QApplication.translate("MainWindow", "Length", None, QtGui.QApplication.UnicodeUTF8))
        self.label_32.setText(QtGui.QApplication.translate("MainWindow", "Height", None, QtGui.QApplication.UnicodeUTF8))
        self.label_27.setText(QtGui.QApplication.translate("MainWindow", "Width", None, QtGui.QApplication.UnicodeUTF8))
        self.label_28.setText(QtGui.QApplication.translate("MainWindow", "Length", None, QtGui.QApplication.UnicodeUTF8))
        self.label_18.setText(QtGui.QApplication.translate("MainWindow", "Width", None, QtGui.QApplication.UnicodeUTF8))
        self.label_19.setText(QtGui.QApplication.translate("MainWindow", "Length", None, QtGui.QApplication.UnicodeUTF8))
        self.label_20.setText(QtGui.QApplication.translate("MainWindow", "Height", None, QtGui.QApplication.UnicodeUTF8))
        self.BookshelfButton.setText(QtGui.QApplication.translate("MainWindow", "Bookshelf", None, QtGui.QApplication.UnicodeUTF8))
        self.TableButton.setText(QtGui.QApplication.translate("MainWindow", "Table", None, QtGui.QApplication.UnicodeUTF8))
        self.WallLightButton.setText(QtGui.QApplication.translate("MainWindow", "Wall Light", None, QtGui.QApplication.UnicodeUTF8))
        self.label_9.setText(QtGui.QApplication.translate("MainWindow", "Width", None, QtGui.QApplication.UnicodeUTF8))
        self.label_10.setText(QtGui.QApplication.translate("MainWindow", "Length", None, QtGui.QApplication.UnicodeUTF8))
        self.label_11.setText(QtGui.QApplication.translate("MainWindow", "Height", None, QtGui.QApplication.UnicodeUTF8))
        self.label_21.setText(QtGui.QApplication.translate("MainWindow", "Width", None, QtGui.QApplication.UnicodeUTF8))
        self.label_22.setText(QtGui.QApplication.translate("MainWindow", "Length", None, QtGui.QApplication.UnicodeUTF8))
        self.label_23.setText(QtGui.QApplication.translate("MainWindow", "Height", None, QtGui.QApplication.UnicodeUTF8))
        self.label_34.setText(QtGui.QApplication.translate("MainWindow", "Height", None, QtGui.QApplication.UnicodeUTF8))
        self.ClosetButton.setText(QtGui.QApplication.translate("MainWindow", "Closet", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("MainWindow", "Width", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("MainWindow", "Length", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("MainWindow", "Height", None, QtGui.QApplication.UnicodeUTF8))
        self.HandleButton.setText(QtGui.QApplication.translate("MainWindow", "Handle", None, QtGui.QApplication.UnicodeUTF8))
        self.LampButton.setText(QtGui.QApplication.translate("MainWindow", "Lamp", None, QtGui.QApplication.UnicodeUTF8))
        self.label_33.setText(QtGui.QApplication.translate("MainWindow", "Length", None, QtGui.QApplication.UnicodeUTF8))
        self.label_29.setText(QtGui.QApplication.translate("MainWindow", "Height", None, QtGui.QApplication.UnicodeUTF8))
        self.DeskButton.setText(QtGui.QApplication.translate("MainWindow", "Desk", None, QtGui.QApplication.UnicodeUTF8))
        self.ChairButton.setText(QtGui.QApplication.translate("MainWindow", "Chair", None, QtGui.QApplication.UnicodeUTF8))
        self.RefrigeratorButton.setText(QtGui.QApplication.translate("MainWindow", "Refrigerator", None, QtGui.QApplication.UnicodeUTF8))
        self.label_12.setText(QtGui.QApplication.translate("MainWindow", "Width", None, QtGui.QApplication.UnicodeUTF8))
        self.label_13.setText(QtGui.QApplication.translate("MainWindow", "Length", None, QtGui.QApplication.UnicodeUTF8))
        self.label_14.setText(QtGui.QApplication.translate("MainWindow", "Height", None, QtGui.QApplication.UnicodeUTF8))
        self.label_24.setText(QtGui.QApplication.translate("MainWindow", "Width", None, QtGui.QApplication.UnicodeUTF8))
        self.label_25.setText(QtGui.QApplication.translate("MainWindow", "Length", None, QtGui.QApplication.UnicodeUTF8))
        self.label_26.setText(QtGui.QApplication.translate("MainWindow", "Height", None, QtGui.QApplication.UnicodeUTF8))
        self.label_35.setText(QtGui.QApplication.translate("MainWindow", "Width", None, QtGui.QApplication.UnicodeUTF8))
        self.label_36.setText(QtGui.QApplication.translate("MainWindow", "Length", None, QtGui.QApplication.UnicodeUTF8))
        self.label_37.setText(QtGui.QApplication.translate("MainWindow", "Height", None, QtGui.QApplication.UnicodeUTF8))
        self.OlinChairButton.setText(QtGui.QApplication.translate("MainWindow", "Olin Chair", None, QtGui.QApplication.UnicodeUTF8))
        self.MaterialsLabel.setText(QtGui.QApplication.translate("MainWindow", "Materials", None, QtGui.QApplication.UnicodeUTF8))
        self.MaterialBox.setItemText(0, QtGui.QApplication.translate("MainWindow", "Default", None, QtGui.QApplication.UnicodeUTF8))
        self.MaterialBox.setItemText(1, QtGui.QApplication.translate("MainWindow", "Plastic", None, QtGui.QApplication.UnicodeUTF8))
        self.MaterialBox.setItemText(2, QtGui.QApplication.translate("MainWindow", "Earth", None, QtGui.QApplication.UnicodeUTF8))
        self.MaterialBox.setItemText(3, QtGui.QApplication.translate("MainWindow", "Diffuse", None, QtGui.QApplication.UnicodeUTF8))
        self.MaterialBox.setItemText(4, QtGui.QApplication.translate("MainWindow", "Emissive", None, QtGui.QApplication.UnicodeUTF8))
        self.MaterialBox.setItemText(5, QtGui.QApplication.translate("MainWindow", "Unshaded", None, QtGui.QApplication.UnicodeUTF8))
        self.MaterialBox.setItemText(6, QtGui.QApplication.translate("MainWindow", "Shiny", None, QtGui.QApplication.UnicodeUTF8))
        self.MaterialBox.setItemText(7, QtGui.QApplication.translate("MainWindow", "Chrome", None, QtGui.QApplication.UnicodeUTF8))
        self.MaterialBox.setItemText(8, QtGui.QApplication.translate("MainWindow", "Blazed", None, QtGui.QApplication.UnicodeUTF8))
        self.MaterialBox.setItemText(9, QtGui.QApplication.translate("MainWindow", "Earth with Clouds", None, QtGui.QApplication.UnicodeUTF8))
        self.MaterialBox.setItemText(10, QtGui.QApplication.translate("MainWindow", "Brick", None, QtGui.QApplication.UnicodeUTF8))
        self.MaterialBox.setItemText(11, QtGui.QApplication.translate("MainWindow", "Silver", None, QtGui.QApplication.UnicodeUTF8))
        self.MaterialBox.setItemText(12, QtGui.QApplication.translate("MainWindow", "Wood", None, QtGui.QApplication.UnicodeUTF8))
        self.MaterialBox.setItemText(13, QtGui.QApplication.translate("MainWindow", "Rough", None, QtGui.QApplication.UnicodeUTF8))
        self.MaterialBox.setItemText(14, QtGui.QApplication.translate("MainWindow", "Marble", None, QtGui.QApplication.UnicodeUTF8))

