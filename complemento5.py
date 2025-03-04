from multimethod import multimethod
from PyQt6 import QtGui
from PyQt6.QtCore import Qt, QPointF

def dibujar_decorador(func):
    def wrapper(self, color=Qt.GlobalColor.black):
        self.painter.setBrush(color)
        func(self)
    return wrapper

class Figura:
    def __init__(self, painter: QtGui.QPainter, x, y, tamaño):
        self.x = x
        self.y = y
        self.tamaño = tamaño
        self.painter = painter

class Circulo(Figura):
    @dibujar_decorador
    def dibujar(self):
        self.painter.drawEllipse(self.x - self.tamaño, self.y - self.tamaño, self.tamaño * 2, self.tamaño * 2)

class Cuadrado(Figura):
    @dibujar_decorador
    def dibujar(self):
        self.painter.drawRect(self.x, self.y, self.tamaño, self.tamaño)

class Triangulo(Figura):
    @dibujar_decorador
    def dibujar(self):
        puntos = [
            QPointF(self.x, self.y - self.tamaño),
            QPointF(self.x - self.tamaño, self.y + self.tamaño),
            QPointF(self.x + self.tamaño, self.y + self.tamaño)
        ]
        self.painter.drawPolygon(*puntos)

class Pentagono(Figura):
    @dibujar_decorador
    def dibujar(self):
        puntos = [
            QPointF(self.x, self.y - self.tamaño),
            QPointF(self.x - self.tamaño, self.y - self.tamaño / 2),
            QPointF(self.x - self.tamaño, self.y + self.tamaño),
            QPointF(self.x + self.tamaño, self.y + self.tamaño),
            QPointF(self.x + self.tamaño, self.y - self.tamaño / 2)
        ]
        self.painter.drawPolygon(*puntos)

def dibujar_figuras(painter: QtGui.QPainter):
    figuras = [
        (Circulo, 99, 100, 40, Qt.GlobalColor.white),
        (Cuadrado, 199, 100, 50, Qt.GlobalColor.green),
        (Triangulo, 99, 200, 40, Qt.GlobalColor.blue),
        (Pentagono, 249, 200, 40, Qt.GlobalColor.yellow)
    ]

    for figura_cls, x, y, tamaño, color in figuras:
        figura = figura_cls(painter, x, y, tamaño)
        figura.dibujar(color)