#4. Given an array which may contain duplicates, print all elements and their frequencies.

num=[1,1,1,2,3,3,3,3,3,4,1,2,3,4,5]

freq={}
for item in num:
    if item in freq:
        freq[item]=freq[item]+1
    else:
        freq[item]=1
        
print(freq)
