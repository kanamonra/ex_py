# 10.1 print result
class thing():
    pass

example = thing()
print(thing)   # result: <class '__main__.thing'>
print(example)  # <__main__.thing object at 0x0000023C02B0FBD0>

# 10.2 print 'abc'
class thing2:
    letters = 'abc'

print(thing2.letters)

# 10.3 'xyz' but give init
class thing3:
    def __init__(self):
        self.letters = 'xyz'

