# -*- coding: utf-8 -*-
from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8

    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)


class UserSettingsDialogUi(object):
    """ User interface definition """
    def setupUi(self, UserSettingsWindow):
        UserSettingsWindow.setObjectName(_fromUtf8("UserSettingsWindow"))
        UserSettingsWindow.resize(600, 300)
        UserSettingsWindow.setMinimumSize(600, 300)
        UserSettingsWindow.setMaximumSize(600, 300)
        self.verticalLayout = QtGui.QVBoxLayout(UserSettingsWindow)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.tabWidget = QtGui.QTabWidget(UserSettingsWindow)
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.generalTab = QtGui.QWidget()
        self.generalTab.setObjectName(_fromUtf8("generalTab"))
        self.formLayoutWidget_2 = QtGui.QWidget(self.generalTab)
        self.formLayoutWidget_2.setGeometry(QtCore.QRect(290, 10, 271, 180))
        self.formLayoutWidget_2.setObjectName(_fromUtf8("formLayoutWidget_2"))
        self.generalTabRight = QtGui.QFormLayout(self.formLayoutWidget_2)
        self.generalTabRight.setMargin(0)
        self.generalTabRight.setObjectName(_fromUtf8("generalTabRight"))
        self.formLayoutWidget_5 = QtGui.QWidget(self.generalTab)
        self.formLayoutWidget_5.setGeometry(QtCore.QRect(10, 10, 271, 180))
        self.formLayoutWidget_5.setObjectName(_fromUtf8("formLayoutWidget_5"))
        self.generalTabLeft = QtGui.QFormLayout(self.formLayoutWidget_5)
        self.generalTabLeft.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.generalTabLeft.setMargin(0)
        self.generalTabLeft.setObjectName(_fromUtf8("generalTabLeft"))
        self.langLabel = QtGui.QLabel(self.formLayoutWidget_5)
        self.langLabel.setObjectName(_fromUtf8("langLabel"))
        self.generalTabLeft.setWidget(0, QtGui.QFormLayout.LabelRole, self.langLabel)
        self.comboBox = QtGui.QComboBox(self.formLayoutWidget_5)
        self.comboBox.setObjectName(_fromUtf8("comboBox"))
        self.generalTabLeft.setWidget(0, QtGui.QFormLayout.FieldRole, self.comboBox)
        self.lineEdit = QtGui.QLineEdit(self.formLayoutWidget_5)
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.generalTabLeft.setWidget(2, QtGui.QFormLayout.FieldRole, self.lineEdit)
        self.masterPasswordcheckBox = QtGui.QCheckBox(self.formLayoutWidget_5)
        self.masterPasswordcheckBox.setObjectName(_fromUtf8("masterPasswordcheckBox"))
        self.generalTabLeft.setWidget(2, QtGui.QFormLayout.LabelRole, self.masterPasswordcheckBox)
        self.resetButton = QtGui.QPushButton(self.formLayoutWidget_5)
        self.resetButton.setObjectName(_fromUtf8("resetButton"))
        self.generalTabLeft.setWidget(3, QtGui.QFormLayout.FieldRole, self.resetButton)
        self.tabWidget.addTab(self.generalTab, _fromUtf8(""))
        self.localStorageTab = QtGui.QWidget()
        self.localStorageTab.setObjectName(_fromUtf8("localStorageTab"))
        self.localStorageTableView = QtGui.QTableView(self.localStorageTab)
        self.localStorageTableView.setGeometry(QtCore.QRect(0, 40, 571, 180))
        self.localStorageTableView.setObjectName(_fromUtf8("localStorageTableView"))
        self.formLayoutWidget_3 = QtGui.QWidget(self.localStorageTab)
        self.formLayoutWidget_3.setGeometry(QtCore.QRect(0, 10, 171, 25))
        self.formLayoutWidget_3.setObjectName(_fromUtf8("formLayoutWidget_3"))
        self.localStorageLayout = QtGui.QFormLayout(self.formLayoutWidget_3)
        self.localStorageLayout.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.localStorageLayout.setMargin(0)
        self.localStorageLayout.setObjectName(_fromUtf8("localStorageLayout"))
        self.addLocalStorageButton = QtGui.QPushButton(self.formLayoutWidget_3)
        self.addLocalStorageButton.setObjectName(_fromUtf8("addLocalStorageButton"))
        self.localStorageLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.addLocalStorageButton)
        self.deleteLocalStorageButton = QtGui.QPushButton(self.formLayoutWidget_3)
        self.deleteLocalStorageButton.setObjectName(_fromUtf8("deleteLocalStorageButton"))
        self.localStorageLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.deleteLocalStorageButton)
        self.tabWidget.addTab(self.localStorageTab, _fromUtf8(""))
        self.FTPStorageTab = QtGui.QWidget()
        self.FTPStorageTab.setObjectName(_fromUtf8("FTPStorageTab"))
        self.FTPStorageTableView = QtGui.QTableView(self.FTPStorageTab)
        self.FTPStorageTableView.setGeometry(QtCore.QRect(0, 40, 571, 180))
        self.FTPStorageTableView.setObjectName(_fromUtf8("FTPStorageTableView"))
        self.formLayoutWidget_4 = QtGui.QWidget(self.FTPStorageTab)
        self.formLayoutWidget_4.setGeometry(QtCore.QRect(0, 10, 161, 25))
        self.formLayoutWidget_4.setObjectName(_fromUtf8("formLayoutWidget_4"))
        self.FTPStorageLayout = QtGui.QFormLayout(self.formLayoutWidget_4)
        self.FTPStorageLayout.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.FTPStorageLayout.setMargin(0)
        self.FTPStorageLayout.setObjectName(_fromUtf8("FTPStorageLayout"))
        self.addFTPStorageButton = QtGui.QPushButton(self.formLayoutWidget_4)
        self.addFTPStorageButton.setObjectName(_fromUtf8("addFTPStorageButton"))
        self.FTPStorageLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.addFTPStorageButton)
        self.deleteFTPStorageButton = QtGui.QPushButton(self.formLayoutWidget_4)
        self.deleteFTPStorageButton.setObjectName(_fromUtf8("deleteFTPStorageButton"))
        self.FTPStorageLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.deleteFTPStorageButton)
        self.tabWidget.addTab(self.FTPStorageTab, _fromUtf8(""))
        self.gridLayout.addWidget(self.tabWidget, 0, 0, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.blanklabel1 = QtGui.QLabel(UserSettingsWindow)
        self.blanklabel1.setText(_fromUtf8(""))
        self.blanklabel1.setObjectName(_fromUtf8("blanklabel1"))
        self.horizontalLayout.addWidget(self.blanklabel1)
        self.blanklabel2 = QtGui.QLabel(UserSettingsWindow)
        self.blanklabel2.setText(_fromUtf8(""))
        self.blanklabel2.setObjectName(_fromUtf8("blanklabel2"))
        self.horizontalLayout.addWidget(self.blanklabel2)
        self.OKButton = QtGui.QPushButton(UserSettingsWindow)
        self.OKButton.setObjectName(_fromUtf8("OKButton"))
        self.horizontalLayout.addWidget(self.OKButton)
        self.CancelButton = QtGui.QPushButton(UserSettingsWindow)
        self.CancelButton.setObjectName(_fromUtf8("CancelButton"))
        self.horizontalLayout.addWidget(self.CancelButton)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(UserSettingsWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(UserSettingsWindow)

    def retranslateUi(self, UserSettingsWindow):
        UserSettingsWindow.setWindowTitle(_translate("UserSettingsWindow", "Settings", None))
        self.langLabel.setText(_translate("UserSettingsWindow", "Language", None))
        self.masterPasswordcheckBox.setText(_translate("UserSettingsWindow", "use master passord", None))
        self.resetButton.setText(_translate("UserSettingsWindow", "Reset to defaults", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.generalTab),
                                  _translate("UserSettingsWindow", "General", None))
        self.addLocalStorageButton.setText(_translate("UserSettingsWindow", "Add", None))
        self.deleteLocalStorageButton.setText(_translate("UserSettingsWindow", "Delete", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.localStorageTab),
                                  _translate("UserSettingsWindow", "Local storage", None))
        self.addFTPStorageButton.setText(_translate("UserSettingsWindow", "Add", None))
        self.deleteFTPStorageButton.setText(_translate("UserSettingsWindow", "Delete", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.FTPStorageTab),
                                  _translate("UserSettingsWindow", "FTP storage", None))
        self.OKButton.setText(_translate("UserSettingsWindow", "Save", None))
        self.CancelButton.setText(_translate("UserSettingsWindow", "Cancel", None))


class SettingsTableModel(QtCore.QAbstractTableModel):
    def __init__(self, databases, column_structure, parent=None):
        QtCore.QAbstractTableModel.__init__(self, parent)
        self.databases = databases
        self.column_structure = column_structure

    def rowCount(self, parent):
        return len(self.databases)

    def columnCount(self, parent):
        if len(self.databases):
            return len(self.databases[0].keys())
        else:
            return len(self.column_structure)

    def flags(self, index):
        return QtCore.Qt.ItemIsEditable | QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsSelectable

    def data(self, index, role):

        if role == QtCore.Qt.DisplayRole:
            row = index.row()
            column = index.column()
            return self.databases[row].values()[column]

        if role == QtCore.Qt.EditRole:
            row = index.row()
            column = index.column()
            return self.databases[row].values()[column]

    def setData(self, index, value, role=QtCore.Qt.EditRole):
        if role == QtCore.Qt.EditRole:
            row = index.row()
            column = index.column()
            self.databases[row][self.databases[row].keys()[column]] = unicode(value.toPyObject())
            if column == 0:
               self.databases[row][self.databases[row].keys()[1]] = unicode(value.toPyObject()).lower()+'.db'
            self.dataChanged.emit(index, index)
            return True
        return False

    def headerData(self, section, orientation, role):

        if role == QtCore.Qt.DisplayRole:
            if orientation == QtCore.Qt.Horizontal:
                if len(self.databases):
                    return self.databases[0].keys()[section]
                else:
                    return self.column_structure.keys()[section]
            else:
                return QtCore.QString("%1").arg(section + 1)

    def insertRow(self, int_row, parent=QtCore.QAbstractItemModel):
        self.beginInsertRows(parent, 1, 1)
        self.databases.append(self.column_structure)
        self.endInsertRows()

        return True

    def removeRow(self, int_row, parent):
        self.beginRemoveRows(parent, int_row, int_row)
        del self.databases[int_row]
        self.endRemoveRows()

        return True

    def insertColumns(self, position, columns, parent=QtCore.QModelIndex()):
        self.beginInsertColumns(parent, position, position + columns - 1)

        rowCount = len(self.databases)

        for i in range(columns):
            for j in range(rowCount):
                self.databases[j].insert(position, QtGui.QColor("#000000"))

        self.endInsertColumns()

        return True


class UserSettingsDialog(QtGui.QDialog):

    def __init__(self, usersett):
        from collections import OrderedDict

        QtGui.QWidget.__init__(self, None)
        self.ui = UserSettingsDialogUi()
        self.ui.setupUi(self)
        self.usersett = usersett

        # dividing list of databases into local and FTP databases
        # to display them in separate tables
        localdatabases_columns = OrderedDict([("Name", ""),
                                              ("Path", ""),
                                              ("Password", "")])

        ftpdatabases_columns = OrderedDict([("Name", ""),
                                            ("Path", ""),
                                            ("Password", ""),
                                            ("FTP_Server", ""),
                                            ("FTP_Port", ""),
                                            ("FTP_User", ""),
                                            ("FTP_Password", "")])
        localdatabases = []
        for x in self.usersett.databases:
            if x["Type"] == "local":
                d = OrderedDict([("Name", x["Name"]),
                                 ("Path", x["Path"]),
                                 ("Password", x["Password"])])
                localdatabases.append(d)

        self.ui.localStorageTableView.setModel(SettingsTableModel(localdatabases, localdatabases_columns))

        ftpdatabases = []
        for x in self.usersett.databases:
            if x["Type"] == "ftp":
                d = OrderedDict([("Name", x["Name"]),
                                 ("Path", x["Path"]),
                                 ("Password", x["Password"]),
                                 ("FTP_Server", x["Properties"]["FTP_Server"]),
                                 ("FTP_Port", x["Properties"]["FTP_Port"]),
                                 ("FTP_User", x["Properties"]["FTP_User"]),
                                 ("FTP_Password", x["Properties"]["FTP_Password"])])

                ftpdatabases.append(d)

        self.ui.FTPStorageTableView.setModel(SettingsTableModel(ftpdatabases, ftpdatabases_columns))

        self.ui.OKButton.clicked.connect(self.save)
        self.ui.CancelButton.clicked.connect(self.cancel)
        self.ui.deleteLocalStorageButton.clicked.connect(self.removeLocalStorageRow)
        self.ui.addLocalStorageButton.clicked.connect(self.addLocalStorageRow)
        self.ui.deleteFTPStorageButton.clicked.connect(self.removeFTPStorageRow)
        self.ui.addFTPStorageButton.clicked.connect(self.addFTPStorageRow)
        self.ui.resetButton.clicked.connect(self.resetToDefaults)

    def save(self):
        self.usersett.databases = self.ui.localStorageTableView.model().databases
        self.usersett.databases = []
        localdatabases = [dict(Name=x["Name"],
                               Type="local",
                               Properties={},
                               Path=x["Path"],
                               Password=x["Password"])
                          for x in self.ui.localStorageTableView.model().databases]

        ftpdatabases = [dict(Name=x["Name"],
                             Type="ftp",
                             Properties=dict(FTP_Server=x["FTP_Server"],
                                             FTP_Port=int(x["FTP_Port"]),
                                             FTP_User=x["FTP_User"],
                                             FTP_Password=x["FTP_Password"]),
                             Path=x["Path"],
                             Password=x["Password"])
                        for x in self.ui.FTPStorageTableView.model().databases]

        self.usersett.databases = localdatabases + ftpdatabases

        self.usersett.save_config()
        self.close()

    def cancel(self):
        self.close()

    def addLocalStorageRow(self):
        selected_index = self.ui.localStorageTableView.model().index(len(self.usersett.databases), 0)

        self.ui.localStorageTableView.model().insertRow(len(self.usersett.databases), selected_index)

    def removeLocalStorageRow(self):
        selected_index = self.ui.localStorageTableView.selectionModel().selectedIndexes()[0]

        self.ui.localStorageTableView.model().removeRow(selected_index.row(), selected_index.parent())

    def addFTPStorageRow(self):
        selected_index = self.ui.FTPStorageTableView.model().index(len(self.usersett.databases), 0)

        self.ui.FTPStorageTableView.model().insertRow(len(self.usersett.databases), selected_index)

    def removeFTPStorageRow(self):
        selected_index = self.ui.FTPStorageTableView.selectionModel().selectedIndexes()[0]

        self.ui.FTPStorageTableView.model().removeRow(selected_index.row(), selected_index.parent())

    def resetToDefaults(self):
        reply = QtGui.QMessageBox.question(self, 'Message', "Do ypu want to reset config?",
                                                   QtGui.QMessageBox.Yes | QtGui.QMessageBox.No,
                                                   QtGui.QMessageBox.No)
        if reply == QtGui.QMessageBox.Yes:
            self.usersett.reset_to_dafaults()
            self.close()



if __name__ == "__main__":
    pass