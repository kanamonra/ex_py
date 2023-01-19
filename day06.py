# 9.4 OopsException 만들기

class OopsException(Exception):
    pass

try:
    raise OopsException("Caught an oops (; ꒪ö꒪) ")
except OopsException as ehe:
    print(ehe)

shorty = ['Hello', 'I', 'am', 'a', 'robot']
for word in shorty:
    if word.istitle():
        print(f"This word is already got title on it. {OopsException(word)}")


