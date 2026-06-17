s=input("Enter a string : ").lower().replace(" ","")
t=input("Enter a string : ").lower().replace(" ","")
freq_s={}
freq_t={}
for char in s:
    if char in freq_s:
        freq_s[char]+=1
    else:
        freq_s[char]=1
for char in t:
    if char in freq_t:
        freq_t[char]=1
    else:
        freq_t[char]=1
if freq_s==freq_t:
    print("Anagram")
else:
    print("Not Anagram")
    