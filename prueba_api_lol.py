import sys
import requests
import random
from PyQt5 import uic, QtWidgets
from PyQt5 import QtGui
from ventana15puntos import Ui_VentanaCorreo

qtCreatorFile = "nose.ui" 

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
        #BOTON DE PRUEBA
        self.botonPrueba.clicked.connect(self.probar)
    
    def generarImagen(self):
        #campeones = "http://ddragon.leagueoflegends.com/cdn/12.23.1/data/es_MX/champion.json"
        #campeon = "http://ddragon.leagueoflegends.com/cdn/12.23.1/data/es_MX/champion/LeeSin.json"
        #hechizo = "http://ddragon.leagueoflegends.com/cdn/12.23.1/img/spell/AsheSpiritOfTheHawk.png"

        if self.juegoIniciado == False:
            self.botonActualizarImagen.deleteLater()
            self.juegoIniciado = True

        #REQUEST PARA LA LISTA DE CAMPEONES
        response = requests.get("http://ddragon.leagueoflegends.com/cdn/12.23.1/data/es_MX/champion.json")
        r = response.json()
        data = r["data"]

        idsCampeones = []
        nombresCampeones = []

        for champion in data.values():
            idsCampeones.append(champion["key"])

        campeonElegido = random.choice(idsCampeones)

        #SE RECORRE CADA CAMPEÓN PARA ENCONTRAR AL ELEGIDO
        for champion in data.values():
            nombresCampeones.append(champion["id"])
            if champion["key"] == campeonElegido:     
                self.nameCampeon = champion["id"]
                nameCampeonJson = champion["id"] + ".json"
        #SE OBTIENE EL NOMBRE DEL CAMPEÓN Y SU VERSIÓN .JSON
        if self.cajaCmapeonesHecha == False:
            self.cajaCampeones.addItems(nombresCampeones)
            self.cajaCmapeonesHecha = True
        
        #REQUEST PARA OBTENER EL JSON DEL CAMPEÓN SELECCIONADO
        campeon = "http://ddragon.leagueoflegends.com/cdn/12.23.1/data/es_MX/champion/{}".format(nameCampeonJson)
        responseCampeon = requests.get(campeon)
        r = responseCampeon.json()

        #SE CREA LISTA PARA ALMACENAR LOS HECHIZOS
        listaHechizo = []

        #SE RECORREN LOS HECHIZOS Y SE AGREGAN A LA LISTA
        for hechizo in r["data"][self.nameCampeon]["spells"]:
            listaHechizo.append(hechizo["id"])

        #SE ELIGE ALEATORIAMENTE UN HECHIZO
        nameHechizo = random.choice(listaHechizo)
        nameHechizoPng = nameHechizo + ".png"
        #SE OBTIENE EL NOMBRE Y SU VERSION .PNG

        #REQUEST PARA OBTENER LA IMAGEN DEL HECHIZO
        responseHechizo = requests.get("http://ddragon.leagueoflegends.com/cdn/12.23.1/img/spell/{}".format(nameHechizoPng))

        #SE GUARDA LA IMAGEN DEL HECHIZO
        with open('image.jpg', 'wb') as f:
            f.write(responseHechizo.content)
        pixmap = QtGui.QPixmap("image.jpg")
        self.etiquetaImagen.setPixmap(pixmap)
        
    def enviarRespuesta(self):
        if self.cajaCampeones.currentText() == self.nameCampeon:
            self.contador += 1
            if self.contador == 1 and self.quincePuntosObtenidos == False:
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
        
    #FUNCION DE PRUEBA
    def probar(self):
        self.ventana.close()
        
if __name__ == "__main__":
    app =  QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec())