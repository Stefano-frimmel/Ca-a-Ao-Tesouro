import eel
import random

# Inicializa o Eel apontando para a pasta web
eel.init('web')

# Tamanho do mapa
MAP_SIZE = 10

# Geração aleatória do tesouro
treasure_x = random.randint(0, MAP_SIZE - 1)
treasure_y = random.randint(0, MAP_SIZE - 1)

@eel.expose
def check_position(x, y):
    distance = abs(x - treasure_x) + abs(y - treasure_y)

    if distance == 0:
        return "🎉 Tesouro encontrado!"
    elif distance <= 1:
        return "🔥 Muito quente!"
    elif distance <= 3:
        return "🌡️ Quente"
    elif distance <= 6:
        return "🧊 Frio"
    else:
        return "❄️ Muito frio"

@eel.expose
def reset_game():
    global treasure_x, treasure_y
    treasure_x = random.randint(0, MAP_SIZE - 1)
    treasure_y = random.randint(0, MAP_SIZE - 1)
    return "Novo jogo iniciado!"

# Inicia o app no navegador
eel.start('index.html', size=(500, 600))