import sys
import requests
import random
import json
from PyQt5 import uic, QtWidgets
from PyQt5 import QtGui
from ventana15puntos import Ui_VentanaCorreo
from ventanaAdministrador import Ui_VentanaAdministrador
from ventanaContrasena import Ui_VentanaContrasena

qtCreatorFile = "ventanaPrincipal.ui" 

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.contador = 0
        #BOOLEANOS DE EVENTOS COMPLETOS
        self.juegoIniciado = False
        self.cajaCmapeonesHecha = False
        self.quincePuntosObtenidos = False
        #BOTONES
        self.botonActualizarImagen.clicked.connect(self.generarImagen)
        self.botonEnviar.clicked.connect(self.enviarRespuesta)
        self.accionAdministrador.triggered.connect(self.abrirVentanaContrasena)
        #DICCIONARIO CON LOS CORREOS
        with open("correos.txt", "r") as f:
            self.correos = json.load(f)
    
    def generarImagen(self):
        #campeones = "http://ddragon.leagueoflegends.com/cdn/12.23.1/data/es_MX/champion.json"
        #campeon = "http://ddragon.leagueoflegends.com/cdn/12.23.1/data/es_MX/champion/LeeSin.json"
        #hechizo = "http://ddragon.leagueoflegends.com/cdn/12.23.1/img/spell/AsheSpiritOfTheHawk.png"

        if self.juegoIniciado == False:
            self.botonActualizarImagen.deleteLater()
            self.juegoIniciado = True

        #REQUEST PARA LA LISTA DE CAMPEONES
        self.response = requests.get("http://ddragon.leagueoflegends.com/cdn/12.23.1/data/es_MX/champion.json")
        self.r = self.response.json()
        self.data = self.r["data"]

        self.idsCampeones = []
        self.nombresCampeones = []

        for champion in self.data.values():
            self.idsCampeones.append(champion["key"])

        campeonElegido = random.choice(self.idsCampeones)

        #SE RECORRE CADA CAMPEÓN PARA ENCONTRAR AL ELEGIDO
        for champion in self.data.values():
            self.nombresCampeones.append(champion["id"])
            if champion["key"] == campeonElegido:     
                self.nameCampeon = champion["id"]
                self.nameCampeonJson = champion["id"] + ".json"
        #SE OBTIENE EL NOMBRE DEL CAMPEÓN Y SU VERSIÓN .JSON
        if self.cajaCmapeonesHecha == False:
            self.cajaCampeones.addItems(self.nombresCampeones)
            self.cajaCmapeonesHecha = True
        
        #REQUEST PARA OBTENER EL JSON DEL CAMPEÓN SELECCIONADO
        self.campeon = "http://ddragon.leagueoflegends.com/cdn/12.23.1/data/es_MX/champion/{}".format(self.nameCampeonJson)
        self.responseCampeon = requests.get(self.campeon)
        self.r = self.responseCampeon.json()

        #SE CREA LISTA PARA ALMACENAR LOS HECHIZOS
        self.listaHechizo = []

        #SE RECORREN LOS HECHIZOS Y SE AGREGAN A LA LISTA
        for hechizo in self.r["data"][self.nameCampeon]["spells"]:
            self.listaHechizo.append(hechizo["id"])

        #SE ELIGE ALEATORIAMENTE UN HECHIZO
        self.nameHechizo = random.choice(self.listaHechizo)
        self.nameHechizoPng = self.nameHechizo + ".png"
        #SE OBTIENE EL NOMBRE Y SU VERSION .PNG

        #REQUEST PARA OBTENER LA IMAGEN DEL HECHIZO
        self.responseHechizo = requests.get("http://ddragon.leagueoflegends.com/cdn/12.23.1/img/spell/{}".format(self.nameHechizoPng))

        #SE GUARDA LA IMAGEN DEL HECHIZO
        with open('image.jpg', 'wb') as f:
            f.write(self.responseHechizo.content)
        pixmap = QtGui.QPixmap("image.jpg")
        self.etiquetaImagen.setPixmap(pixmap)
        
    def enviarRespuesta(self):  
        if self.cajaCampeones.currentText() == self.nameCampeon:
            self.contador += 1
            if self.contador == 15 and self.quincePuntosObtenidos == False:
                self.abrirVentanaCorreo()
                self.quincePuntosObtenidos = True
            self.cajaContador.display(self.contador)
            self.generarImagen()
        else:
            self.contador = 0
            self.cajaContador.display(self.contador)
            self.generarImagen()
    
    def abrirVentanaCorreo(self):
        self.ventana = QtWidgets.QMainWindow()
        self.ui = Ui_VentanaCorreo()
        self.ui.setupUi(self.ventana)
        self.ventana.show()
    
    def abrirVentanaAdministrador(self):
        self.ventana = QtWidgets.QMainWindow()
        self.ui = Ui_VentanaAdministrador()
        self.ui.setupUi(self.ventana)
        self.ventana.show()
    
    def abrirVentanaContrasena(self):
        self.ventana = QtWidgets.QMainWindow()
        self.ui = Ui_VentanaContrasena()
        self.ui.setupUi(self.ventana)
        self.ventana.show()

    #FUNCION DE PRUEBA
    def probar(self):
        print("FUNCIONA")
        
if __name__ == "__main__":
    app =  QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec())
