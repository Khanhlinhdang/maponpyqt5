import sys
from PyQt5 import QtWidgets
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QWidget, QMessageBox
from pyqtlet import L, MapWidget
from PyQt5.uic import loadUi

class MapWindow(QWidget):
    def __init__(self):
        # Setting up the widgets and layout
        super( MapWindow, self).__init__()
        loadUi("gui_.ui", self)

        self.mapWidget = MapWidget()
        self.QVBoxLayout.addWidget(self.mapWidget)
        self.setLayout(self.QVBoxLayout)
        self.map = L.map(self.mapWidget)
        self.map.setView([20.5, 105.5], 4)
        L.tileLayer('https://tile.openstreetmap.org/{z}/{x}/{y}.png').addTo(self.map) #
        self.layerGroup = L.layerGroup()
        self.map.addLayer(self.layerGroup)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainwindow = MapWindow()
    widget = QtWidgets.QStackedWidget()
    widget.addWidget(mainwindow)
    widget.setWindowIcon(QIcon("./tich.png"))
    widget.setWindowTitle('openstreetmap')
    widget.setFixedWidth(1400)
    widget.setFixedHeight(800)
    widget.show()
    sys.exit(app.exec_())