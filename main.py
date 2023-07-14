from flask import Flask

#creando variable

app = Flask(__name__)

@app.route('/')
def index():
    return 'hola 2687386'