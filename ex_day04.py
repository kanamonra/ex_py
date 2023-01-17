# 7.10 리스트 컴프리헨션을 이용하여 range(10) 짝수 만들기
# number_list = [number for number in range(10) if number %2 == 0]
# print(number_list)
# 7.11 rap song
# start1 + start2 +rhymes[1]
start1 = ["fee", "fie", "foe"]
rhymes = [
    ("flop", "get a mop"),
    ("fope", "turn the rope"),
    ("fa", "get your ma"),
    ("fudge", "call the judge"),
    ("fat", "pet the cat"),
    ("fog", "walk the dog"),
    ("fun", "say we're done"),
]
start2 = "Someone better"
x = (f'{start1[0].title()}! {start1[1].title()}! {start1[2].title()}!')

for i in rhymes:
    print(f'{x} {i[0].title()}!')
    print(start2, i[1])





