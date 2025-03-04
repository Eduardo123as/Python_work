import sys
import json
import random  # Importar random para generar colores aleatorios
from PyQt6 import QtGui, QtWidgets
import urllib.request
import library05

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.label = QtWidgets.QLabel()
        canvas = QtGui.QPixmap(800, 800)
        canvas.fill(QtGui.QColor("white"))
        self.label.setPixmap(canvas)
        self.setCentralWidget(self.label)
        self.leer_json()

    def leer_json(self):
        try:
            with urllib.request.urlopen("http://localhost:8000/figuras_random") as url:
                data = json.load(url)
                print(json.dumps(data, indent=4))  # Imprime el JSON para depuración
                for figura in data["figuras"]:
                    self.dibuja_figura(figura)
        except Exception as e:
            print(f"⚠️ Error al cargar JSON: {e}")

    def generar_color_aleatorio(self):
        # Generar valores aleatorios para rojo, verde y azul
        rojo = random.randint(0, 255)
        verde = random.randint(0, 255)
        azul = random.randint(0, 255)
        return QtGui.QColor(rojo, verde, azul)  # Crear un QColor con los valores RGB

    def dibuja_figura(self, json_fig):
        canvas = self.label.pixmap()
        painter = QtGui.QPainter(canvas)

        # Generar un color aleatorio para la figura
        color = self.generar_color_aleatorio()

        if json_fig["nombre"] == "circulo":
            figura = library05.Circulo(painter, json_fig["x"], json_fig["y"], json_fig["medida"], color)
        elif json_fig["nombre"] == "cuadrado":
            figura = library05.Cuadrado(painter, json_fig["x"], json_fig["y"], json_fig["medida"], color)
        elif json_fig["nombre"] == "triangulo":
            figura = library05.Triangulo(painter, json_fig["x"], json_fig["y"], json_fig["medida"], color)
        elif json_fig["nombre"] == "pentagono":
            figura = library05.Pentagono(painter, json_fig["x"], json_fig["y"], json_fig["medida"], color)
        else:
            print(f"⚠️ No se reconoce la figura {json_fig['nombre']}")
            return

        figura.dibujar()
        painter.end()
        self.label.setPixmap(canvas)  # Actualizar el lienzo

# Iniciar la aplicación
app = QtWidgets.QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()