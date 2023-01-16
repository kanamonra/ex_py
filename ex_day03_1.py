# 5.5 letter.format()
salutation = 'Mr'
name = 'Bob'
product = 'hat'
verbed = 'putting on foot'
room = 'usage is for head'
animals = 'not foot'
amount = '30'
percent = '40'
Spokesman = 'Monica'
job_title = 'CEO'

letter_1 = '    Dear {0} {1}'.format(salutation, name)
letter_2 = '    Thank you for your letter. We are sorry that our {0} {1} in your {2}.'.format(product, verbed, room)
letter_3 = '    Please note that it should never be used in {0}, especially near any {1}.'.format(room, animals)
letter_4 = '''    Send us your receipt and {0} for shipping and handling. We will send you another {1} that, in our tests, in {2}% less likely to have {3}'''.format(amount, product, percent, verbed)
letter_5 = '''        Thank you for you support.
        Sincerely,
        {0}
        {1}'''.format(Spokesman, job_title)
print(letter_1)
print(letter_2)
print(letter_3)
print(letter_4)
print(letter_5)