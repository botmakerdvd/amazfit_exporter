#!/usr/bin/python3
import sys
import amazfit_exporter
from PyQt5 import QtCore, QtWidgets, uic
from PyQt5.QtWidgets import QFileDialog

form_class = uic.loadUiType("amazfit_exporter_gui.ui")[0]
class MyWindowClass(QtWidgets.QMainWindow, form_class):
	def __init__(self, parent=None):
		QtWidgets.QMainWindow.__init__(self, parent)
		self.setupUi(self)
		self.but_select_orig.clicked.connect(self.but_select_orig_clicked)
		self.but_select_dest.clicked.connect(self.but_select_dest_clicked)
		self.but_generate.clicked.connect(self.gpx_fromdb)

	def but_select_orig_clicked(self):
		self.text_path_orig.setText(QFileDialog.getOpenFileName()[0])
	def but_select_dest_clicked(self):
		self.text_path_dest.setText(QFileDialog.getExistingDirectory())
	def gpx_fromdb(self):
		db = self.text_path_orig.text()
		dest = self.text_path_dest.text()
		amazfit_exporter.db_to_gpx(db,dest)
		self.endlabel.setText("GPX files exportation finished")
app = QtWidgets.QApplication(sys.argv)
MyWindow = MyWindowClass(None)
MyWindow.show()
app.exec_()
