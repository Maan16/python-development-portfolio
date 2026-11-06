# name= input ('your name? ')
# color= input('your color? ')
# print(name + " likes " + color )

command = ''

while command != 'quit':
    command = input('Enter your command >').lower()

    if command == 'start':
        print('Car started')

    elif command == 'stop':
        print('car stopped')

    elif command == 'help':
        print('''
    Type Start: to start the car
    Type Stop: to stop the car
    Type Quitt: to exit the game
              ''')

    elif command == 'quit':
        break

    else:

        print('I dont understand')

        # just checking uploads



