def censor(text, word):
    bleep = "*" * len(word)
    #print(bleep)
    space = " "
    text  = text.split()
    i = 0
    #print(text)
    for w in text:
        if w == word:
            text[i] = bleep
            i += 1
        else:
            i += 1
            continue
        
    print(space.join(text))
    return space.join(text)

censor("Yo go fro yo go",  "go")
