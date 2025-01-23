import os

os.system("clear")

print('Capitalizing the first letter of each word in a string.')

sentence = input('Enter a sentence: ')
print('You entered:', sentence)

result = ''

pre = ' '
for ch in sentence:
    if pre == ' ':
        print(ch.upper(), end='')
    else:
        print(ch, end='')
    pre = ch

# if there is no period at the end of the sentence, add one

if sentence[-1] != '.':
    print('.')
