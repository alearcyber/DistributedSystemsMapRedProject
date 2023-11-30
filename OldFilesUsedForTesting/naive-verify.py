#!../venv/bin/python3.10
"""
does the naive verification of average rgb values of the
"""
from dataprocessing import *





def verify_colors():

    reds = []
    greens = []
    blues = []

    file = open("imagelist.txt")
    for line in file:
        reds.append(average_pixels(line.strip(), RED)[0])
        greens.append(average_pixels(line.strip(), GREEN)[0])
        blues.append(average_pixels(line.strip(), BLUE)[0])
    file.close()

    rm = sum(reds) / len(reds)
    gm = sum(greens) / len(greens)
    bm = sum(blues) / len(blues)

    print("average of all the reds:", rm)
    print("average of all the greens:", gm)
    print("average of all the blues:", bm)





def main():
    verify_colors()




if __name__ == "__main__":
    main()


