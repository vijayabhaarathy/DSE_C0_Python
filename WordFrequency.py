#8. Input a text file (containing 1 or more paragraphs of English text) from the user, parse this file to display the frequency of occurrence of each word in this text file. Find the 3 most frequent words as well.

content=open("Assignment1_Q8.txt").read().split()

freq_words={}

for item in content:
    if item in freq_words:
        freq_words[item]+=1
    else:
        freq_words[item]=1

freq_sorted=sorted(freq_words, key=freq_words.get, reverse=True)

print(f"Words & frequencies: {freq_words}")
print(f"Three most used words: {freq_sorted[:3]}")

