# 6.2
guess_me = 7
number = 1
while number < guess_me:
    number = number + 1
    if number == guess_me:
        print('Found it!')
        break
    if number > guess_me:
        print('too_low')

    else:
        print('oops')
