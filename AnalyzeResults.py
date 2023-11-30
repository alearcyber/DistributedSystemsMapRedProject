#####################################################################################################################
# This file is for analyzing the results of the Movie Review MapReduce Program running on the whole set
# of 2000 reviews stored in OUTPUT.txt
#####################################################################################################################


file = open("OUTPUT.txt")
words = []
for line in file:
    tokens = line.strip().split('\t')
    words.append((tokens[0], int(tokens[1])))

file.close()
sorted_words = sorted(words, key=lambda x: x[1], reverse=True)


print("==== 30 Most Positive Words ====")
print("Word,Sentiment")
for word, sentiment in sorted_words[:30]:
    print(f"{word},{sentiment}")



print("==== 30 Most Negative Words ====")
print("Word,Sentiment")
for word, sentiment in sorted_words[-30:]:
    print(f"{word},{sentiment}")



