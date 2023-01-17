# 8.1 english-french
e2f = {'dog': 'chien', 'cat': 'chat', 'walrus': 'morse'}
# 8.2 print walrus
print(e2f.get('walrus'))
# 8.3 eng - french
f2e = {}
for k, v in e2f.items():
    f2e[v] = [k]
print(f2e)