# 5.4 "새 스타일로 매일 쓰기"
# 'Dear {1} {0},'.format(salutation, name)
# 'Hello, {}'.format(name)

letter_1 = '    Dear {0} {1}'.format('salutation', 'name')
letter_2 = '    Thank you for your letter. We are sorry that our {0} {1} in your {2}.'.format('product', 'verbed', 'room')
letter_3 = '    Please note that it should never be used in {0}, especially near any {1}.'.format('room', 'animals')
letter_4 = '''    Send us your receipt and {0} for shipping and handling. We will send you another {1} that, in our tests, in {2}% less likely to have {3}'''.format('amount', 'product', 'percent', 'verbed')
letter_5 = '''        Thank you for you support.
        Sincerely,
        {0}
        {1}'''.format('Spokesman', 'job_title')
print(letter_1)
print(letter_2)
print(letter_3)
print(letter_4)
print(letter_5)
