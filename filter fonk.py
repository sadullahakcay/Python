words = ["apple", "swim", "clock", "me", "kiwi", "banana"]
for i in filter(lambda x: len(x)<5, words):
    print(i)