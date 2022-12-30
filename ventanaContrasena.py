# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ventanaContrasena.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from ventanaAdministrador import Ui_VentanaAdministrador


class Ui_VentanaContrasena(object):
    def setupUi(self, VentanaContrasena):
        VentanaContrasena.setObjectName("VentanaContrasena")
        VentanaContrasena.resize(290, 80)
        self.cajaTextoContrasena = QtWidgets.QLineEdit(VentanaContrasena)
        self.cajaTextoContrasena.setGeometry(QtCore.QRect(20, 20, 251, 20))
        self.cajaTextoContrasena.setObjectName("cajaTextoContrasena")
        self.pushButton = QtWidgets.QPushButton(VentanaContrasena)
        self.pushButton.setGeometry(QtCore.QRect(110, 50, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.enviarContrasena)

        self.retranslateUi(VentanaContrasena)
        QtCore.QMetaObject.connectSlotsByName(VentanaContrasena)

    def retranslateUi(self, VentanaContrasena):
        _translate = QtCore.QCoreApplication.translate
        VentanaContrasena.setWindowTitle(_translate("VentanaContrasena", "Spell Guesser 0.3"))
        self.pushButton.setText(_translate("VentanaContrasena", "Enviar"))
    
    def enviarContrasena(self):
        try:
            if self.cajaTextoContrasena.text() == "sevenpointou":
                self.abrirVentanaAdministrador()
        except:
            pass
    
    def abrirVentanaAdministrador(self):
        self.ventana = QtWidgets.QMainWindow()
        self.ui = Ui_VentanaAdministrador()
        self.ui.setupUi(self.ventana)
        self.ventana.show()
            
