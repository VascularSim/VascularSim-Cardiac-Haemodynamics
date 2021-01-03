from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

import pyqtgraph as pg
import numpy as np


class Window(object):

    def __init__(self, MainWindow):
        super().__init__()
        self.MainWindow = MainWindow
        self.centralwidget = QWidget(MainWindow)
        
        self.menubar = QMenuBar(self.MainWindow)

        # LAYOUTSs
        self.mainlayout = QGridLayout(self.centralwidget)

        self.input_section_layout = QGridLayout()
        self.section_1_label = QLabel("Graph-1")
        self.section_1_dropdown_1 = QComboBox()

        self.section_2_label = QLabel("Graph-2")
        self.section_2_dropdown_1 = QComboBox()

        
        self.setupUi()

    def setupUi(self):
        # MAINWINDOW
        self.MainWindow.setObjectName("MainWindow")
        self.MainWindow.setWindowTitle("VascularSim - Cardiac Haemodynamics")
        self.MainWindow.setWindowIcon(QIcon('./VascularSim.ico'))
        self.MainWindow.resize(1200,650)
        self.MainWindow.setMaximumHeight(650)
        self.MainWindow.setMaximumWidth(1200)
        
        # CENTRAL WIDGET
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.MainWindow.setCentralWidget(self.centralwidget)


        
        # ==================Graph Layout            
        pg.setConfigOptions(antialias= True, background=QColor(255,255,255,255))
        plotwin = pg.GraphicsLayoutWidget(show=True)
        plotwin.setContentsMargins(0, 0, 0, 0)

        # FIRST PLOT
        self.p1 = plotwin.addPlot()
        self.curve1 = self.p1.plot()
        self.curve1.setPen('g')  # Green pen

        # SECOND PLOT
        plotwin.nextRow()
        self.p2 = plotwin.addPlot()
        self.curve2 = self.p2.plot()
        self.curve2.setPen('#0096ff')  # Blue pen

        # THIRD PLOT
        plotwin.nextRow()
        self.p3 = plotwin.addPlot()
        self.curve3 = self.p3.plot()
        self.curve4 = self.p3.plot()
        self.curve3.setPen('g')  # green pen
        self.curve4.setPen('#0096ff')  # blue pen

        #COMBOBOX graph 1
        for i in range(5):
            self.section_1_dropdown_1.addItem("")
        self.section_1_dropdown_1.setItemText(0,"Select section")
        self.section_1_dropdown_1.setItemText(1,"Left atrium")
        self.section_1_dropdown_1.setItemText(2,"Left ventricle")
        self.section_1_dropdown_1.setItemText(3,"Right atrium")
        self.section_1_dropdown_1.setItemText(4,"Right ventricle")
        self.section_1_dropdown_1.setItemText(5,"Aorta")

        self.section_1_dropdown_1.currentIndexChanged.connect(self.grpah1Plot)

        #COMBOBOX graph 1
        for i in range(5):
            self.section_2_dropdown_1.addItem("")
        self.section_2_dropdown_1.setItemText(0,"Select section")
        self.section_2_dropdown_1.setItemText(1,"Left atrium")
        self.section_2_dropdown_1.setItemText(2,"Left ventricle")
        self.section_2_dropdown_1.setItemText(3,"Right atrium")
        self.section_2_dropdown_1.setItemText(4,"Right ventricle")
        self.section_2_dropdown_1.setItemText(5,"Aorta")

        self.section_2_dropdown_1.currentIndexChanged.connect(self.grpah2Plot)

        #-----------------------ADD WIDGET TO INPUT SECTION LAYOUT
        self.input_section_layout.addWidget(self.section_1_label, 0, 0)
        self.input_section_layout.addWidget(self.section_1_dropdown_1, 0, 1)
        
        self.input_section_layout.addWidget(self.section_2_label, 1, 0 )
        self.input_section_layout.addWidget(self.section_2_dropdown_1, 1, 1)

        #-----------------------ADD WIDGET TO MAINLAYOUT
        self.mainlayout.addLayout(self.input_section_layout, 0, 0, 1, 1)
        self.mainlayout.addWidget(plotwin, 0, 1, 1, 1)



        # ______________________________MENUBAR _____________________________
        
        # ============MENU BAR
        self.MainWindow.setMenuBar(self.menubar)

        # ============MENU FILE
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setTitle("File")

        self.actionQuit = QAction(self.MainWindow)
        self.actionQuit.setText("Quit")
        
        self.menuFile.addAction(self.actionQuit)
        self.actionQuit.triggered.connect(self.exit)

        self.menubar.addAction(self.menuFile.menuAction())

    def grpah1Plot(self):
        graph1Index = int(self.section_1_dropdown_1.currentIndex())
        if graph1Index == 0:
            self.curve1.setData()
        if graph1Index == 1:
            la = np.genfromtxt("LA.txt")
            la = la[0:15000]
            self.curve1.setData(la)
            self.graphOverlay()
        if graph1Index == 2:
            lv = np.genfromtxt("LV.txt")
            lv = lv[0:15000]
            self.curve1.setData(lv)
            self.graphOverlay()
        if graph1Index == 3:
            ra = np.genfromtxt("RA.txt")
            ra = ra[0:15000]
            self.curve1.setData(ra)
            self.graphOverlay()
        if graph1Index == 4:
            rv = np.genfromtxt("RV.txt")
            rv = rv[0:15000]
            self.curve1.setData(rv)
            self.graphOverlay()
        if graph1Index == 5:
            aorta = np.genfromtxt("aorta.txt")
            aorta = aorta[0:15000]
            self.curve1.setData(aorta)
            self.graphOverlay()

    def grpah2Plot(self):
        graph2Index = int(self.section_2_dropdown_1.currentIndex())
        if graph2Index == 0:
            self.curve2.setData()
        if graph2Index == 1:
            la = np.genfromtxt("LA.txt")
            la = la[0:15000]
            self.curve2.setData(la)
            self.graphOverlay()
        if graph2Index == 2:
            lv = np.genfromtxt("LV.txt")
            lv = lv[0:15000]
            self.curve2.setData(lv)
            self.graphOverlay()
        if graph2Index == 3:
            ra = np.genfromtxt("RA.txt")
            ra = ra[0:15000]
            self.curve2.setData(ra)
            self.graphOverlay()
        if graph2Index == 4:
            rv = np.genfromtxt("RV.txt")
            rv = rv[0:15000]
            self.curve2.setData(rv)
            self.graphOverlay()
        if graph2Index == 5:
            aorta = np.genfromtxt("aorta.txt")
            aorta = aorta[0:15000]
            self.curve2.setData(aorta)
            self.graphOverlay()

    def graphOverlay(self):
        g1 = int(self.section_1_dropdown_1.currentIndex())
        g2 = int(self.section_2_dropdown_1.currentIndex())

        if (g1 != 0) and (g2 != 0):
            if g1 == 0:
                self.curve3.setData()
            if g1 == 1:
                la = np.genfromtxt("LA.txt")
                la = la[0:15000]
                self.curve3.setData(la)
            if g1 == 2:
                lv = np.genfromtxt("LV.txt")
                lv = lv[0:15000]
                self.curve3.setData(lv)
            if g1 == 3:
                ra = np.genfromtxt("RA.txt")
                ra = ra[0:15000]
                self.curve3.setData(ra)
            if g1 == 4:
                rv = np.genfromtxt("RV.txt")
                rv = rv[0:15000]
                self.curve3.setData(rv)
            if g1 == 5:
                aorta = np.genfromtxt("aorta.txt")
                aorta = aorta[0:15000]
                self.curve3.setData(aorta)

            if g2 == 0:
                self.curve4.setData()
            if g2 == 1:
                la = np.genfromtxt("LA.txt")
                la = la[0:15000]
                self.curve4.setData(la)
            if g2 == 2:
                lv = np.genfromtxt("LV.txt")
                lv = lv[0:15000]
                self.curve4.setData(lv)
            if g2 == 3:
                ra = np.genfromtxt("RA.txt")
                ra = ra[0:15000]
                self.curve4.setData(ra)
            if g2 == 4:
                rv = np.genfromtxt("RV.txt")
                rv = rv[0:15000]
                self.curve4.setData(rv)
            if g2 == 5:
                aorta = np.genfromtxt("aorta.txt")
                aorta = aorta[0:15000]
                self.curve4.setData(aorta)
        else:
            print("one is zero")

    def stop(self):
        self.timer.stop()

    def alert(self, msg):
        alert = QMessageBox()
        alert.setWindowTitle("Alert!!")
        alert.setWindowFlag(Qt.AA_EnableHighDpiScaling | Qt.FramelessWindowHint)
        alert.setStyleSheet("background-color: rgb(60, 60, 60);\n" "color: rgb(240, 240, 240);\n")
        alert.setText(msg)
        alert.exec_()

    def exit(self):
        sys.exit()

if __name__ == "__main__":
    import os
    import sys
    
    app = QApplication(sys.argv)    
    wid = QMainWindow()
    ui = Window(wid)
    wid.show()
    sys.exit(app.exec())    


