T = int(input())

for _ in range(T):
    word = input()
    letters = list(word)
    letters_set = list(set(letters))

    if len(letters_set) == 1:
        print('NO')
    else:
        uniq1 = letters_set[0]
        uniq2 = letters_set[1]

        index_uniq1 = letters.index(uniq1)
        index_uniq2 = letters.index(uniq2)

        letters[index_uniq1], letters[index_uniq2] = \
        letters[index_uniq2], letters[index_uniq1]

        print('YES')
        print(''.join(letters))

