from Add_Function import function_add as Add
from Product_Function import function_multiply as Multiply
from Subtract_Function import function_subtract as Subtract

def use_functions() -> None:
    number1 = input("What is your first favorite number?\n")
    number2 = input("What is your second favorite number?\n")

    Add.adding(number1, number2)

    Multiply.multiplying(number1, number2)

    Subtract.difference(number1, number2)


    if __name__=="__main__":
        use_functions()