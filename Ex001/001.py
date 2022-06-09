text = input('Enter a sentence: ')

for i in text.split(' '):
    if i.find('абв') == -1:
        print(i, end=' ')
