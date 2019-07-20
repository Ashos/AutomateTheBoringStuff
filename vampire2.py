name = input("Enter a name: ")
age = input("Enter your age: ")

if name == 'Alice':
    print('Hi, Alice.')
elif len(age) < 12:
    print('You are not Alice, kiddo.')
elif len(age) > 100:
    print('You are not Alice, grannie.')
elif len(age) > 2000:
    print('Unlike you, Alice is not an undead, immortal vampire.')
