word = input() + ' запретил букву'
for i in range(ord('а'), ord('я')+1):
    if word and chr(i) in word:
        print(word + ' ' + chr(i))
        word = word.replace(chr(i), '')
        word = " ".join(word.split())