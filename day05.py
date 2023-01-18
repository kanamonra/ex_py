# 8.10
square = {number: number**2 for number in range(10)}
print(square)
# 8.11
set_square = {number for number in range(10) if number % 2 == 0}
print(set_square)
# 8.13 zip()
a = ("The glass is half full", 'The glass is half empty', 'How did you get a glass?')
b = ('optimist', 'persist', 'troll')
zip_it = dict(zip(a, b))
print(zip_it)
# 8.14 movie dictionary
titles = ['Creature of Habit', 'Crewel Fate']
plots = ['A nun turns into a monster', 'A haunted yarn shop']
movies = dict(zip(titles, plots))
print(movies)
