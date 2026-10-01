games = list()
game = input("Ingresar el juego (0 - detener ingreso)")
game = game.lower()
while game != "0":
    if game in games:
        print("El juego ya esta ingresado")
    else:
        games.append(games)
    game = input("Ingresar el juego (0 - detener ingreso)")
    game = game.lower()
games.sort()
print("Lista de juegos:", games)