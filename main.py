from objects import Object
from move import MoveFront

if __name__ == '__main__':
    spaceship = Object({"speed": (-7, 3), "coord": (12, 5)})
    MoveFront().action(spaceship)
    print(spaceship.params)
