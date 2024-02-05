class Flower:
    def __init__(self, name, color):
        self._name=name
        self._color = color

    def get_name(self):
        return self._name, self._color

    def set_name(self, new_name, color):
        self._name = new_name
        self._color = color
        
    def main():
        flower = Flower("rose", "red")
        print("flower is", flower.get_name())

        flower.set_name("petunia", "red")

        print("new flower is", flower.get_name())

    if __name__=="__main__":
        main()
