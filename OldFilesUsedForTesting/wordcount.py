#!../venv/bin/python3.10
import argparse
import sys




# Read lines from standard input
def map_parse_input_data():
    output = dict()
    #Fix the rest
    for line in sys.stdin:
        tokens = line.strip().split(' ')
        method = tokens[0]
        img_path = tokens[1]
        yield method, img_path



def mapper():
    pass


def main():
    parser = argparse.ArgumentParser(description='Mapper and Reducer for wordcount in MapReduce.')
    parser.add_argument('-m', '--map', action='store_true')
    parser.add_argument('-r', '--reduce', action='store_true')
    args = parser.parse_args()


    if args.map:
        print("selected map")
    elif args.reduce:
        print("selected reduce")
    else:
        print("selected neither")


if __name__ == "__main__":
    main()
