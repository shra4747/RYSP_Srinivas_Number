with open('oxford.txt', 'r+') as f:
    x = ""
    for line in f.readlines():
        try:
            x += line.split(" ")[0]
        except:
            continue
    with open('oxforddict.txt', 'w+') as f:
        f.write(x)