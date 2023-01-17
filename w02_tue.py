# Alcohol recommendation program
import random

alcohol_drinks = {
    'Beer': 'Chicken',
    'Soju': 'Somyeong',
    'Wine': 'Cheese',
}
alcohol_list = list(alcohol_drinks)  # extract keys
food_list =[food for food in alcohol_drinks.values()]  # extract values and append list

while True:
    alcohol = input(f'What would you like to have? '
                    f'1. {alcohol_list[0]}, '
                    f'2. {alcohol_list[1]}, '
                    f'3. {alcohol_list[2]}: '
                    f'4. Take a random recommendation, '
                    f'5. Bills: '
                    f'0. Quit the program: ')
    if alcohol == '0':
        print(f'Please join us again. Thank you')
        break
    elif alcohol == '1':
        print(f'For your choose, We like to recommend {alcohol_drinks[alcohol_list[0]]}.')
        pass
    elif alcohol == '2':
        print(f'For your choose, We like to recommend {alcohol_drinks[alcohol_list[1]]}.')
        pass
    elif alcohol == '3':
        print(f'''For your choose, We like to recommend {alcohol_drinks[alcohol_list[0]]}.''')
        pass
    elif alcohol == '4':
        print(f'''We recommend {random.choice(food_list)}'s best pal is {list(food_list)}.''')
    elif alcohol == '5':
        print('Thank you for coming. We hope you will come again.')
    else:
        print(f'Please choose a number that in our menu. For example: 1')
