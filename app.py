from argparse import ArgumentParser

parser = ArgumentParser(description = "An addition program")

parser.add_argument("add", nargs = '*', metavar = "num", type = int, 
                     help = "All the numbers separated by spaces will be added.")

def main():
    args = parser.parse_args()
    if len(args.add) != 0:
        print(sum(args.add))