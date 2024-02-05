import argparse

def argument() -> None:
    parser=argparse.ArgumentParser()
    parser.add_argument(help="enter string", dest="input_string", type=str)
    parser.add_argument(help="enter integer", dest="input_integer", type=int)
    parser.add_argument(help="enter float", dest="input_float", type=float)

    args = parser.parse_args()

    string = args.input_string
    integer=args.input_integer
    floats = args.input_float


if __name__=='__main__':
    argument()
