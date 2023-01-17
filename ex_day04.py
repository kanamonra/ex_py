# 7.8 리스트 만들기
secret = ['Groucho', 'Chico', 'Harpo']
# 7.9 Harpo의 첫글자만 소문자로 변경
secret[-1] = secret[-1].lower()
print(secret)
# 7.9 순서를 바뀌기
secret.reverse()
secret[-3] = secret[-3].title()
print(secret)
