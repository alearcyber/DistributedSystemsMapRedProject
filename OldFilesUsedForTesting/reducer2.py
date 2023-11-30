#!../venv/bin/python3.10
from operator import itemgetter
import sys


def word_count_reduce():
    current_word = None
    current_count = 0
    word = None

    # input comes from STDIN
    for line in sys.stdin:
        # remove leading and trailing whitespace
        line = line.strip()

        # parse the input we got from mapper.py
        word, count = line.split('\t', 1)

        # convert count (currently a string) to int
        try:
            count = int(count)
        except ValueError:
            # count was not a number, so silently
            # ignore/discard this line
            continue

        # this IF-switch only works because Hadoop sorts map output
        # by key (here: word) before it is passed to the reducer
        if current_word == word:
            current_count += count
        else:
            if current_word:
                # write result to STDOUT
                print(f"{current_word}\t{current_count}")

            current_count = count
            current_word = word

    # do not forget to output the last word if needed!
    if current_word == word:
        print(f"{current_word}\t{current_count}")


def reduce_without_generator():

    #data for aggregating similar categories
    recent_method = None
    means = []



    # input comes from STDIN
    for line in sys.stdin:

        # parse the input from mapper.py
        method, mean = line.strip().split('\t', 1)

        #convert to appropriate datatypes
        mean = float(mean)


        #AGGREGATE HERE

        #two cases: Moving onto new method to aggregate, continuing aggregating.
        if recent_method == method: # continue aggregating
            means.append(mean)
        else: #encountered a new one
            #aggregate and print out the method being moved on from, if it existed
            if recent_method: #it does exist
                final_mean = sum(means) / len(means)
                print(f"{recent_method}\t{final_mean}")

            #reset the list used for aggregating and assign new current method
            means = [mean]
            recent_method = method

    #Since printing (output kinda) only happens when a new method is encountered, the last one will never be
    # printed, so go ahead and handle last method here
    final_mean = sum(means) / len(means)
    print(f"{recent_method}\t{final_mean}")



#expects input to be a color enum and average for that image, string and float, tab separated.
def read_mapped_data():

    #read thru standard input and parse the data
    for line in sys.stdin:
        try:
            tokens = line.strip().split('\t')
            method = tokens[0]
            mean = float(tokens[1])
            yield method, mean
        except:  # throw out data if it is not properly formatted
            print("THREW STUFF AWAY")
            pass


def reduce():

    recent_method = None
    count = 0
    total = 0


    for method, mean in read_mapped_data():
        # AGGREGATE HERE
        #if recent_method is None:


        # two cases: Moving onto new method to aggregate or continuing aggregating.
        if recent_method == method: # continue aggregating
            count += 1
            total += mean
        else: # encountered new method
            # aggregate and print out the method being moved on from, if it existed
            if recent_method:  # it does exist
                final_mean = total / count
                print(f"{recent_method}\t{final_mean}")

            # reset the list used for aggregating and assign new current method
            count = 0
            total = 0
            recent_method = method


    # Since printing (output kinda) only happens when a new method is encountered, the last one will never be
    # printed, so go ahead and handle last method here
    final_mean = total / count
    print(f"{recent_method}\t{final_mean}")




def reduce2():
    # data for aggregating similar categories
    recent_method = None
    means = []

    # input comes from STDIN
    for method, mean in read_mapped_data():

        # parse the input from mapper.py
        # convert to appropriate datatypes
        mean = float(mean)

        # AGGREGATE HERE

        # two cases: Moving onto new method to aggregate, continuing aggregating.
        if recent_method == method:  # continue aggregating
            means.append(mean)
        else:  # encountered a new one
            # aggregate and print out the method being moved on from, if it existed
            if recent_method:  # it does exist
                final_mean = sum(means) / len(means)
                print(f"{recent_method}\t{final_mean}")

            # reset the list used for aggregating and assign new current method
            means = [mean]
            recent_method = method

    # Since printing (output kinda) only happens when a new method is encountered, the last one will never be
    # printed, so go ahead and handle last method here
    final_mean = sum(means) / len(means)
    print(f"{recent_method}\t{final_mean}")




def main():
    reduce2()

if __name__ == "__main__":
    main()


