# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ventana15puntos.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

import requests
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_VentanaCorreo(object):
    def setupUi(self, VentanaCorreo):
        VentanaCorreo.setObjectName("VentanaCorreo")
        VentanaCorreo.resize(402, 150)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icono.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        VentanaCorreo.setWindowIcon(icon)
        self.cajaTextoCorreo = QtWidgets.QLineEdit(VentanaCorreo)
        self.cajaTextoCorreo.setGeometry(QtCore.QRect(100, 40, 201, 20))
        self.cajaTextoCorreo.setObjectName("cajaTextoCorreo")
        self.label = QtWidgets.QLabel(VentanaCorreo)
        self.label.setGeometry(QtCore.QRect(120, 10, 161, 20))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(VentanaCorreo)
        self.label_2.setGeometry(QtCore.QRect(70, 70, 261, 21))
        self.label_2.setObjectName("label_2")
        self.botonEnviarCorreo = QtWidgets.QPushButton(VentanaCorreo)
        self.botonEnviarCorreo.setGeometry(QtCore.QRect(160, 100, 81, 23))
        self.botonEnviarCorreo.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.botonEnviarCorreo.setObjectName("botonEnviarCorreo")

        self.envioFinalizado = False
        self.botonEnviarCorreo.clicked.connect(self.enviarCorreo)

        self.retranslateUi(VentanaCorreo)
        QtCore.QMetaObject.connectSlotsByName(VentanaCorreo)

    def retranslateUi(self, VentanaCorreo):
        _translate = QtCore.QCoreApplication.translate
        VentanaCorreo.setWindowTitle(_translate("VentanaCorreo", "Spell Guesser 0.2"))
        self.label.setText(_translate("VentanaCorreo", "<html><head/><body><p align=\"center\"><span style=\" font-size:9pt;\">FELICITACIONES</span></p></body></html>"))
        self.label_2.setText(_translate("VentanaCorreo", "<html><head/><body><p align=\"center\">Ingresa tu correo para recibir tu clave</p></body></html>"))
        self.botonEnviarCorreo.setText(_translate("VentanaCorreo", "Enviar"))

    def enviarCorreo(self):
        if len(self.cajaTextoCorreo.text()) > 10:
            print(self.cajaTextoCorreo.text())
            publicacionPrivada = requests.post("https://pastebin.com/api/api_post.php", {"api_dev_key" : "qYMkxOh56SgXxOIybNBw2V_8Iiyv8dWB", "api_user_key": "3b4557b6934a98343f011eb1874cb89d", "api_option" : "paste", "api_paste_code": self.cajaTextoCorreo.text(), "api_paste_private" : "0" })
            #r = requests.post("https://pastebin.com/api/api_post.php", {"api_dev_key" : "qYMkxOh56SgXxOIybNBw2V_8Iiyv8dWB", "api_option": "paste", "api_paste_code" : self.cajaTextoCorreo.text()})
            print(publicacionPrivada.content)