# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import QAbstractItemView
from PyQt5.QtWidgets import QHBoxLayout
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QTableView
from PyQt5.QtWidgets import QVBoxLayout
from PyQt5.QtWidgets import QWidget

class Window(QMainWindow):
   def __init__(self, parent=None):

      super().__init__(parent)
      self.setWindowTitle("TContacts - v0.0.2")
      self.resize(550, 250)
      self.centralWidget = QWidget()
      self.setCentralWidget(self.centralWidget)
      self.layout = QHBoxLayout()
      self.centralWidget.setLayout(self.layout)

      self.UISetup()


   def UISetup(self):
      self.table = QTableView()
      self.table.setSelectionBehavior(QAbstractItemView.SelectRows)
      self.table.resizeColumnsToContents()

      self.addButton = QPushButton("Add")
      self.deleteButton = QPushButton("Delete")
      self.clearAllButton = QPushButton("Clear")

      layout = QVBoxLayout()
      layout.addWidget(self.addButton)
      layout.addWidget(self.deleteButton)
      layout.addStretch()
      layout.addWidget(self.clearAllButton)
      self.layout.addWidget(self.table)
      self.layout.addLayout(layout)
