""" First approach """
name = input('First and last name to reverse -> ')
words = name.split(" ")
for word in words:
    last_index = len(word) - 1
    for i in range(last_index, -1, -1):
        print(word[i], end='')
    print(end=' ')
print(end='\n')

''' Second approach '''
name = input('First and last name to reverse -> ')
first, last = name.split()
print(first[::-1], last[::-1])
