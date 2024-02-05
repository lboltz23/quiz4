from dataclasses import dataclass

@dataclass
class outfit:
    top:str
    bottoms:str
    price: int


outfit1 = outfit("tshirt", "jeans", 20)
outfit2 = outfit("tanktop", "skirt", 40)

def checkpriceaftersale(self) -> float:
    if self.price < 30:
        return self.price * 0.5
    else:
        return self.price * 0.2

