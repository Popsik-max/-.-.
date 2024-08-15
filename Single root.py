def single_root_words(root_word, *other_words):
    same_words = []
    for i in range(len(other_words)):
        word = str(other_words[i])
        if root_word.lower() in word.lower():
            same_words.append(word)
            continue
        elif word.lower() in root_word.lower():
            same_words.append(word)
            continue
        else:
            i+=1
            continue


    return (same_words)

result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')
print(result1)
print(result2)

