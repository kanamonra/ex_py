# 10.9
class laser:
    def does(self):
        return 'disintegrate'

class claw:
    def does(self):
        return 'crush'
class smartphone:
    def does(self):
        return 'ring'

    class robot():
        def does(cls):
            print(cls())

a = laser()
b = claw()
c = smartphone()

print(a.does())
print(b.does())
print(c.does())



