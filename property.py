from collections.abc import Iterable

class Flower:
    def __init__(self, name, color):
        self._name=name
        self._color = color

    @property
    def name(self)
        return self._name, self._color

    @name.setter
    def name(self, new_name):
        if not isinstance(new_name, str):
            var1, var2 = new_name
        else:
            var1 = new_name
            var2 = "No new color"
        self._name = var1
        self._color = var2
        
    def main():
        flower = Flower("rose", "red")
        print("flower is", flower.name)

        flower.name = "petunia"

        print("new flower is", flower.name)

    if __name__=="__main__":
        main()


    

