for i in range(5):
    word = input('Enter a word:')
    if 'x' in word.lower():
        continue
    print(f'You entered: {word}')