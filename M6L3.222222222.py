games = ['dota 2', 'cs go', 'warface', 'minecraft']
searching = input('Solicitud:')
searching = searching.lower()
if searching in games:
    print("Solicitudd encontrada")
else:
    print("Deseo no esta adentro de las librerias")