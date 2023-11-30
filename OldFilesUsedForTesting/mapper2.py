#!../venv/bin/python3.10


#this was the first functioning mapper I created for average the number of pixels by color.
#The input for this mapper is simple the image paths separated by newlines
import sys
from dataprocessing import *



#This is the naive example for word count without generator
def word_count_map():
    # input comes from STDIN (standard input)
    for line in sys.stdin:
        # remove leading and trailing whitespace
        line = line.strip()
        # split the line into words
        words = line.split()
        # increase counters
        for word in words:
            # write the results to STDOUT (standard output);
            # what we output here will be the input for the
            # Reduce step, i.e. the input for reducer.py
            #
            # tab-delimited; the trivial word count is 1
            print(f"{word}\t{1}")


# read data from standard in. Each line represents a job to do
def parse_input_data():
    for line in sys.stdin:
        tokens = line.strip().split(',')
        method = tokens[0]
        img_path = tokens[1]
        yield method, img_path


def mapper():
    for method, img_path in parse_input_data():
        #DO THE WORK FOR THE JOB HERE
        avg = average_pixels(img_path, method)


        #print the job to standard output
        print(f"{method}\t{avg}")





def main():
    mapper()


if __name__ == "__main__":
    main()

