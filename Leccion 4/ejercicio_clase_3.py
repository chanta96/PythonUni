#escribir 4 jugadores de la seleccion, en un diccionario, con sus datos
seleccionArgentina = {'10':{'nombre':'Leopoldo Messi',
                            'edad':35,'equipo actual':'Paris Saint Germain',
                            'altura':1.69,'Precio de mercado':'50.000.000€',
                            'Posicion':'Enganche'},
                      '24':{'Nombre':'Gonzalo Montiel',
                            'edad':21,'equipo actual':'Sevilla',
                            'altura':1.75,'Precio de mercado':'14.000.000€',
                            'Posicion':'Lateral derecho'},
                      '9':{'Nombre':'Julian Alvarez',
                           'edad':22,'equipo actual':'Manchester City',
                           'altura':1.73,'Precio de mercado':'23.000.000€',
                           'Posicion':'Centro delantero'},
                      '18':{'Nombre':'Guido Rodriguez',
                            'edad':28,'equipo actual':'Real Betis',
                            'altura':1.85,'Precio de mercado':'25.000.000€',
                            'Posicion':'Mediocampista defensivo'},
                      '2':{'Nombre':'MArtinez Quarta',
                           'edad':28,'equipo actual':'Fiorentina',
                           'altura':1.83,'Precio de mercado':'12.000.000€',
                           'Posicion':'Defensa central'},
                      '20':{'nombre':'Exequiel Palacios',
                           'edad':'23','equipo actual':'Bayer 04 Leverkusen',
                           'altura':1.77,'Precio de mercado':'15.000.000€',
                           'Posicion':'Mediocampista de Creaciones'}
                      }

for k,v in seleccionArgentina.items():
    print(k,v)
