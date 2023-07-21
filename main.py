from flask import Flask, render_template

#creando variable

app = Flask(__name__)

@app.route('/')
def index():
    return 'hola 2687386'

@app.route('/paises')
def paises():
    ''' Lista en python '''
    continentes = [
        [
            {
                'continente':'América',
                'paises': 
                [ 
                        'Colombia',
                        'Perú',
                        'Argentina',
                        'Chile', 
                        'Venezuela', 
                        'Brasil', 
                        'Panamá'
                ]
            }
        ],
        [
            {
                'continente':'Europa',
                'paises': 
                [ 
                    'Irlanda',
                    'Francia',
                    'España'
                ]
            }
        ],
        [
            {
                'continente':'Asia',
                'paises':
                [
                    'China',
                    'Vietnam',
                    'Korea'
                ]
            }
        ],
    ]
    largo_continentes=[ len(continentes[0][0]["paises"]), 
                        len(continentes[1][0]["paises"]), 
                        len(continentes[2][0]["paises"])
                    ]
    print(largo_continentes)
    # pais = ', '.join(map(str, continentes))

    # continentes = [
    #         [
    #         'Colombia',
    #         'Perú',
    #         'Argentina',
    #         'Chile', 
    #         'Venezuela', 
    #         'Brasil', 
    #         'Panamá'
    #         ],
    #         [
    #             'China',
    #             'Vietnam',
    #             'Korea'
    #         ],
    #         [
    #             'Irlanda',
    #             'Francia',
    #             'España'
    #         ],
    #         [
    #             'Australia',
    #             'Nueva Guinea',
    #             'Tonga'
    #         ]
    #     ]
    '''' Convertir array a String separado por lo que se le indique en las comillas sencillas'''
    user = 'Deyby Ariza'
    return render_template('paises_listas.html', 
                           user =  user,
                           continentes = continentes,
                           largo_continentes = largo_continentes
                           )

# Estructura
# nombre
# paises - nombre, capital, moneda , población, superficie en km2
