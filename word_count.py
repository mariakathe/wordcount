happy = input("Enter a phrase to word count: ")

words = happy.split()

counts = {}
for word in words:
    counts[word] = counts.get(word, 0) + 1

    
print("The word frequency of your phrase is: ")
print(counts)
