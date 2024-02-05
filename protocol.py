from typing import Protocol
import os

class Fruits(Protocol):
    def coloroffruit(self) -> None:
        pass

    def shapeoffruit(self) -> None:
        pass

class Orange:
    def coloroffruit(self)-> None:
        print("I am the color orange")

    def shapeoffruit(self)-> None:
        print("I am a circle")

class Blueberry:

    def coloroffruit(self)-> None:
        print("I am the color blue")

    def shapeoffruit(self)-> None:
        print("I am a circle")

