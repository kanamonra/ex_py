# 6.3
guess_me = 5
number = 1
while number < guess_me:
    for number in range(0, 10):
        if number == guess_me:
            print('Found it!')
        print('too low')
    number = number + 1
    if number == guess_me:
        print('Found it!')

    if number > guess_me:
        print('oops')
        break
