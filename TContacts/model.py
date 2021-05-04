from PyQt5.QtCore import Qt
from PyQt5.QtSql import QSqlTableModel

class ContactsModel:
   def __init__(self):
      self.model = self._createModel()

   @staticmethod
   def _createModel():
      tableModel = QSqlTableModel()
      tableModel.setTable("CONTACTS")
      tableModel.setEditStrategy(QSqlTableModel.OnFieldChange)
      tableModel.select()
      headers = ("ID", "NAME", "TITLE", "EMAIL")
      for columnIndex, header in enumerate(headers):
         tableModel.setHeaderData(columnIndex, Qt.Horizontal, header)
      return tableModel
