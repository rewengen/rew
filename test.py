print('Heyo')

import random

word = random.choice(['морская', 'десять', 'ресторатор'])

# word_list = ['_' for i in word]
# print(word_list)

# THE SAME
word_list = []
for i in word:
    word_list.append('_')
print("".join(word_list))
errors = 0

while True:

    user_letter = input('Введите букву\n')
    find_letter = False

    for index, letter in enumerate(word):
        if user_letter == letter:
            find_letter = True
            word_list[index] = user_letter
    if not find_letter:
        errors += 1
        print(f'Такой буквы нет в слове. Ошибок: {errors}/3')

    print("".join(word_list))

    if '_' not in word_list:
        print(f'\nПобеда! Ошибок: {errors}/3')
        break
    elif errors == 3:
        print('\nПоражение')
        break
