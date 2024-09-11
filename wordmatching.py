def match_words(words):
    count = 0
    lst = []

    for word in words:


        if len(word) > 1 and word[0] == word[-1]:
            count = count + 1
            lst.append(word)

    print("list of words with first and last letter are same\n", lst)
    return count

li = ['abc', 'cfc','xyz','aba','racecar']

cnt = match_words(li)



print("Number of words having same first and last letter are same:",cnt)