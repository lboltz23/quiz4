from dataclasses import dataclass

@dataclass
class outfit:
    top:str
    bottoms:str
    price: int


outfit1 = outfit("tshirt", "jeans", 20)
outfit2 = outfit("tanktop", "skirt", 40)

print(outfit1)
print(outfit2)