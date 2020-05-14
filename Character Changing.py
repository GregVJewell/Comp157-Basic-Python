def main():
    word = 'cancelled'
    print(word)
    word = list('cancelled')
    for x in range(len(word)):
        if(word[x] == 'a' or word[x] == 'e' or word[x] == 'i' or word[x] == 'o' or word[x] == 'u'):
            word[x] = '*'
    word = "".join(word)
    print(word)

main()