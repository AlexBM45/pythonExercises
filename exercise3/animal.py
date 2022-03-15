import animals

menu = {
    '1': '1 - bat',
    '2': '2 - bear',
    '3': '3 - duck',
    '4': '4 - camel',
    '5': '5 - cow',
    '0': '6 - Exit'
}

class Animal():
    def __init__(self,tipo):
        self.tipo = tipo

    def mostrarAnimal(self):
        animal_art = getattr(animals, self.tipo)
        return animal_art


if __name__ == '__main__':
    for option in menu:
        print(menu.get(option)) #muestra el valor de la llave

    while True:
        userInput = input('Opción elegida: ')
        if userInput == '0':
            break
        elif userInput in menu:
            menuValue = menu.get(userInput).split(' ')[2]
            animal = Animal(menuValue)
            print(animal.mostrarAnimal())
        else:
            print('Opción inválida')
            

