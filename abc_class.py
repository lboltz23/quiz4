from abc import ABC, abstractmethod
import os

class Fruits(ABC):

@abstractmethod
def coloroffruit(self)
    pass

@abstractmethod
def shapeoffruit(self)
    pass

class Orange(Fruits):

    def coloroffruit(self):
        print("I am the color orange")

    def shapeoffruit(self):
        print("I am a circle")

class Blueberry(Fruits):

    def coloroffruit(self):
        print("I am the color blue")

    def shapeoffruit(self):
        print("I am a circle")

