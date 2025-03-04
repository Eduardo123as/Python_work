from flask import Flask, jsonify
import json
import random

app = Flask(__name__)

def figuras_random():
    figuras = []
    nombres = [
        ("circulo", "white"),
        ("cuadrado", "green"),
        ("triangulo", "blue"),
        ("pentagono", "yellow")
    ]

    for _ in range(random.randint(3, 10)):
        nombre, color = random.choice(nombres)
        figuras.append({
            "nombre": nombre,
            "x": random.randint(0, 400),
            "y": random.randint(0, 400),
            "medida": random.randint(20, 100),
            "color": color
        })

    return {"figuras": figuras}

@app.route('/figuras_random', methods=['GET'])
def get_figuras():
    return jsonify(figuras_random())

if __name__ == '__main__':
    app.run(port=8000, debug=True)
