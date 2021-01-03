from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

import pyqtgraph as pg


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
        self.section_1_dropdown_2 = QComboBox()

        self.section_2_label = QLabel("Graph-2")
        self.section_2_dropdown_1 = QComboBox()
        self.section_2_dropdown_2 = QComboBox()

        
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
        #self.curve2.setPen('#0096ff')  # Blue pen

        # THIRD PLOT
        plotwin.nextRow()
        self.p3 = plotwin.addPlot()
        self.curve3 = self.p3.plot()
        #self.curve3.setPen('#fc02f8')  # Pink pen

        #-----------------------ADD WIDGET TO INPUT SECTION LAYOUT
        self.input_section_layout.addWidget(self.section_1_label, 0, 0)
        self.input_section_layout.addWidget(self.section_1_dropdown_1, 0, 1)
        self.input_section_layout.addWidget(self.section_1_dropdown_2, 0, 2)

        self.input_section_layout.addWidget(self.section_2_label, 1, 0 )
        self.input_section_layout.addWidget(self.section_2_dropdown_1, 1, 1)
        self.input_section_layout.addWidget(self.section_2_dropdown_2, 1, 2)

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


