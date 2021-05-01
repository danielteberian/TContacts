# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import QHBoxLayout
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QWidget

class Window(QMainWindow):
   def __init__(self, parent=None):
      super().__init__(parent)
      self.setWindowTitle("TContacts - v0.0.1")
      self.resize(550, 250)
      self.centralWidget = QWidget()
      self.setCentralWidget(self.centralWidget)
      self.layout = QHBoxLayout()
      self.centralWidget.setLayout(self.layout)

