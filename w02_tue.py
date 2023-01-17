a = {'green' : 'go', 'red' : 'stop'}
# for i in range(len(a)):
#     print(a.keys())
# for a in enumerate(a):   # tuple version
#    print(a[1])

# combine with **a **b
first = {'a': 'agony', 'b': 'bliss'}
second = {'b': 'bills', 'c': 'cat'}
print({**first, **second})           # same result

# combine with update() example
third = {'g': 'girl', 'e': 'emo'}
first.update(second)
print(first)   # same result

# deepcopy
second_copy = second.copy()
second['b'] = 'm'
print(second)

# compare dictionary
print(first == second)
print(second == second_copy)

