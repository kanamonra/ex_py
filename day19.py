# 카운드다운
# 10장 문제
def countdown(n):
    if n == 0:
        print('Launched!!!')
    else:
        print(n)
        countdown(n-1)


in_num = int(input('How much time do you want to count? --> '))
countdown(in_num)