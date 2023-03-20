word = input("enter a word: ")
for letter in word:
    if org(letter) >= 97 and org(letter)<=122:
        print(chr(org(letter)-32))
    else:
        print(letter)
        