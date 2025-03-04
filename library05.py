from PyQt6.QtGui import QPainter, QColor, QPolygon
from PyQt6.QtCore import QPoint
import math  # Importar math para funciones trigonométricas

class Circulo:
    def __init__(self, painter, x, y, medida, color):
        self.painter = painter
        self.x = x
        self.y = y
        self.radio = medida
        self.color = color

    def dibujar(self):
        self.painter.setBrush(QColor(self.color))  # 🟢 Aplica color
        self.painter.drawEllipse(self.x, self.y, self.radio, self.radio)

class Cuadrado:
    def __init__(self, painter, x, y, medida, color):
        self.painter = painter
        self.x = x
        self.y = y
        self.lado = medida
        self.color = color

    def dibujar(self):
        self.painter.setBrush(QColor(self.color))  # 🟢 Aplica color
        self.painter.drawRect(self.x, self.y, self.lado, self.lado)

class Triangulo:
    def __init__(self, painter, x, y, medida, color):
        self.painter = painter
        self.x = x
        self.y = y
        self.tamano = medida
        self.color = color

    def dibujar(self):
        self.painter.setBrush(QColor(self.color))  # 🟢 Aplica color
        puntos = QPolygon([
            QPoint(self.x, self.y),  
            QPoint(self.x + self.tamano, self.y + self.tamano),
            QPoint(self.x - self.tamano, self.y + self.tamano)
        ])
        self.painter.drawPolygon(puntos)

class Pentagono:
    def __init__(self, painter, x, y, medida, color):
        self.painter = painter
        self.x = x
        self.y = y
        self.tamano = medida
        self.color = color

    def dibujar(self):
        self.painter.setBrush(QColor(self.color))  # 🟢 Aplica color
        angulo = 72  # 360° / 5 lados
        puntos = QPolygon([
            QPoint(
                int(self.x + self.tamano * math.cos(math.radians(i * angulo))),
                int(self.y + self.tamano * math.sin(math.radians(i * angulo)))
            )
            for i in range(5)
        ])
        self.painter.drawPolygon(puntos)