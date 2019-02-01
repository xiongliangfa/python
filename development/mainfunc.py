class AnimalActions:
    def quack(self): return self.strings['quack']
    def bark(self): return self.strings['bark']

class Duck(AnimalActions):
    strings = dict(
        quack = "Quaaaaak!",
        bark = "The duck cannot bark.",
    )


class Dog(AnimalActions):
    strings = dict(
        quack = "The dog cannot quack.",
        bark = "Arf!",
    )

def in_the_doghouse(dog):
    print(dog.bark())

def in_the_forest(duck):
    print(duck.quack())

def main():
    donald = Duck()
    fido = Dog()

    print("- In the forest:")
    for o in ( donald, fido ):
        in_the_forest(o)

    print("- In the doghouse:")
    for o in ( donald, fido ):
        in_the_doghouse(o)

if __name__ == "__main__":
    ...