from random import shuffle

print('Normal edition')
input('press enter to countinue')

people = ['Brad', 'Dylan', 'Elias', 'Jonah', 'Mahathi', 'Michael', 'Nathan', 'Yonas']
shuffle(people)
print('Randomly sorted')
print(people)

print()

people.sort(reverse=True)
print('Reverse Sorted')
print(people)

print()

people.sort()
print('Sorted')
print(people)

print('Creative edition')
input('press enter to countinue')

