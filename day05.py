# 8.6 life dictionary deep copy exercise
life = {
    'animals': {
        'cats': [
            'Henry', 'Grumpy', 'Lucy'
        ],
        'octopi': {},
        'emus': {}
    },
    'plants': {},
    'other': {}
}
# 8.7 life dictionary 1st key
# print(life.keys())
# 8.8 life[animals] key 출력
print(life['animals'].keys())
# 8.9 life[animals, cats] all key 출력
print(life['animals'])
