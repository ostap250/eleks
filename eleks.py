word_count = dict()

with open('words.txt','r') as file:
    for line in file:
        for word in line.split():
            if word not in word_count:
                word_count[word] = 0
            word_count[word] = word_count[word] + 1

word_count = dict(sorted(word_count.items(), key=lambda item: item[1],
    reverse=1))

for key, value in word_count.items():
    print("Word '"+ key +"' appeared "+ str(value) +" times")