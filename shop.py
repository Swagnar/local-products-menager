# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GUI.ui'
#
# Created by: PyQt4 UI code generator 4.12.1
#
# WARNING! All changes made in this file will be lost!
from __future__ import division
import sys
import random
import time
import csv
from PyQt4 import QtCore
from PyQt4 import QtGui
from PyQt4.Qt import *
def main():
    app = QApplication(sys.argv)
    ex = Ui_MainWindow()
    w = QMainWindow()
    ex.setupUi(w)
    w.show()
    sys.exit(app.exec_())
    
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

#deklaracja tablicy globalnej do przechowywania zawartości QtGui.QTableWidget
#używana podczas wyszukiwań, dodawania, wszystkiego
dane = []
tabInwersyjna0 = {}
tabInwersyjna1 = {}
tabInwersyjna2 = {}
tabInwersyjna3 = {}
tabInwersyjna4 = {}
tabInwersyjna5 = {}
tabInwersyjna6 = {}
tabInwersyjna7 = {}

#klasa głównego okna
class Ui_MainWindow(object):
    #klasa inwokująca główne elementy okna
    def setupUi(self, MainWindow):

        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(1094, 600)

        validator = QtGui.QDoubleValidator()
        #walidator liczb double, to do formularza 


        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.tableWidget = QtGui.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(20, 10, 801, 561))
        self.tableWidget.setMouseTracking(False)
        self.tableWidget.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.tableWidget.setObjectName(_fromUtf8("tableWidget"))
        self.tableWidget.setColumnCount(8)
        self.tableWidget.setRowCount(0)
        self.tableWidget.setSelectionMode(QtGui.QAbstractItemView.NoSelection)
        self.tableWidget.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, item)

        item = QtGui.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(9)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(0, item)

        item = QtGui.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(9)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(1, item)

        item = QtGui.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(9)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(9)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtGui.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(9)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtGui.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(9)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(5, item)
        item = QtGui.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(9)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(6, item)
        item = QtGui.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(9)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(7, item)

        item = QtGui.QTableWidgetItem()
        self.tableWidget.setItem(0, 0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setItem(0, 1, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setItem(0, 2, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setItem(0, 3, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setItem(0, 4, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setItem(0, 5, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setItem(0, 6, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setItem(0, 7, item)

        self.labelAdd = QtGui.QLabel(self.centralwidget)
        self.labelAdd.setGeometry(QtCore.QRect(840, 15, 101, 17))
        self.labelAdd.setObjectName(_fromUtf8("labelAdd"))
        self.line = QtGui.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(825, 30, 265, 16))
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.labelProduct = QtGui.QLabel(self.centralwidget)
        self.labelProduct.setGeometry(QtCore.QRect(840, 50, 66, 17))
        self.labelProduct.setObjectName(_fromUtf8("labelProduct"))
        self.choiceProduct = QtGui.QComboBox(self.centralwidget)
        self.choiceProduct.setGeometry(QtCore.QRect(832, 70, 141, 27))
        self.choiceProduct.setObjectName(_fromUtf8("choiceProduct"))
        self.choiceProduct.addItem(_fromUtf8(""))
        self.choiceProduct.addItem(_fromUtf8(""))
        self.choiceProduct.addItem(_fromUtf8(""))
        self.choiceProduct.addItem(_fromUtf8(""))
        self.choiceProduct.addItem(_fromUtf8(""))
        self.choiceProduct.addItem(_fromUtf8(""))
        self.choiceProduct.addItem(_fromUtf8(""))
        self.choiceProduct.addItem(_fromUtf8(""))
        self.choiceProduct.addItem(_fromUtf8(""))
        self.choiceProduct.addItem(_fromUtf8(""))
        self.productDate = QtGui.QDateEdit(self.centralwidget)
        self.productDate.setGeometry(QtCore.QRect(832, 130, 141, 27))
        self.productDate.setMaximumDate(QtCore.QDate(2019, 12, 31))
        self.productDate.setMinimumDate(QtCore.QDate(1900, 1, 1))
        self.productDate.setObjectName(_fromUtf8("productDate"))
        self.labelDate = QtGui.QLabel(self.centralwidget)
        self.labelDate.setGeometry(QtCore.QRect(840, 110, 91, 17))
        self.labelDate.setObjectName(_fromUtf8("labelDate"))
        self.cenaPL = QtGui.QLineEdit(self.centralwidget)
        self.cenaPL.setGeometry(QtCore.QRect(980, 70, 113, 27))
        self.cenaPL.setInputMethodHints(QtCore.Qt.ImhDigitsOnly)
        self.cenaPL.setObjectName(_fromUtf8("cenaPL"))
        self.cenaPL.setValidator(validator)
        self.cenaRE = QtGui.QLineEdit(self.centralwidget)
        self.cenaRE.setGeometry(QtCore.QRect(980, 130, 113, 27))
        self.cenaRE.setInputMethodHints(QtCore.Qt.ImhDigitsOnly)
        self.cenaRE.setObjectName(_fromUtf8("cenaRE"))
        self.cenaRE.setValidator(validator)
        self.cenaWW = QtGui.QLineEdit(self.centralwidget)
        self.cenaWW.setGeometry(QtCore.QRect(980, 100, 113, 27))
        self.cenaWW.setInputMethodHints(QtCore.Qt.ImhDigitsOnly)
        self.cenaWW.setObjectName(_fromUtf8("cenaWW"))
        self.cenaWW.setValidator(validator)
        self.densityProduct = QtGui.QLineEdit(self.centralwidget)
        self.densityProduct.setGeometry(QtCore.QRect(980, 160, 113, 27))
        self.densityProduct.setInputMethodHints(QtCore.Qt.ImhDigitsOnly)
        self.densityProduct.setObjectName(_fromUtf8("densityProduct"))
        self.boolProduct = QtGui.QCheckBox(self.centralwidget)
        self.boolProduct.setGeometry(QtCore.QRect(850, 160, 96, 22))
        self.boolProduct.setObjectName(_fromUtf8("boolProduct"))
        self.brandProduct = QtGui.QLineEdit(self.centralwidget)
        self.brandProduct.setGeometry(QtCore.QRect(832, 210, 261, 27))
        self.brandProduct.setObjectName(_fromUtf8("brandProduct"))
        self.labelBrand = QtGui.QLabel(self.centralwidget)
        self.labelBrand.setGeometry(QtCore.QRect(840, 190, 91, 17))
        self.labelBrand.setObjectName(_fromUtf8("labelBrand"))
        
        
        #definicja pojedynczego guzika
        self.addProduct = QtGui.QPushButton(self.centralwidget) #gdzie
        self.addProduct.setGeometry(QtCore.QRect(900, 240, 97, 27)) #wlasciwosci
        self.addProduct.setObjectName(_fromUtf8("addProduct")) #nazwa
        dane = self.addProduct.clicked.connect(self.add_product)
        #tutaj wywoluje funkcje add_product i przekazuje zmienna dane jako argument by zmieniac jej zawartosc
        

        self.line_2 = QtGui.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(825, 270, 265, 16))
        self.line_2.setFrameShape(QtGui.QFrame.HLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName(_fromUtf8("line_2"))
        self.line_3 = QtGui.QFrame(self.centralwidget)
        self.line_3.setGeometry(QtCore.QRect(825, 37, 3, 241))
        self.line_3.setFrameShape(QtGui.QFrame.VLine)
        self.line_3.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_3.setObjectName(_fromUtf8("line_3"))
        self.labelDelete = QtGui.QLabel(self.centralwidget)
        self.labelDelete.setGeometry(QtCore.QRect(840, 290, 66, 17))
        self.labelDelete.setObjectName(_fromUtf8("labelDelete"))
        self.line_4 = QtGui.QFrame(self.centralwidget)
        self.line_4.setGeometry(QtCore.QRect(825, 310, 265, 3))
        self.line_4.setFrameShape(QtGui.QFrame.HLine)
        self.line_4.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_4.setObjectName(_fromUtf8("line_4"))
        self.line_5 = QtGui.QFrame(self.centralwidget)
        self.line_5.setGeometry(QtCore.QRect(1000, 310, 3, 75))
        self.line_5.setFrameShape(QtGui.QFrame.VLine)
        self.line_5.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_5.setObjectName(_fromUtf8("line_5"))

        self.importTable = QtGui.QPushButton(self.centralwidget)
        self.importTable.setGeometry(QtCore.QRect(1010, 320, 70, 27))
        self.importTable.setObjectName(_fromUtf8("importTable"))
        dane = self.importTable.clicked.connect(self.import_from_txt)
        #niedzialajacy import

        self.exportTable = QtGui.QPushButton(self.centralwidget)
        self.exportTable.setGeometry(QtCore.QRect(1010, 350, 70, 27))
        self.exportTable.setObjectName(_fromUtf8("exportTable"))
        dane = self.exportTable.clicked.connect(self.export_to_txt)

        self.idToDelete = QtGui.QSpinBox(self.centralwidget)
        self.idToDelete.setGeometry(QtCore.QRect(832, 320, 60, 27))
        self.idToDelete.setObjectName(_fromUtf8("idToDelete"))
        self.deleteProduct = QtGui.QPushButton(self.centralwidget)
        self.deleteProduct.setGeometry(QtCore.QRect(900, 320, 97, 27))
        self.deleteProduct.setObjectName(_fromUtf8("deleteProduct"))
        dane = self.deleteProduct.clicked.connect(self.delete_product)
        self.deleteAllProduct = QtGui.QPushButton(self.centralwidget)
        self.deleteAllProduct.setGeometry(QtCore.QRect(832, 350, 165, 27))
        self.deleteAllProduct.setObjectName(_fromUtf8("deleteAllProduct"))
        dane = self.deleteAllProduct.clicked.connect(self.delete_all_products)
        self.line_7 = QtGui.QFrame(self.centralwidget)
        self.line_7.setGeometry(QtCore.QRect(825, 383, 265, 3))
        self.line_7.setFrameShape(QtGui.QFrame.HLine)
        self.line_7.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_7.setObjectName(_fromUtf8("line_7"))
        self.labelRandom = QtGui.QLabel(self.centralwidget)
        self.labelRandom.setGeometry(QtCore.QRect(840, 390, 66, 17))
        self.labelRandom.setObjectName(_fromUtf8("labelRandom"))
        self.line_6 = QtGui.QFrame(self.centralwidget)
        self.line_6.setGeometry(QtCore.QRect(825, 310, 3, 74))
        self.line_6.setFrameShape(QtGui.QFrame.VLine)
        self.line_6.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_6.setObjectName(_fromUtf8("line_6"))
        self.nRandom = QtGui.QSpinBox(self.centralwidget)
        self.nRandom.setGeometry(QtCore.QRect(830, 420, 60, 27))
        self.nRandom.setObjectName(_fromUtf8("nRandom"))
        self.nRandom.setMaximum(99999999)
        self.randomizeButton = QtGui.QPushButton(self.centralwidget)
        self.randomizeButton.setGeometry(QtCore.QRect(900, 420, 181, 27))
        self.randomizeButton.setObjectName(_fromUtf8("randomizeButton"))
        dane = self.randomizeButton.clicked.connect(self.randomize_products)
        self.line_8 = QtGui.QFrame(self.centralwidget)
        self.line_8.setGeometry(QtCore.QRect(825, 410, 265, 3))
        self.line_8.setFrameShape(QtGui.QFrame.HLine)
        self.line_8.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_8.setObjectName(_fromUtf8("line_8"))
        self.line_9 = QtGui.QFrame(self.centralwidget)
        self.line_9.setGeometry(QtCore.QRect(825, 455, 265, 3))
        self.line_9.setFrameShape(QtGui.QFrame.HLine)
        self.line_9.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_9.setObjectName(_fromUtf8("line_9"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.menuBar = QtGui.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 1131, 25))
        self.menuBar.setObjectName(_fromUtf8("menuBar"))
        self.menuOpcje = QtGui.QMenu(self.menuBar)
        self.menuOpcje.setObjectName(_fromUtf8("menuOpcje"))
        MainWindow.setMenuBar(self.menuBar)
        self.actionWyszukiwanie_liniowe = QtGui.QAction(MainWindow)
        self.actionWyszukiwanie_liniowe.setObjectName(_fromUtf8("actionWyszukiwanie_liniowe"))
        dane = self.actionWyszukiwanie_liniowe.triggered.connect(self.linear_search)
        self.actionWyszykiwanie_binarne = QtGui.QAction(MainWindow)
        self.actionWyszykiwanie_binarne.setObjectName(_fromUtf8("actionWyszykiwanie_binarne"))
        dane = self.actionWyszykiwanie_binarne.triggered.connect(self.linear_search)
        self.actionWyszukiwanie_lancuchowe = QtGui.QAction(MainWindow)
        self.actionWyszukiwanie_lancuchowe.setObjectName(_fromUtf8("actionWyszukiwanie_lancuchowe"))
        dane = self.actionWyszukiwanie_lancuchowe.triggered.connect(self.linear_search)
        self.actionNdelete = QtGui.QAction(MainWindow)
        self.actionNdelete.setObjectName(_fromUtf8("actionNdelete"))
        dane = self.actionNdelete.triggered.connect(self.n_delete)
        self.menuOpcje.addAction(self.actionWyszukiwanie_liniowe)
        self.menuOpcje.addAction(self.actionWyszykiwanie_binarne)
        self.menuOpcje.addAction(self.actionWyszukiwanie_lancuchowe)
        self.menuOpcje.addAction(self.actionNdelete)
        self.menuBar.addAction(self.menuOpcje.menuAction())
        
        self.search_rs_table = QtGui.QTableWidget(self.centralwidget)
        self.search_rs_table.setGeometry(QtCore.QRect(830, 460, 256, 192))
        self.search_rs_table.setObjectName(_fromUtf8("search_rs_table"))
        self.search_rs_table.setColumnCount(8)
        self.search_rs_table.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.search_rs_table.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.search_rs_table.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.search_rs_table.setHorizontalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.search_rs_table.setHorizontalHeaderItem(3, item)
        item = QtGui.QTableWidgetItem()
        self.search_rs_table.setHorizontalHeaderItem(4, item)
        item = QtGui.QTableWidgetItem()
        self.search_rs_table.setHorizontalHeaderItem(5, item)
        item = QtGui.QTableWidgetItem()
        self.search_rs_table.setHorizontalHeaderItem(6, item)
        item = QtGui.QTableWidgetItem()
        self.search_rs_table.setHorizontalHeaderItem(7, item)



        self.le = QLineEdit()
        self.le2 = QLineEdit()
        self.le3 = QLineEdit()
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
    #klasa inwokujaca mniej wazne rzeczy, jakies stringi, formaty widoku i inne
    def retranslateUi(self, MainWindow):
        item = self.search_rs_table.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Produkt", None))
        item = self.search_rs_table.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Firma", None))
        item = self.search_rs_table.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Rok wydania", None))
        item = self.search_rs_table.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Gramatura", None))
        item = self.search_rs_table.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Dostępność", None))
        item = self.search_rs_table.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Cena w Polsce", None))
        item = self.search_rs_table.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "Cena na świecie", None))
        item = self.search_rs_table.horizontalHeaderItem(7)
        item.setText(_translate("MainWindow", "Cena retail", None))
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))

        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Produkt", None))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Firma", None))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Rok wydania", None))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Gramatura", None))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Dostępność", None))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Cena w Polsce", None))
        item = self.tableWidget.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "Cena na świecie", None))
        item = self.tableWidget.horizontalHeaderItem(7)
        item.setText(_translate("MainWindow", "Cena retail", None))
        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        
        self.tableWidget.setSortingEnabled(__sortingEnabled)
        self.labelAdd.setText(_translate("MainWindow", "Dodaj do bazy:", None))
        self.labelProduct.setText(_translate("MainWindow", "Produkt:", None))
        self.choiceProduct.setItemText(0, _translate("MainWindow", "Hoodie", None))
        self.choiceProduct.setItemText(1, _translate("MainWindow", "T-shirt", None))
        self.choiceProduct.setItemText(2, _translate("MainWindow", "Czapka", None))
        self.choiceProduct.setItemText(3, _translate("MainWindow", "Beanie", None))
        self.choiceProduct.setItemText(4, _translate("MainWindow", "Buty", None))
        self.choiceProduct.setItemText(5, _translate("MainWindow", "Kurtka", None))
        self.choiceProduct.setItemText(6, _translate("MainWindow", "Plaszcz", None))
        self.choiceProduct.setItemText(7, _translate("MainWindow", "Parka", None))
        self.choiceProduct.setItemText(8, _translate("MainWindow", "Bomberka", None))
        self.productDate.setDisplayFormat(_translate("MainWindow", "yyyy", None))
        self.labelDate.setText(_translate("MainWindow", "Rok wydania:", None))
        self.cenaPL.setPlaceholderText(_translate("MainWindow", "cena w polsce", None))
        self.cenaRE.setPlaceholderText(_translate("MainWindow", "cena retail", None))
        self.densityProduct.setPlaceholderText(_translate("MainWindow", "gramatura", None))
        self.boolProduct.setText(_translate("MainWindow", "Dostępne?", None))
        self.cenaWW.setPlaceholderText(_translate("MainWindow", "cena na świecie", None))
        self.labelBrand.setText(_translate("MainWindow", "Nazwa firmy:", None))
        self.addProduct.setText(_translate("MainWindow", "Dodaj", None))
        self.labelDelete.setText(_translate("MainWindow", "Usuń:", None))
        self.importTable.setText(_translate("MainWindow", "Import", None))
        self.exportTable.setText(_translate("MainWindow", "Export", None))
        self.deleteProduct.setText(_translate("MainWindow", "Usuń", None))
        self.deleteAllProduct.setText(_translate("MainWindow", "Usuń wszysko", None))
        self.labelRandom.setText(_translate("MainWindow", "Losuj:", None))
        self.randomizeButton.setText(_translate("MainWindow", "Wygeneruj", None))
        self.menuOpcje.setTitle(_translate("MainWindow", "Opcje", None))
        self.actionWyszukiwanie_liniowe.setText(_translate("MainWindow", "Wyszukiwanie liniowe", None))
        self.actionWyszukiwanie_liniowe.setShortcut(_translate("MainWindow", "Ctrl+L", None))
        self.actionWyszykiwanie_binarne.setText(_translate("MainWindow", "Wyszykiwanie binarne", None))
        self.actionWyszykiwanie_binarne.setShortcut(_translate("MainWindow", "Ctrl+B", None))
        self.actionWyszukiwanie_lancuchowe.setText(_translate("MainWindow", "Wyszukiwanie lancuchowe", None))
        self.actionWyszukiwanie_lancuchowe.setShortcut(_translate("MainWindow", "Ctrl+C", None))
        self.actionNdelete.setText(_translate("MainWindow", "Usuń co n-ty rekord", None))
        self.actionNdelete.setShortcut(_translate("MainWindow", "Ctrl+N", None))
    #funkcja usuwajaca co n-te pozycje
    def n_delete(self,MainWindow):
        print "suk"
        num, ok = QInputDialog.getInt(self.le3, "N-te usuwanie", "Wpisz liczbe:")
        #pobieranie imputu
        if ok:
            self.le3.setText(str(num))

        tmp = 0
        rows = self.tableWidget.rowCount()
        while tmp <= rows:
            print(str(tmp) + " | " + str(rows) + " = " + str(tmp%num))
            if rows % num == 0:
                dane.pop(tmp) #usuwanie ze zmiennej globalnej
                self.tableWidget.removeRow(tmp) #usuwanie ze QtGui.QTableWidget

            tmp = tmp + 1
    def export_to_txt(self,MainWindow):

        FileDump = open('exportedDB.txt', 'r+')
        FileDump.truncate(0)
        FileDump.close()
        with open('exportedDB.txt', 'w') as f:
            csv.writer(f, delimiter=' ').writerows(dane)

    def import_from_txt(self,MainWindow):
        y = 0
        importedDane = []
        with open("exportedDB.txt", "r") as f:
            for r in f:
                r = r.rstrip()
                numbers = r.split(' ')
                importedDane.insert(y, numbers)
                y = y + 1
        rows = len(importedDane) 
        n = 0
        while n < rows:
            self.tableWidget.insertRow(n)
            self.tableWidget.setItem(n, 0, QTableWidgetItem(importedDane[n][1]))
            self.tableWidget.setItem(n, 1, QTableWidgetItem(importedDane[n][2]))
            self.tableWidget.setItem(n, 2, QTableWidgetItem(importedDane[n][3]))
            self.tableWidget.setItem(n, 3, QTableWidgetItem(importedDane[n][4]))
            if importedDane[n][5] == "0":
                self.tableWidget.setItem(n, 4, QTableWidgetItem("Nie"))
            else:
                self.tableWidget.setItem(n, 4, QTableWidgetItem("Tak"))
            self.tableWidget.setItem(n, 5, QTableWidgetItem(importedDane[n][6]))
            self.tableWidget.setItem(n, 6, QTableWidgetItem(importedDane[n][7]))
            self.tableWidget.setItem(n, 7, QTableWidgetItem(importedDane[n][8]))
            n += 1

    def add_product(self, MainWindow):
        tekst = ""
        rows = self.tableWidget.rowCount()
        print "liczba startowa: " + str(rows)
        if self.boolProduct.isChecked():
            tekst = "Tak"
        else:
            tekst = "Nie"
        if self.brandProduct.text() == "" and self.densityProduct.text() == "" and self.cenaPL.text() == "" and self.cenaWW.text() == "" and self.cenaRE.text() == "":
            print "Brakujące argumenty"
        else:
            #wstawiam pusty wiersz
            self.tableWidget.insertRow(rows)
            dane.insert(rows, [rows, str(self.choiceProduct.currentText()),
                str(self.brandProduct.text()),
                str(self.productDate.date().toString('yyyy')),
                str(self.densityProduct.text()),
                tekst,
                str(self.cenaPL.text()),
                str(self.cenaWW.text()),
                str(self.cenaRE.text())])
            #ze zmniennej dane wrzucam elementy do stringgrida
            self.tableWidget.setItem(rows, 0, QtGui.QTableWidgetItem(unicode(self.choiceProduct.currentText())))
            self.tableWidget.setItem(rows, 1, QtGui.QTableWidgetItem(unicode(self.brandProduct.text())))
            self.tableWidget.setItem(rows, 2, QtGui.QTableWidgetItem(self.productDate.date().toString('yyyy')))
            self.tableWidget.setItem(rows, 3, QtGui.QTableWidgetItem(self.densityProduct.text()))
            self.tableWidget.setItem(rows, 4, QtGui.QTableWidgetItem(tekst))
            self.tableWidget.setItem(rows, 5, QtGui.QTableWidgetItem(self.cenaPL.text()))
            self.tableWidget.setItem(rows, 6, QtGui.QTableWidgetItem(self.cenaWW.text()))
            self.tableWidget.setItem(rows, 7, QtGui.QTableWidgetItem(self.cenaRE.text()))
            #debug
            print "liczba po dodaniu: " + str(self.tableWidget.rowCount())
            print dane
            #re.findall('"([^"]*)"', dane)

    def delete_product(self, MainWindow):
        rows = self.tableWidget.rowCount()
        ajdi = self.idToDelete.value()

        if ajdi > rows:
            print "nie ma takiego produktu"
        else:
            dane.pop(ajdi-1) #usuwanie ze zmiennej
            self.tableWidget.removeRow(ajdi-1) #usuwanie ze stringgrida

    def delete_all_products(self, MainWindow):
        dane = []
        self.tableWidget.setRowCount(0) #yup

    def randomize_products(self,MainWindow):
        n = self.nRandom.value()
        rows = self.tableWidget.rowCount()
        #czasStartowy = time.time()
        while n > 0:
            x = 8
            brand = ""
            randomBool = random.randint(0,1)                        #seed dla bool'a
            while x > 0:
                brand = brand + str(chr(random.randint(97,122)))    #rand nazwa firmy
                x = x - 1

            if randomBool == 1:
                flextape = "Tak"
            else:
                flextape = "Nie"

            randomChoice = random.randint(0,8)                      #seed dla menu wyboru

            self.tableWidget.insertRow(rows)                        #wstawiam pusty wiersz do stringgrida


            #wrzucam losowe wartosci do zmiennej
            dane.insert(rows, [rows, str(self.choiceProduct.itemText(randomChoice)),
                brand, 
                str(random.randint(1900, 2019)),
                str(random.randint(100, 320)),
                randomBool,
                str(random.uniform(0.0, 9999.9)),
                str(random.uniform(0, 9999)),
                str(random.uniform(0, 9999))])
            self.tableWidget.setItem(rows, 0, QtGui.QTableWidgetItem(unicode(self.choiceProduct.itemText(randomChoice))))
            self.tableWidget.setItem(rows, 1, QtGui.QTableWidgetItem(brand))
            self.tableWidget.setItem(rows, 2, QtGui.QTableWidgetItem(dane[rows][3]))
            self.tableWidget.setItem(rows, 3, QtGui.QTableWidgetItem(dane[rows][4]))
            if randomBool == 1:
                self.tableWidget.setItem(rows, 4, QtGui.QTableWidgetItem("Tak"))
            else:
                self.tableWidget.setItem(rows, 4, QtGui.QTableWidgetItem("Nie"))
            self.tableWidget.setItem(rows, 5, QtGui.QTableWidgetItem(dane[rows][6]))
            self.tableWidget.setItem(rows, 6, QtGui.QTableWidgetItem(dane[rows][7]))
            self.tableWidget.setItem(rows, 7, QtGui.QTableWidgetItem(dane[rows][8]))
            
            if str(dane[rows][1]) not in tabInwersyjna1:
                tabInwersyjna1[str(dane[rows][1])]=[rows]
            else:
                tabInwersyjna1[str(dane[rows][1])].append(rows)
            
            if str(dane[rows][2]) not in tabInwersyjna2:
                tabInwersyjna2[str(dane[rows][2])]=[rows]
            else:
                tabInwersyjna2[str(dane[rows][2])].append(rows)

            if str(dane[rows][3]) not in tabInwersyjna3:
                tabInwersyjna3[str(dane[rows][3])]=[rows]
            else:
                tabInwersyjna3[str(dane[rows][3])].append(rows)
            
            if str(dane[rows][4]) not in tabInwersyjna4:
                tabInwersyjna4[str(dane[rows][4])]=[rows]
            else:
                tabInwersyjna4[str(dane[rows][4])].append(rows)

            if str(dane[rows][5]) not in tabInwersyjna5:
                tabInwersyjna5[str(dane[rows][5])]=[rows]
            else:
                tabInwersyjna5[str(dane[rows][5])].append(rows)

            if str(dane[rows][6]) not in tabInwersyjna6:
                tabInwersyjna6[str(dane[rows][6])]=[rows]
            else:
                tabInwersyjna6[str(dane[rows][6])].append(rows)

            if str(dane[rows][7]) not in tabInwersyjna7:
                tabInwersyjna7[str(dane[rows][7])]=[rows]
            else:
                tabInwersyjna7[str(dane[rows][7])].append(rows)
            
            print n
            n = n - 1
            rows = rows + 1


        #czasKoncowy = time.time() - czasStartowy
        #print "\n[" + str(czasKoncowy) + " sekund"
        #print(dane[94][0])
    def binary_search(self,MainWindow):
        rows = self.tableWidget.rowCount()
        rt = rows - 1
        lf = 0
        toBeSortedValues = []
        foundedValues = []
        items = ("Produkt", "Firma", "Rok Wydania", "Gramatura", "Dostepnosc", "Cena w Polsce", "Cena na swiecie", "Cena retail")

        item, ok = QInputDialog.getItem(self.le, 'Wyszukiwanie binarne', "Lista kolumn", items, 0, False)

        if ok and item:
            self.le.setText(item)

        text, ok = QInputDialog.getText(self.le2, 'Wyszukiwanie binarne', 'Wpisz szukana wartosc:')

        if ok:
            self.le2.setText(unicode(text))
        z = 0
        while z != 8:
            if self.le.text() == items[z]:
                for r in range(rows):
                    toBeSortedValues.insert(r, dane[r][z+1])
                sortedValues = sorted(toBeSortedValues)
            z = z + 1

        if(sortedValues[lf] == self.le2.text()):
            foundedValues.append(sortedValues[lf])
        if(sortedValues[rt] == self.le2.text()):
            foundedValues.append(sortedValues[lf])

        while lf + 1 < rt:
            mid = (lf+rt) / 2
            pivot = sortedValues[int(mid)]
            print("lf = " + str(lf) + " rt = " + str(rt) + " mid = " + str(mid) + " pivot = " + str(pivot))
            if(pivot == self.le2.text()):
                foundedValues.append(pivot)
                break
            elif pivot > self.le2.text():
                lf = int(mid)
            else:
                rt = int(mid)
        print foundedValues

        z = 0
        while z != 8:
            if self.le.text() == items[z]:
                for r in range(rows):
                    if self.tableWidget.item(r,z).text() == self.le2.text():
                        self.search_rs_table.insertRow(newRows)
                        self.search_rs_table.setItem(newRows, 0, QtGui.QTableWidgetItem(self.tableWidget.item(r,0)))
                        self.search_rs_table.setItem(newRows, 1, QtGui.QTableWidgetItem(self.tableWidget.item(r,1).text()))
                        self.search_rs_table.setItem(newRows, 2, QtGui.QTableWidgetItem(self.tableWidget.item(r,2).text()))
                        self.search_rs_table.setItem(newRows, 3, QtGui.QTableWidgetItem(self.tableWidget.item(r,3).text()))
                        self.search_rs_table.setItem(newRows, 4, QtGui.QTableWidgetItem(self.tableWidget.item(r,4).text()))
                        self.search_rs_table.setItem(newRows, 5, QtGui.QTableWidgetItem(self.tableWidget.item(r,5).text()))
                        self.search_rs_table.setItem(newRows, 6, QtGui.QTableWidgetItem(self.tableWidget.item(r,6).text()))
                        self.search_rs_table.setItem(newRows, 7, QtGui.QTableWidgetItem(self.tableWidget.item(r,7).text()))
                        newRows += 1
                        print(str(r+1) + "|" + self.tableWidget.item(r,0).text() + "|" + self.tableWidget.item(r,1).text() + "|" + str(self.tableWidget.item(r,2).text()) + "|" + str(self.tableWidget.item(r,3).text()) + "|" + str(self.tableWidget.item(r,4).text()) + "|" + str(self.tableWidget.item(r,5).text()) + "|" + str(self.tableWidget.item(r,6).text()) + "|" + str(self.tableWidget.item(r,7).text()))
            z = z + 1
        '''while lf <= rt:
            mid = (lf + rt)/2
            pivot = sortedValues[int(mid)]
            print("lf = " + str(lf) + " rt = " + str(rt) + " mid = " + str(mid) + " pivot = " + str(pivot))
            if pivot > self.le2.text():
                rt = mid - 1
            elif pivot < self.le2.text():
                lf = mid + 1
            else:
                print pivot
        '''


        

    def linear_search(self,MainWindow):
        beginingsTable = []
        rows = self.tableWidget.rowCount()
        newRows = self.search_rs_table.rowCount()
        #print rows, newRows
        items = ("Produkt", "Firma", "Rok Wydania", "Gramatura", "Dostepnosc", "Cena w Polsce", "Cena na swiecie", "Cena retail")

        item, ok = QInputDialog.getItem(self.le, 'Wyszukiwanie ', "Lista kolumn", items, 0, False)
        #pierwszy box, combobox w ktorym wybierasz kolumne po ktorej szukasz
        if ok and item:
            self.le.setText(item)

        text, ok = QInputDialog.getText(self.le2, 'Wyszukiwanie ', 'Wpisz szukana wartosc:')
        #pobieranie wartosci do wyszukania
        if ok:
            self.le2.setText(unicode(text))
        chain_bool = 1
        tmp = 0
        z = 0
        visited = set()
        czasStartowy = time.time()
        while z != 8:
            #if gramatura == gramatura
            if self.le.text() == items[z]:
                for r in range(rows):
                    if self.tableWidget.item(r,z).text() == self.le2.text():
                        self.search_rs_table.insertRow(newRows)
                        self.search_rs_table.setItem(newRows, 0, QtGui.QTableWidgetItem(self.tableWidget.item(r,0)))
                        self.search_rs_table.setItem(newRows, 1, QtGui.QTableWidgetItem(self.tableWidget.item(r,1).text()))
                        self.search_rs_table.setItem(newRows, 2, QtGui.QTableWidgetItem(self.tableWidget.item(r,2).text()))
                        self.search_rs_table.setItem(newRows, 3, QtGui.QTableWidgetItem(self.tableWidget.item(r,3).text()))
                        self.search_rs_table.setItem(newRows, 4, QtGui.QTableWidgetItem(self.tableWidget.item(r,4).text()))
                        self.search_rs_table.setItem(newRows, 5, QtGui.QTableWidgetItem(self.tableWidget.item(r,5).text()))
                        self.search_rs_table.setItem(newRows, 6, QtGui.QTableWidgetItem(self.tableWidget.item(r,6).text()))
                        self.search_rs_table.setItem(newRows, 7, QtGui.QTableWidgetItem(self.tableWidget.item(r,7).text()))
                        newRows += 1
                czasKoncowy = czasStartowy - time.time()
            z = z + 1
        z = 0
        while z != 8:
            if self.le.text() == items[z]:
                print("\n\n")
                while tmp < rows:
                    if self.tableWidget.item(tmp,z).text() not in visited:  #sprawdzam czy wartosc juz wystapila w visited
                        visited.add(self.tableWidget.item(tmp,z).text())    #jezeli tak, dodaje ja do visited i nastepnym razem nie wykonuje linijki ponizej
                        beginingsTable.append([str(self.tableWidget.item(tmp,z).text()), tmp+1])
                        tmp += 1
                    else:                                                   #jezeli nie, zwieksz tmp i sprawdz nastepny wiersz
                        tmp += 1
            z += 1
        
        beginingsTable.sort()

        print beginingsTable
        print("Znaleziono: " + str(newRows) + " rekordow")  


    def chain_search(self,MainWindow):
        rows = self.tableWidget.rowCount()
        newRows = self.search_rs_table.rowCount()
        visited = set()
        beginingsTable = []
        z = 0
        tmp = 0
        print rows, newRows
        items = ("Produkt", "Firma", "Rok Wydania", "Gramatura", "Dostepnosc", "Cena w Polsce", "Cena na swiecie", "Cena retail")

        item, ok = QInputDialog.getItem(self.le, 'Wyszukiwanie ', "Lista kolumn", items, 0, False)

        if ok and item:
            self.le.setText(item)

        text, ok = QInputDialog.getText(self.le2, 'Wyszukiwanie ', 'Wpisz szukana wartosc:')

        if ok:
            self.le2.setText(unicode(text))

        BeginingsTable = {}
        while z != 8:
            if self.le.text() == items[z]:
                print("\n\n")
                while tmp < rows:
                    if self.tableWidget.item(tmp,z).text() not in visited:  #sprawdzam czy wartosc juz wystapila w visited
                        visited.add(self.tableWidget.item(tmp,z).text())    #jezeli tak, dodaje ja do visited i nastepnym razem nie wykonuje linijki ponizej
                        beginingsTable.append([str(self.tableWidget.item(tmp,z).text()), tmp])
                        tmp += 1
                    else:                                                   #jezeli nie, zwieksz tmp i sprawdz nastepny wiersz
                        tmp += 1
                z += 1
        beginingsTable.sort()
        if z == 0:
            BeginingsTable = tabInwersyjna0
        elif z == 1:
            BeginingsTable = tabInwersyjna1
        elif z == 2:
            BeginingsTable = tabInwersyjna2
        elif z == 3:
            BeginingsTable = tabInwersyjna3
        elif z == 4:
            BeginingsTable = tabInwersyjna4
        elif z == 5:
            BeginingsTable = tabInwersyjna5
        elif z == 6:
            BeginingsTable = tabInwersyjna6
        elif z == 7:
            BeginingsTable = tabInwersyjna7

        if str(self.le2.text()) in beginingsTable:
            wynik = []
            n = 0
            for val in beginingsTable[str(self.le2.text())]:
                wynik.insert(n, dane[value])
                n += 1
        tmp = 0
        while tmp < rows:
            if self.tableWidget.item(tmp,z).text() not in visited:  #sprawdzam czy wartosc juz wystapila w visited
                visited.add(self.tableWidget.item(tmp,z).text())    #jezeli tak, dodaje ja do visited i nastepnym razem nie wykonuje linijki ponizej
                beginingsTable.append([str(self.tableWidget.item(tmp,z).text()), tmp+1])
                tmp += 1
            else:                                                   #jezeli nie, zwieksz tmp i sprawdz nastepny wiersz
                tmp += 1
        beginingsTable.sort()
        
        
main()